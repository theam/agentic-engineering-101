---
title: "Laboratorio 5 — De un backlog a pistas en paralelo"
module: 5
kind: lab
minutes: 60
level: intermediate
last_reviewed: 2026-09-17
---

# Laboratorio 5 — De un backlog a pistas en paralelo

## Objetivo

Haz que un agente convierta el catálogo de issues de práctica en issues de GitHub, encuentre por sí solo los solapamientos entre ellas (incluido el único conflicto que necesita una decisión humana), aplique la decisión que ya registraste para ese conflicto en el [laboratorio 4](../04-context-is-infrastructure/lab.md), las agrupe en pistas de trabajo (tracks) y escriba prompts de arranque para tres pistas que ejecutarás a la vez en el [laboratorio 6](../06-run-sessions-in-parallel/lab.md).

Practicas las habilidades del [módulo 05](README.md): issues como prompts, dimensionar por radio de impacto, planificar un orden de merge y escribir prompts de arranque que resuelvan las decisiones antes de que arranque una sesión.

## Antes de empezar

- **Tu copia del proyecto de práctica en GitHub.** Si hiciste el [laboratorio 0](../00-start-here/lab.md), ya la tienes. Si no, sigue la sección «Use it for the labs» del [README del proyecto de práctica](../../../practice/shelf/README.md) (usa `~/code/shelf`). En este laboratorio la llamamos «tu repositorio».
- **GitHub CLI con sesión iniciada:** `gh auth status`.
- **Un `main` limpio y al día:** `git fetch origin && git status` en tu repositorio dice que estás en `main`, al día y sin nada pendiente de commit.
- **Recomendado:** el [laboratorio 4](../04-context-is-infrastructure/lab.md), para que tu repositorio tenga un AGENTS.md, un `kb/ACTIVE.md` y el registro de la decisión sobre C1 y C2, `kb/decisions/D-0001-storage-change-order.md`. El laboratorio funciona sin ellos: sáltate las partes de `ACTIVE.md` y toma la decisión en el paso 3.
- **Trabajo previo:** conserva las issues que ya abriste para S1, la S2 opcional, S3 o S6. El paso 1 reutiliza las existentes, incluidas las cerradas.

**En tu propio repositorio:** reúne entre 6 y 12 trabajos próximos (elementos del backlog, notas de la hoja de ruta, una lista salida de una reunión) en un archivo que el agente pueda leer. Incluye al menos una pareja que sospeches que va a chocar. Donde este laboratorio usa `gh`, usa la CLI de tu gestor de issues, o pide al agente borradores que pegues tú.

## Pasos

### 1. Crea las issues a partir del catálogo (10 minutos)

Abre tu agente en la carpeta de Shelf. En Academy, pulsa **Copy task for my agent** y pega la tarea en la sesión. Incluye los nueve enunciados. Si lees en GitHub, pega el prompt y después el catálogo enlazado en el mismo mensaje.

```text
Usa las nueve issues de Shelf que figuran a continuación. Ejecuta gh repo view y muéstrame el propietario y el repositorio. Espera mi confirmación antes de crear o modificar issues.

Cuando confirme, lista las issues abiertas y cerradas. Busca cada ID del catálogo entre las issues existentes, incluidas las cerradas. Crea solo las que falten con gh issue create. Usa el título exacto y las secciones Problema, Criterios de aceptación, Archivos que probablemente cambian y Fuera de alcance. Escribe cada cuerpo en un archivo temporal y usa --body-file para conservar el Markdown. Deja vacíos los campos de etiquetas, responsables e hitos.

Si completé el laboratorio 3, pídeme la URL del pull request de S6. Cuando te la dé, enlázalo en un comentario y cierra S6 si sigue abierta. Si me salté el laboratorio 3, deja S6 como está.

Muéstrame una tabla con los nueve IDs, los números de issue, los títulos y los estados. Para ahí para que pueda comprobar el resultado.
```

[Nueve enunciados de Shelf](../../../practice/issues/es.md "copy-task")

**Fíjate en:** el agente se detiene después de `gh repo view` y espera a tu OK. Si tu configuración pide permiso para cada `gh issue create`, es la barrera de seguridad (guardrail) del [módulo 03](../03-close-the-loop/README.md) haciendo su trabajo: crear issues es una acción hacia fuera, y la puerta eres tú.

**Punto de control:** `gh issue list --state all --limit 30` muestra exactamente una issue para cada una de S1–S7, C1 y C2,. Decidir qué puede ir en paralelo es tu trabajo en el paso 2.

### 2. Encuentra los solapamientos antes de planificar (10 minutos)

En la misma sesión:

