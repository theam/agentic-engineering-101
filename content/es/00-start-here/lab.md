---
title: "Laboratorio 0 — El juego completo"
module: 0
kind: lab
minutes: 45
level: foundation
last_reviewed: 2026-09-17
---

# Laboratorio 0 — El juego completo

## Objetivo

Sacar adelante un cambio real con agentes en unos 45 minutos y, mientras tanto, lanzar otro en paralelo. Vas a:

1. pedir a un agente que te explique un código que nunca ha visto,
2. conversar, planificar e implementar la issue S1 con tests, y abrir un pull request,
3. mientras eso avanza, empezar la issue S2 en un worktree de git aparte con una segunda sesión,
4. revisar el primer pull request desde una tercera sesión limpia, que no lo ha escrito.

Harás cada paso de forma superficial, a propósito. Aquí no se explica nada en profundidad. Cada paso termina señalando el módulo que lo explica. La idea es ver el juego completo una vez, para que el resto de la guía tenga dónde encajar.

## Antes de empezar

**Comprueba los requisitos previos** del [módulo 00](README.md#requisitos-previos):

```bash
git --version
gh auth status
python --version   # o bien: python3 --version
claude --version   # o bien: codex --version
```

En este laboratorio, usa `python3` donde ponga `python` si así se llama Python 3 en tu máquina.

**Haz tu propia copia del proyecto de prácticas.** Necesitas un repositorio que sea tuyo, para que los agentes puedan subir ramas y abrir pull requests. Desde la raíz de tu copia local de esta guía (clonada o descargada), sigue la receta del [README del proyecto de prácticas](../../../practice/shelf/README.md):

```bash
mkdir -p ~/code
cp -r practice/shelf ~/code/shelf
cd ~/code/shelf
git init -b main
git add .
git commit -m "Start from the Agentic Engineering 101 practice project"
gh repo create shelf --private --source=. --remote=origin --push
python -m unittest
```

**Punto de control:** la salida de los tests termina en `OK` (13 tests en este momento) y `gh repo view` muestra tu repositorio nuevo. Si ya tienes un repositorio llamado `shelf`, elige otro nombre.

**Crea dos issues.** Abre el [catálogo de issues de prácticas](../../../practice/issues/es.md). Ejecuta `gh issue create` dos veces y pega el título y el cuerpo de **S1** (`S1: Filtrar shelf list por estado`) y de **S2** (`S2: Buscar libros por título o autor`), sin la línea de "Seguridad en paralelo". **Punto de control:** `gh issue list` muestra las dos, como #1 y #2. El [laboratorio 5](../05-decompose-into-tracks/lab.md) crea el resto.

**En tu propio repositorio:** elige dos issues pequeñas que toquen archivos distintos, que podrías terminar a mano en menos de una hora cada una, y en un repositorio con tests que el agente pueda ejecutar. Para esta primera vez, evita código que maneje dinero, autenticación o datos de producción.

> [!TIP]
> Los tests apuntan `SHELF_PATH` y `HOME` a una carpeta temporal, así que nunca tocan tu `~/.shelf.json` real. Cuando un agente pruebe el comando a mano, pídele que haga lo mismo: que apunte antes `SHELF_PATH` a un archivo temporal.

Tiempos aproximados: 5 minutos para la explicación, 10 para conversar y arrancar S1, 10 para arrancar S2, 15 para la revisión y 5 para decidir y limpiar.

## Pasos

### 1. Pide al agente que te explique el proyecto (5 minutos)

Abre una sesión en `~/code/shelf` (`claude` o `codex`) y escribe:

```text
Lee README.md, AGENTS.md, el paquete shelf/ y los tests antes de responder.
Después explica en menos de 200 palabras: qué hace esta herramienta, cómo
viaja un comando desde la línea de comandos hasta el archivo JSON y cómo se
ejecutan los tests. Ejecuta los tests para confirmarlo. No cambies ningún archivo.
```

**Fíjate en:** los cuatro comandos (`add`, `list`, `start`, `finish`); un módulo por comando dentro de `shelf/commands/`, que se descubren automáticamente; `cli.py`, que interpreta los argumentos y convierte los errores en códigos de salida; `store.py`, que lee y escribe un único archivo JSON, `~/.shelf.json` salvo que `SHELF_PATH` indique otro; y una ejecución real de los tests que termina en `OK`. Si describe una funcionalidad que no existe, apúntalo. Los detalles inventados son un síntoma de falta de contexto.

**Punto de control:** puedes explicar en una frase cómo llega `shelf finish 3` hasta el archivo.

Se explica en: el [módulo 02](../02-one-agent-done-well/README.md) (háblale como a un compañero) y el [módulo 04](../04-context-is-infrastructure/README.md) (el contexto).

### 2. Conversa y planifica S1 antes de escribir código (5 minutos)

La issue ya fija el comportamiento: los estados válidos, el código de salida 2 con un error que los nombra y el mensaje exacto cuando no hay coincidencias. Lo que queda por hablar es cómo construirlo. En la misma sesión:

```text
Vamos a hablar de la issue #1 antes de construir nada. Léela con gh issue view 1.
Dame dos opciones para implementarla dentro de los criterios de aceptación,
con sus pros y contras, y cita los códigos de salida y mensajes exactos que
deben comprobar los tests. Recomienda una. No escribas código hasta que te
diga que construyas.
```

**Fíjate en:** las cadenas exactas de la issue (`No books with status reading.`, código de salida 2 para un estado no válido) y opciones reales. Por ejemplo: dejar que `argparse` valide el valor con una lista fija de opciones construida a partir de `STATUSES` en `shelf/models.py`, o validarlo a mano dentro del comando. Si el agente empieza a editar archivos, páralo y repite "todavía no escribas código".

Elige una opción en una sola frase, por ejemplo: "La opción A: choices de argparse a partir de STATUSES, así el error de uso sale gratis."

**Punto de control:** has acordado el enfoque con el agente en tres mensajes cortos como mucho, y no ha cambiado ningún archivo (`git status` está limpio).

Se explica en: el [módulo 02](../02-one-agent-done-well/README.md) (conversar, planificar, construir).

### 3. Construye S1 con tests y abre un pull request (arranca ahora y sigue solo)

```text
Constrúyelo. Trabaja en una rama nueva llamada s1-status-filter.
Escribe primero los tests y ejecútalos para demostrar que fallan. Después implementa.
Ejecuta toda la batería con python -m unittest y enséñame la salida.
Después haz commit, push y abre un pull request con gh pr create cuya
descripción diga "Closes #1".
```

**Fíjate en:** una ejecución que falla antes de la implementación, otra que pasa después y la URL de un pull request al final. No te quedes mirando cómo trabaja. Ve al paso 4.

Se explica en: el [módulo 03](../03-close-the-loop/README.md) (el agente comprueba su propio trabajo) y el [módulo 05](../05-decompose-into-tracks/README.md) (un pull request, de principio a fin).

### 4. Mientras S1 avanza, empieza S2 en un worktree (10 minutos)

Abre una segunda terminal. Un worktree es una segunda carpeta de trabajo sobre el mismo repositorio, con su propia rama, de modo que las dos sesiones nunca editan los mismos archivos en disco:

```bash
cd ~/code/shelf
git fetch origin
git worktree add --no-track -b s2-search ../shelf-s2 origin/main
cd ../shelf-s2
claude   # o bien: codex
```

`--no-track` evita que la rama nueva siga a `origin/main`, algo que confundiría a `git status` y a `git push`. El [módulo 06](../06-run-sessions-in-parallel/README.md#una-receta-de-worktrees-que-no-muerde) explica por qué.

> [!TIP]
> En Claude Code, `claude --worktree s2-search` crea el worktree y arranca la sesión en un solo paso, dentro de `.claude/worktrees/` ([documentación de worktrees](https://code.claude.com/docs/en/worktrees)). Si lo usas, añade `.claude/worktrees/` a `.gitignore`.

Esta sesión no sabe nada de la primera. Dale un prompt corto:

```text
Implementa la issue #2 (léela con gh issue view 2). Antes de escribir código,
dime en cinco puntos qué vas a cambiar, qué archivos vas a tocar y cómo lo
vas a probar. Espera a que te dé el visto bueno.
```

Lee los cinco puntos. La issue sugiere un `shelf/commands/search.py` nuevo y un `tests/test_search.py` nuevo, y pide que la búsqueda ignore mayúsculas y minúsculas también con letras acentuadas (`GARCÍA` debe encontrar `García`). Si los puntos cubren eso, responde:

```text
ok, constrúyelo: primero los tests, ejecuta python -m unittest y después abre un pull request que cierre la #2.
```

Cuando la primera sesión te necesite (una pregunta, una petición de permiso, un pull request terminado), cambia a ella, responde y vuelve. Ese ir y venir es la verdadera habilidad del ciclo externo.

**Punto de control:** `git worktree list` muestra dos entradas, en ramas distintas. S1 cambia `shelf/commands/list_books.py` y `tests/test_cli.py`; S2 añade archivos nuevos. No tocan los mismos archivos, y eso es lo que permite ejecutarlas en paralelo con seguridad.

Se explica en: el [módulo 05](../05-decompose-into-tracks/README.md) (pistas independientes) y el [módulo 06](../06-run-sessions-in-parallel/README.md) (worktrees y cambiar entre sesiones).

### 5. Revisa el pull request de S1 desde una sesión limpia (15 minutos)

Espera a que el paso 3 abra su pull request. Busca su número con `gh pr list`. Después abre una **tercera** sesión en un worktree de ese pull request, para que quien revisa no comparta ni la memoria ni la carpeta de quien lo escribió:

```bash
cd ~/code/shelf
git fetch origin
git worktree add --detach ../shelf-review origin/s1-status-filter
cd ../shelf-review
claude   # o bien: codex
```

(En Claude Code, `claude --worktree "#<número>"` hace lo mismo a partir del número del pull request.)

```text
Vas a revisar un pull request que no has escrito tú. Ejecuta gh pr view <número>
y gh pr diff <número>, y lee la issue que cierra. Comprueba, en este orden:
1. ¿Cumple todos los criterios de aceptación, con los mensajes y códigos de
   salida exactos? ¿Hace algo que la issue no pide?
2. ¿Fallarían los tests nuevos si se revirtiera el cambio? Léelos y después
   ejecuta python -m unittest.
3. Casos límite: un estado no válido, ningún libro que coincida, una
   estantería vacía y shelf list sin --status.
Informa solo de problemas que afecten a la corrección o a los requisitos de
la issue, del más grave al menos grave, cada uno con archivo y línea. Si no
encuentras ninguno, dilo y enseña la salida de los tests. No cambies ningún archivo.
```

**Fíjate en:** hallazgos con archivo y línea, o un "no hay problemas de corrección" claro y respaldado por una ejecución de los tests. Una revisión que solo elogia el código, o que solo enumera preferencias de estilo, no es una revisión.

Para cada hallazgo, decide una de tres cosas: **arreglar ahora** (pégalo en la primera sesión: "Aquí tienes el resultado de la revisión: … Arregla lo que sea un problema real de corrección, haz push y dime qué has cambiado"), **abrir una issue** para más adelante o **descartarlo** con un motivo de una línea.

> [!TIP]
> Codex tiene un comando `/review` integrado que puede revisar frente a una rama base, cambios sin commit o un commit concreto ([buenas prácticas de Codex](https://learn.chatgpt.com/guides/best-practices)). Si tienes las dos herramientas, prueba a revisar con la que no escribió el código.

**Punto de control:** cada hallazgo tiene una decisión escrita al lado.

Se explica en: el [módulo 07](../07-agents-review-agents/README.md) (agentes que revisan a agentes, triaje por decisión).

### 6. Decide, haz merge y limpia (5 minutos)

Si el pull request de S1 está bien, haz tú el merge en GitHub. Un agente puede prepararlo todo, pero el merge es decisión tuya. Deja S2 en marcha o terminada; puedes hacer su merge ahora o más tarde.

Elimina el worktree de revisión. No tiene cambios, así que es seguro:

```bash
cd ~/code/shelf
git worktree remove ../shelf-review
git worktree list
```

Conserva `../shelf-s2` hasta que se haga el merge de su pull request, y después elimínalo del mismo modo.

Se explica en: el [módulo 06](../06-run-sessions-in-parallel/README.md) (higiene de sesiones) y el [módulo 09](../09-teams-and-organizations/README.md) (las personas en los puntos de control).

## Cómo saber que has terminado

- [ ] `gh pr list --state all` muestra un pull request para S1, con los tests pasando en la sesión o en el pull request.
- [ ] S2 tiene un pull request, o `git worktree list` sigue mostrando `shelf-s2` con trabajo en curso.
- [ ] Tienes los hallazgos de la revisión limpia y cada uno tiene una decisión: arreglar ahora, issue o descartar.
- [ ] `git worktree list` ya no muestra `shelf-review`.
- [ ] Para cada uno de los seis pasos, sabes qué módulo lo explica.

## Reflexiona

Escribe tres líneas en un archivo de notas. Las usarás en el [laboratorio 1](../01-from-chatbot-to-system/lab.md).

- **¿Dónde esperaste?** Cuenta los momentos en que miraste trabajar a un agente en lugar de hacer otra cosa.
- **¿Qué comprobaste tú que podría haber comprobado el agente?** Cada una de esas comprobaciones es trabajo para el [módulo 03](../03-close-the-loop/README.md).
- **¿Encontró la revisión limpia algo que se le escapó a quien escribió el código?** Si lo encontró, pregúntate por qué se le escapó. Si no, ¿fue una revisión demasiado blanda o el cambio estaba realmente bien?
- **¿Cuándo perdiste la pista** de qué hacía cada sesión? Esa sensación es el cuello de botella al que esta guía vuelve una y otra vez: tu atención.

## Para ir más allá

- Pregunta a la sesión de S1: "Ahora que lo has construido, ¿qué habrías hecho de otra manera?" Decide si la respuesta merece una issue de seguimiento.
- Haz el merge de S2 después del de S1. Añaden y cambian archivos distintos, así que no deberías tener conflictos. Si aparece alguno, pide a la sesión de S2 que haga merge de `origin/main` en su rama, se adapte, vuelva a ejecutar los tests y haga push (sin necesidad de force-push), y pregúntale por qué se solaparon los archivos.
- Repite el paso 5 con un agente de otro proveedor y compara lo que encuentra cada revisión.
