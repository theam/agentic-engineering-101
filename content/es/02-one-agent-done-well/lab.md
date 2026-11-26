---
title: "Laboratorio 2 — Un agente, bien usado"
module: 2
kind: lab
minutes: 60
level: foundation
last_reviewed: 2026-09-17
---

# Laboratorio 2 — Un agente, bien usado

## Objetivo

Implementar la issue **S3** del proyecto de prácticas (`S3: Mostrar estadísticas de lectura`) con un solo agente, recorriendo explorar → conversar → planificar → construir → verificar → hacer commit.

Mientras trabajas, lleva un **registro de correcciones**: una línea cada vez que tengas que corregir al agente. El pull request es el resultado visible, pero el registro es el verdadero producto de este laboratorio. Cada corrección te dice algo que faltaba: contexto, una comprobación, una decisión o una pregunta mejor. El [laboratorio 4](../04-context-is-infrastructure/lab.md) convierte algunas de esas líneas en reglas.

S3 parece trivial: mostrar cuatro líneas con cuentas. No lo es. La issue fija la salida y la zona horaria, pero deja abiertas decisiones fáciles de pasar por alto: cómo probar "este año" sin depender del día en que se ejecutan los tests y qué hacer con datos que la issue no menciona. La idea de este laboratorio es encontrarlas en la conversación, no en el diff.

## Antes de empezar

- Tienes tu propia copia del proyecto de prácticas del [laboratorio 0](../00-start-here/lab.md), y `python -m unittest` pasa en `main`. (Usa `python3` donde ponga `python` si así se llama Python 3 en tu máquina.)
- Parte de un `main` actualizado, en un worktree nuevo:

  ```bash
  cd ~/code/shelf
  git fetch origin
  git worktree add --no-track -b s3-stats ../shelf-s3 origin/main
  cd ../shelf-s3
  ```