```text
Lee AGENTS.md, el paquete shelf/ y los tests, y después lee cada issue abierta
con gh issue view. No crees ni cambies nada. Dime:
1. Para cada issue: los archivos que probablemente tocará, los contratos
   compartidos que cambia (formatos de datos, funciones públicas, salida de
   comandos) y un tamaño (S, M o L).
2. Cada pareja de issues que se solapa. Di si cada solapamiento es textual
   (mismas líneas, git se detendrá) o semántico (mismo contrato, git puede
   integrarlo y el resultado seguir estando mal), y por qué.
3. Cualquier issue que no esté lista para implementarse tal como está escrita.
```

**Punto de control:** guarda los solapamientos que propone el agente y las pruebas que aporta. Comprueba una afirmación en el código. Si falta un contrato compartido, pregunta qué issues cambian el formato del archivo guardado y apunta si cambia la respuesta. `git status` debería seguir limpio.

### 3. Aplica la decisión que ya tomaste (5 minutos)

C1 y C2 pueden hacer merge en cualquier orden, con consecuencias distintas:

- **Primero C1:** se adapta C2, y la versión 2 del archivo incluye `tags`. Una sola versión, menos código.
- **Primero C2:** se adapta C1, que sube el archivo a la versión 3 y añade una migración desde la versión 2. Más código, pero es lo que hace un proyecto real cuando la versión 2 ya está publicada.

Solo una persona puede elegir, y ya lo hiciste: el laboratorio 4 registró la elección como `D-0001`. No decidas dos veces. Indica al agente dónde está el registro:

```text
Nuestra decisión sobre C1 y C2 está en kb/decisions/D-0001-storage-change-order.md.
Añade una sección «Coordinación» a los cuerpos de C1 y C2: el conflicto
semántico, el orden de merge, la decisión con su fecha y un enlace a D-0001, y
lo que tiene que hacer la segunda para adaptarse. Si S1 o S6 sigue abierta,
añade su solapamiento textual con C1 a las dos issues (hace merge antes que
C1). Usa gh issue edit con --body-file, después vuelve a leer cada issue con
gh issue view y confirma que el cambio se guardó.
```

Si te saltaste el laboratorio 4, elige ahora un orden y sustituye la primera frase del prompt por `Decisión: <primero C1 | primero C2>, porque <una frase>. Antes, regístrala con la fecha de hoy en kb/decisions/D-0001-storage-change-order.md.`

**Fíjate en:** la relectura. Las herramientas a veces fallan en silencio, y una escritura no está terminada hasta que la has vuelto a leer.

**Punto de control:** `gh issue view` sobre C1 y sobre C2 muestra una sección de Coordinación que nombra la otra issue por su número, con la decisión de `D-0001` y su fecha.

### 4. Agrupa en pistas y planifica los merges (10 minutos)

```text
Agrupa las issues abiertas en pistas. Una pista es trabajo que una sesión
puede hacer en un worktree sin editar archivos que sean de otra pista.
Reglas: una issue, un PR (no dividas issues en fases); las issues que no
están listas no son pistas; usa el orden de merge de D-0001. Para
cada pista da: sus issues, los archivos que son suyos, sus restricciones de
merge y una prioridad calculada como
(valor de negocio + urgencia + reducción de riesgo) / esfuerzo,
con una frase que justifique cada puntuación.
Escríbelo en kb/tracks.md con un diagrama de flujo mermaid pequeño en el que
una flecha signifique «hace merge antes que». Si existe kb/ACTIVE.md, añade
una fila por pista.
```

**Fíjate en:** C1 y C2 en pistas separadas (o juntas, con un buen motivo), S7 fuera, cualquier issue abierta que se solape con C1 (S1, S6) haciendo merge antes que ella, una nota sobre el seguimiento «la exportación incluye las etiquetas» y puntuaciones de prioridad que defenderías. Corrige en una frase cualquier puntuación con la que no estés de acuerdo.

**Punto de control:** existe `kb/tracks.md` y recoge el orden entre C1 y C2 de `D-0001`. Si tienes un `ACTIVE.md`, `wc -l kb/ACTIVE.md` sigue por debajo de 100 líneas.

### 5. Escribe prompts de arranque para tres pistas (15 minutos)

El laboratorio 6 ejecuta estas tres pistas a la vez:

- **Pista A:** S4 y S5, issues independientes que añaden archivos (más el método `remove` de S5 en `shelf/store.py`).
- **Pista B:** C1.
- **Pista C:** C2.

Si te saltaste laboratorios anteriores y S1, S2, S3 o S6 siguen abiertas, añádelas a la pista A, que hace merge primero. S2 y S3 solo añaden archivos, y S1 y S6 tienen que hacer merge antes que C1 de todos modos. Si alguna ya tiene un pull request abierto de su laboratorio, haz merge de ese pull request en lugar de empezar la issue otra vez.