- Si S3 todavía no es una issue en tu repositorio, créala a partir del [catálogo de issues de prácticas](../../../practice/issues/es.md) como en el [laboratorio 0](../00-start-here/lab.md#antes-de-empezar): `gh issue create --title "S3: Mostrar estadísticas de lectura" --body-file -`, pega su cuerpo sin la línea de "Seguridad en paralelo" y termina con Ctrl+D. Anota su número; los prompts de abajo usan `#3`.
- Crea `corrections.md` en tus notas (no en el repositorio):

  ```markdown
  | # | Fase | Qué corregí | Qué faltaba | Qué lo habría evitado |
  |---|---|---|---|---|
  ```

  "Qué faltaba" es una de estas opciones: **contexto** (el agente no podía saberlo), **verificación** (podía comprobarlo y no lo hizo), **decisión** (una elección de producto que nadie había tomado), **instrucción** (lo sabía y lo ignoró) o **modelo** (un error sin más).

- Abre una sesión en el worktree (`claude` o `codex`). Usa el modelo más potente al que tengas acceso.

**En tu propio repositorio:** elige una funcionalidad pequeña que toque entre dos y cinco archivos y que esconda una pregunta de definición: una cuenta, un rango de fechas, un "activo" o un "reciente", una regla de redondeo, una zona horaria. Asegúrate de que el repositorio tiene tests que el agente pueda ejecutar. Todo lo que sigue vale cambiando los nombres de shelf por los tuyos.

## Pasos

### 1. Explorar (5 minutos)

```text
Vamos a trabajar en la issue #3 (léela con gh issue view 3).
Todavía no escribas código. Lee shelf/models.py, shelf/store.py, los módulos
de shelf/commands/ y los tests. Después dime en menos de 150 palabras: cómo
cambia el estado de un libro, cuándo se rellena finished_at, en qué zona
horaria se guardan las marcas de tiempo y qué acepta shelf add como estado.
```

**Fíjate en:** respuestas que citan archivos. En el código actual, `finished_at` se rellena cada vez que un libro pasa a `done`, lo que incluye `shelf add … --status done`; las marcas de tiempo son cadenas ISO 8601 en UTC; y `shelf add` todavía no valida `--status` (de eso se encarga la issue S6), así que un archivo de estantería ya puede contener un estado como `finished`. Si el agente te pregunta algo que el código responde, contesta "Lee más código para responder tus propias preguntas." y anótalo como corrección.

**Punto de control:** puedes nombrar dos tipos de datos con los que se encontrará S3 y que la issue no menciona.

### 2. Conversar (10 minutos)

```text
Hablemos antes de construir. La issue fija la salida y dice UTC.
Dame opciones, con sus pros y contras, para dos preguntas abiertas:
1. Cómo probar "finished this year" para que los tests pasen sea cual sea el
   año en que se ejecuten.
2. Qué debe hacer stats con datos que la issue no menciona, como un libro
   añadido directamente como done o un estado que no sea to-read, reading ni done.
Recomienda una opción para cada pregunta. No escribas código hasta que te
diga que construyas.
```

**Fíjate en:** para la pregunta 1, opciones reales, como tests que escriben el archivo de la estantería con marcas de tiempo fijas, una función que recibe la fecha actual como parámetro (no como opción de la línea de comandos; elegir el año está fuera de alcance), o las dos cosas. Para la pregunta 2, un agente que se da cuenta de que la issue dice que "aparecen todos los estados" pero no dice nada de los estados desconocidos, y que pregunta en lugar de decidir en silencio.

Si al agente se le escapa un caso que tú ves, no le des la respuesta todavía. Pregunta: "¿Qué datos harían que estas cuentas salieran mal?" Si sigue sin verlo, díselo y anota una corrección.

Decide en una o dos frases. Por ejemplo:

```text
Los tests escriben el archivo de la estantería con valores fijos de
finished_at, y la función que cuenta recibe la fecha de hoy como parámetro,
que por defecto es ahora en UTC. Un libro añadido como done cuenta como
cualquier otro libro done, porque la issue lo define por finished_at. Los
estados desconocidos no aparecen en ninguna línea; dilo en el pull request.
```

**Punto de control:** tu decisión está escrita y `git status` no muestra cambios.

### 3. Planificar (de 5 a 10 minutos)

```text
Escribe el plan en menos de 25 líneas: archivos que vas a añadir o cambiar,
la salida exacta para una estantería de ejemplo, los tests que vas a añadir y
por qué fallaría cada uno sin el cambio, cómo evitan los tests depender de la
fecha de hoy y lo que no vas a hacer. Después espera.
```

Revísalo con esta lista:

- [ ] Añade `shelf/commands/stats.py` y `tests/test_stats.py`, y no cambia nada más. La issue dice que no hace falta cambiar ningún otro archivo.
- [ ] La salida son exactamente las cuatro líneas de la issue, en orden, con ceros en una estantería vacía.
- [ ] Un test cubre el cambio de año con marcas de tiempo fijas (un libro terminado el año pasado no cuenta), y ningún test lee el reloj real para decidir qué esperar.
- [ ] Dice cómo se tratan los estados desconocidos, según tu decisión.
- [ ] Enumera lo que queda fuera de alcance: nada de estadísticas por autor o etiqueta, nada de gráficos, ninguna opción para elegir el año.

Corrige el plan con mensajes de una frase. Anota cada corrección.

> [!TIP]
> Si tu agente tiene modo plan (consulta los [modos de permisos](https://code.claude.com/docs/en/permission-modes) de Claude Code, o el modo plan en [las buenas prácticas de Codex](https://learn.chatgpt.com/guides/best-practices)), prueba los pasos 1–3 en ese modo y compáralo con la conversación. Apunta cuál *te* mantuvo revisando la intención en lugar del código.

**Punto de control:** has respondido "ok" a un plan que cumple la lista.

### 4. Construir (de 10 a 15 minutos)

```text
Constrúyelo. Escribe primero los tests y ejecútalos para demostrar que fallan.
Después implementa. Después ejecuta toda la batería con python -m unittest y
pega la salida. Para cualquier ejecución manual del comando, apunta
SHELF_PATH a un archivo temporal.
```

No te quedes mirando. Vuelve cuando informe.

**Fíjate en:** una ejecución que falla antes de la implementación, otra que pasa después y la salida pegada tal cual, no resumida. Después comprueba tú el alcance:

```bash
git status
git diff --stat
```

**Punto de control:** `python -m unittest` termina en `OK`, viste fallar primero los tests nuevos y solo han cambiado los archivos del plan.

### 5. Verificar más allá de los tests (5 minutos)

```text
¿Tenemos algún efecto secundario? Comprueba que stats nunca escribe el archivo
de la estantería y piensa en el cambio de año en UTC.
```

Después pide una salida real:

```text
Apunta SHELF_PATH a un archivo temporal. Añade tres libros, empieza el libro 1,
termina el libro 2, añade un cuarto libro con --status done y después ejecuta
shelf stats. Enséñame los comandos exactos y la salida.
```

**Fíjate en:** con las decisiones de ejemplo del paso 2, exactamente esta salida:

```text
to-read: 1
reading: 1
done: 2
finished this year: 2
```

Si decidiste otra cosa (por ejemplo, no contar los libros añadidos directamente como done), calcula tú la salida esperada *antes* de leer la del agente. Si no coinciden, pregunta por qué antes de aceptar ninguna explicación.

**Punto de control:** has visto la salida real del comando y coincide.

### 6. Pide una mirada retrospectiva (3 minutos)

```text
Ahora que lo has construido, ¿qué habrías hecho de otra manera?
```

Decide para cada sugerencia: hacerla ahora (si es pequeña y cabe en el alcance), abrir una issue de seguimiento con `gh issue create` o descartarla. No dejes que la retrospectiva haga crecer el pull request.

**Punto de control:** cada sugerencia tiene una decisión.

### 7. Haz commit y abre el pull request (5 minutos)

```text
Haz commit con un mensaje que explique cómo se prueba "finished this year" y
cómo se tratan los estados desconocidos. Haz push y abre un pull request con
gh pr create que cierre la #3. En la descripción, explica las dos decisiones
y sus pros y contras.
```

**Punto de control:** `gh pr view` muestra el pull request y su descripción contiene las dos decisiones.

### 8. Si dos correcciones fallaron: empieza de nuevo (opcional, 10 minutos)

Si en algún momento corregiste al agente dos veces sobre el mismo problema y seguía mal, para y practica el reinicio:

```text
Para. Resume en 10 puntos como máximo lo que hemos aprendido: restricciones
que encontramos, enfoques que fallaron y por qué. No cambies ningún archivo.
```

Copia los puntos. Descarta el trabajo y crea un worktree limpio:

```bash
cd ~/code/shelf
git worktree remove --force ../shelf-s3
git branch -D s3-stats
git worktree add --no-track -b s3-stats ../shelf-s3 origin/main
```

Abre ahí una sesión nueva. Empiézala con los puntos, tus decisiones del paso 2 y "primero el plan, después espera". Anota el reinicio como corrección. Cuenta como un éxito.

**Punto de control:** la sesión nueva ha producido un plan aceptable con menos correcciones que la primera.

### 9. Clasifica tu registro de correcciones (5 minutos)

Para cada fila, rellena "Qué lo habría evitado":

- una línea en el archivo de instrucciones (**contexto** o **instrucción**) → [módulo 04](../04-context-is-infrastructure/README.md),
- una comprobación que el agente ejecuta por su cuenta (**verificación**) → [módulo 03](../03-close-the-loop/README.md),
- una pregunta mejor durante la conversación (**decisión**) → este módulo,
- nada: era una cuestión de criterio genuina.

**Punto de control:** cada fila tiene fase, causa y forma de evitarlo.

## Cómo saber que has terminado

- [ ] `python -m unittest` termina en `OK` en la rama `s3-stats`.
- [ ] Viste fallar los tests nuevos antes de la implementación.
- [ ] `gh pr view` muestra un pull request para S3 cuya descripción explica cómo se prueba el año y cómo se tratan los estados desconocidos.
- [ ] `git diff --stat origin/main` solo lista `shelf/commands/stats.py` y `tests/test_stats.py`, o la descripción explica por qué no.
- [ ] `corrections.md` tiene una fila por corrección, cada una con fase, causa y forma de evitarlo.

## Reflexiona

- **¿Dónde se concentraron las correcciones?** ¿Al conversar y planificar, o al construir y verificar? Cuanto antes llega una corrección, más barata sale.
- **¿Qué causa dominó?** Muchas filas de "contexto" significan que tu repositorio necesita mejores instrucciones. Muchas de "verificación", que el agente necesita mejores comprobaciones. Muchas de "decisión", que estás delegando elecciones que te corresponden.
- **¿Cuál fue tu mensaje más largo?** ¿Estaba supliendo un contexto que la sesión ya debería haber tenido?
- **¿Encontró el agente las preguntas abiertas, o las encontraste tú?** Si fuiste tú, ¿qué habría necesitado para encontrarlas por su cuenta?

## Para ir más allá

- **Dibuja el sistema.** Pide un `docs/architecture.md` con un diagrama de flujo en Mermaid de cómo llega un comando al archivo y un diagrama de secuencia de `shelf finish`, citando archivos y líneas. Encuentra algo que esté mal o poco claro y corrígelo en una frase. No edites tú el documento.
- **Conversa sin construir.** Toma S7 ("Hacer shelf más útil para clubes de lectura"). Da pocas indicaciones: "Dame tres direcciones muy distintas." Elige una, pide al agente que la escriba como una issue autocontenida al estilo de S1–S6 y para ahí.
- **Compara proveedores.** Repite S3 desde cero con un agente de otro proveedor y compara los dos registros de correcciones fila a fila.