```text
Escribe prompts de arranque para tres pistas que se ejecutarán a la vez:
A (<issues>), B (C1, #<número>) y C (C2, #<número>).
Cada prompt necesita estas secciones: objetivo; lo que ya he comprobado
(hechos con archivo:línea de tu análisis, para que la sesión no los vuelva a
deducir); haz esto primero: demuestra la premisa; decisiones ya tomadas, no
las reabras; alcance e «informa, no arregles»; reglas del repositorio que
romperán el build; notas del entorno; coordinación con las otras dos pistas;
si te ves tomando decisiones de diseño, para e informa; terminado cuando;
informe final.
La pista A hace sus issues una detrás de otra, con una rama y un PR para cada
una. Worktrees: ../shelf-a, ../shelf-c1 y ../shelf-c2. Ramas: una por issue,
con su nombre (por ejemplo s4-export, c1-tags, c2-file-version).
Cada sesión usa su propio SHELF_PATH. Guarda los prompts como
kb/kickoffs/a.md, kb/kickoffs/c1.md y kb/kickoffs/c2.md.
```

(Si tienes abierta [la plantilla del prompt de arranque](README.md#el-prompt-de-arranque), pégala después del prompt.)

**Fíjate en:**

- `D-0001` aparece en «decisiones ya tomadas» en B y en C.
- En el prompt de la pista que hace merge en segundo lugar: «cuando te avise de que la otra ha hecho merge, haz merge de `origin/main` y adáptate», explicando qué significa adaptarse.
- En la pista A: puede hacer merge en cualquier momento y no debe tocar `models.py` ni `store.py` (salvo S5, por su método `remove`).
- Cada «terminado cuando» incluye `python -m unittest`.

**Punto de control:** `ls kb/kickoffs/` muestra los tres archivos.

### 6. Prueba un prompt en frío (5 minutos)

Abre una sesión **nueva**, sin memoria de esta. Pega el contenido del prompt de arranque de la pista que hace merge en *segundo* lugar (C1 o C2) y después:

```text
Antes de hacer nada (no cambies archivos ni crees ningún worktree), responde
en puntos: qué harás primero, qué decisiones están ya tomadas, qué queda fuera
de alcance, qué harás cuando la otra pista haga merge y cómo sabrás que has
terminado. Después lista cada pregunta que necesitarías que te respondieran
antes de empezar.
```

**Fíjate en:** respuestas que salen directamente del prompt. Cada pregunta de su lista es un hueco en tu prompt, no un defecto del agente. Corrige el archivo para cada hueco real y después cierra esta sesión.

**Punto de control:** la lista de preguntas está vacía, o cada pregunta ya tiene respuesta en el archivo.

### 7. Haz commit del plan (5 minutos)

Ejecuta tú estos comandos:

```bash
git add kb/
git commit -m "Plan tracks and kickoff prompts for lab 6"
git push
```

**Punto de control:** `git status` está limpio y `git log -1 --stat` lista los archivos de `kb/`.

## Cómo saber que has terminado

- [ ] `gh issue list --state all --limit 30` muestra una issue por cada entrada del catálogo (S1–S7, C1, C2), sin duplicados.
- [ ] `gh issue view` sobre C1 y sobre C2 muestra una sección de Coordinación que nombra la otra issue, el orden de merge y la decisión con fecha de `D-0001`.
- [ ] S7 no tiene plan de implementación.
- [ ] `kb/tracks.md` lista las pistas, los archivos de cada una, las prioridades justificadas y un diagrama mermaid.
- [ ] `ls kb/kickoffs/` muestra `a.md`, `c1.md` y `c2.md`, y el prompt de la pista que hace merge en segundo lugar ha superado la prueba en frío.
- [ ] `git status` está limpio y el commit está subido.

## Reflexiona

- ¿Encontró el agente el conflicto entre C1 y C2 sin ayuda? ¿Lo llamó semántico o solo vio el archivo de test compartido? ¿Qué podría haberlo hecho más evidente en el código?
- ¿Qué decisiones has tomado hoy en una sola frase? ¿Dónde están escritas ahora, y las encontrará sin ti una sesión del laboratorio 6?
- ¿Cuánto tiempo has pasado leyendo cuerpos de issues y cuánto revisando el plan que explicaba el agente? ¿Qué te saltarías la próxima vez?
- Mira un prompt de arranque. ¿Qué sección quitarías para un arreglo de una línea, y cuál no quitarías nunca?

[Comparar mi plan con la solución](../../../practice/issues/es-solution.md). ¿Qué diferencias cambiarían tu orden de merge?

## Para ir más allá

- **Conversa sobre S7.** Sigue sus criterios de aceptación: pide al agente las preguntas que necesitan respuesta y dos o tres opciones, cada una con los comandos que añade, los archivos que toca y si cambia el formato del archivo. Elige una, registra la decisión en `kb/decisions/` y crea issues solo para la primera rebanada.
- **Escribe un paquete de traspaso** para esta sesión de planificación, como si te fueras una semana. Usa [la plantilla del paquete de traspaso](README.md#paquetes-de-traspaso). Mañana, abre una sesión nueva, pega solo el prompt de reanudación y comprueba si continúa bien.
