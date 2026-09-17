---
title: "Laboratorio 4 — Dale memoria al proyecto"
module: 4
kind: lab
minutes: 45
level: intermediate
last_reviewed: 2026-09-17
---

# Laboratorio 4 — Dale memoria al proyecto

## Objetivo

Construir la capa de contexto del proyecto de prácticas y medir qué cambia. Vas a:

1. hacerle tres preguntas sobre el proyecto a una sesión nueva y guardar sus respuestas,
2. escribir un contrato `AGENTS.md` y un `CLAUDE.md` que lo importe,
3. crear `kb/ACTIVE.md` y un registro de decisión, y hacer commit de todo,
4. hacerle las mismas tres preguntas a otra sesión nueva y comparar,
5. plantar un dato falso en la base de conocimiento (knowledge base) y comprobar que el agente confía más en el código que en la foto fija.

## Antes de empezar

- Tu propia copia del proyecto de prácticas, preparada como en el [laboratorio 0](../00-start-here/lab.md), con `main` limpio. Los pasos suponen que está en `~/code/shelf`; usa tu ruta si es otra. La puerta de Stop del [laboratorio 3](../03-close-the-loop/lab.md) es útil, pero no imprescindible.
- Claude Code o Codex, y la CLI de GitHub con la sesión iniciada.
- Un archivo de notas **fuera** del repositorio, por ejemplo `~/notes/lab-4.md`.
- Unos 45 minutos.

**En tu propio repositorio:** usa las pistas de trabajo (tracks) que tengas de verdad en marcha (de dos a cinco), y elige una decisión que alguien, persona o agente, ya haya intentado reabrir. Esa decisión es el registro más valioso que puedes escribir hoy.

## Pasos

### 1. Haz las preguntas antes de que haya contexto (5 minutos)

```bash
cd ~/code/shelf
git switch main && git pull
git switch -c lab-4-context
```

Abre una sesión nueva y pega:

```text
Responde con lo que encuentres en este repositorio y en GitHub, e indica de dónde
sale cada respuesta:
1. ¿En qué estamos trabajando ahora mismo, y por qué?
2. Las issues C1 (etiquetas) y C2 (versionar el formato del archivo) cambian las
   dos cómo se guardan los libros. ¿Cuál va primero, y qué tiene que hacer
   después la otra?
3. ¿Qué tiene que cumplirse antes de que des por terminado un cambio en este proyecto?
No cambies ningún archivo.
```

Copia las tres respuestas en tus notas bajo **Antes** y cierra la sesión.

**Fíjate en:** respuestas construidas a base de suposiciones. El agente puede encontrar issues abiertas con `gh issue list`, pero no puede conocer tus prioridades, tu decisión sobre C1 y C2 ni tu definición de terminado. Apunta cada respuesta que suene segura pero no tenga fuente.

**Punto de control:** tus notas tienen tres respuestas bajo "Antes" y `git status` está limpio.

### 2. Escribe lo que solo sabes tú (5 minutos, sin agente)

En tus notas, escribe cinco puntos breves:

- **Objetivo:** hacia dónde va ahora el proyecto. Por ejemplo: "preparar shelf para clubes de lectura (S7), empezando por las etiquetas".
- **Pistas:** el trabajo en marcha y su siguiente puerta. Usa tu estado real de los laboratorios anteriores (pull requests abiertos, los que tienen merge, issues que creaste).
- **Decisión:** C1 o C2 primero. Las dos cambian los campos guardados que `tests/test_store.py` fija con exactitud, así que chocan. Elige una:
  - *C1 primero:* las etiquetas llegan antes, y la versión 2 del formato de C2 incluye las etiquetas desde el primer día.
  - *C2 primero:* el archivo tiene versión antes de que cambie nada más, y C1 se convierte en la versión 3 con su propia migración.
- **Por qué:** una frase que justifique tu elección.
- **Terminado significa:** por ejemplo, "`python3 -m unittest` pasa, la puerta de Stop pasa y cada comportamiento nuevo tiene un test que falla si se revierte el cambio".

**Punto de control:** cinco puntos, incluida una decisión con su razón. Registras esta decisión como `D-0001` en el paso 5. El [laboratorio 5](../05-decompose-into-tracks/lab.md) reutiliza ese registro cuando planifica el orden de merge, y el [laboratorio 6](../06-run-sessions-in-parallel/lab.md) lo aplica, así que decides una sola vez.

### 3. Escribe el contrato con el agente (10 minutos)

El proyecto de prácticas trae un `AGENTS.md` mínimo a propósito. Abre una sesión y pega esto, con tus puntos al final:

```text
Sustituye AGENTS.md por un contrato breve para los agentes que trabajen en shelf,
de menos de 60 líneas. Lee antes README.md, el paquete shelf/ y los tests.
Incluye solo lo que no se puede deducir del código:
- primero, un puntero a kb/ACTIVE.md (léelo antes que nada) y a kb/decisions/,
- un mapa de dónde está cada cosa, una línea por entrada,
- los comandos para ejecutar la herramienta y los tests,
- las reglas que debe seguir un cambio (solo biblioteca estándar; los comandos
  nuevos van en shelf/commands/; los tests usan un SHELF_PATH temporal),
- qué significa "terminado".
Deja fuera las descripciones archivo por archivo y todo lo que ya imponen los tests.
Escribe el archivo en inglés.
Después crea CLAUDE.md con una sola línea: @AGENTS.md.
Mis notas:
<pega tus cinco puntos>
```

**Fíjate en:** comandos que existan de verdad (ejecútalos), nada de herramientas inventadas (un comando de linter que el proyecto no tiene, un objetivo de `make`) y una sección de "terminado" que coincida con tus notas. Si algo está mal, corrígelo con una frase ("no hay linter; quita esa línea") en lugar de editar tú el archivo.

**Punto de control:**

```bash
wc -l AGENTS.md          # menos de 60
head -1 CLAUDE.md        # @AGENTS.md
python3 -m unittest      # sigue en OK
```

**Codex:** Codex lee `AGENTS.md` directamente. Conserva `CLAUDE.md` de todos modos, para que los compañeros que usan Claude Code reciban el mismo contrato.

### 4. Crea el índice ACTIVE (5 minutos)

En la misma sesión:

```text
Crea kb/ACTIVE.md como índice del trabajo en marcha, en inglés y con menos de
40 líneas, con estas secciones: Current objective, Next step, Active tracks,
Blockers, Links. Active tracks es una tabla con las columnas
Track | Issue | PR | State | Next gate, una fila por pista. Usa mis notas y el
estado real en GitHub (gh issue list, gh pr list). Nada de historia, ni recuentos
de CI, ni hashes de commit.
```

**Fíjate en:** filas que indiquen un estado y una puerta, no una historia. Si una fila parece un diario ("empezado, luego arreglado, luego…"), pide: "Reescribe esa fila como un estado y una siguiente puerta".

**Punto de control:** `wc -l < kb/ACTIVE.md` muestra un número menor que 40, y cada número de issue y de pull request de la tabla existe (`gh issue view <n>`, `gh pr view <n>`).

### 5. Registra la decisión (5 minutos)

```text
Registra nuestra decisión sobre C1 y C2 en
kb/decisions/D-0001-storage-change-order.md, en inglés, con front matter
(id, title, status: accepted, decided_on) y las secciones Context, Options
considered, Decision y Consequences. En Context, cita la evidencia del código:
tests/test_store.py fija exactamente los campos guardados, así que las dos issues
tienen que cambiarlo. Enlaza el registro desde la fila de ACTIVE a la que afecta.
```

**Punto de control:**

```bash
grep -n "status: accepted" kb/decisions/D-0001-*.md
grep -n "D-0001" kb/ACTIVE.md
```

### 6. Haz commit de la base de conocimiento (2 minutos)

Un cambio en la base de conocimiento sin commit no ha ocurrido. Haz commit antes de ponerlo a prueba:

```bash
git add AGENTS.md CLAUDE.md kb
git commit -m "Add the agent contract and a knowledge base"
git status --short       # no muestra nada
```

Cierra la sesión.

### 7. Haz las mismas preguntas en una sesión nueva (5 minutos)

Abre una sesión **nueva** y pega exactamente el prompt del paso 1. Copia las respuestas en tus notas bajo **Después**.

**Fíjate en:**

- La respuesta 1 nombra tu objetivo y cita `kb/ACTIVE.md`.
- La respuesta 2 da *tu* decisión y su razón, y cita `D-0001`, en lugar de un razonamiento genérico.
- La respuesta 3 coincide con tu definición de terminado.
- Llegó antes y leyendo menos archivos. Si la sesión muestra el uso de contexto o de tokens, compáralo con el del paso 1.

**Punto de control:** bajo "Después", escribe una frase sobre lo que cambió y otra sobre lo que todavía falta.

### 8. Planta un dato falso (5 minutos)

Una base de conocimiento es una foto fija. Comprueba que el agente la trata como tal. Añade esta fila a la tabla de pistas de `kb/ACTIVE.md`, y **no hagas commit**:

```markdown
| CSV export | S4 | — | Merged | — |
```

Abre una sesión nueva y pregunta:

```text
¿Puedo exportar hoy mi shelf a CSV? Enséñame el comando exacto.
```

**Fíjate en:** una buena respuesta mira el código o `python3 -m shelf --help`, no encuentra ningún comando `export` y te dice que la base de conocimiento no coincide con el código. Una respuesta débil se inventa un comando porque `ACTIVE.md` dice que ya se entregó.

Si la respuesta es débil, añade esta regla a `AGENTS.md`, abre otra sesión y vuelve a preguntar:

```markdown
- The knowledge base is a snapshot. When it disagrees with the code, `--help`
  or GitHub, trust those and tell me about the disagreement.
```

Después quita la fila falsa:

```bash
git restore kb/ACTIVE.md
```

Si añadiste la regla, haz commit: `git commit -am "AGENTS.md: live systems win over the knowledge base"`.

**Punto de control:** una sesión señaló la discrepancia, con o sin la regla nueva, y `git status --short` no muestra nada.

Haz push de la rama y abre un pull request con `gh pr create --fill`. Haz merge cuando te convenza, para que todas las sesiones siguientes empiecen con este contexto.

## Cómo saber que has terminado

- [ ] `head -1 CLAUDE.md` muestra `@AGENTS.md`, y `wc -l < AGENTS.md` muestra un número menor que 60.
- [ ] `kb/ACTIVE.md` tiene menos de 100 líneas y una tabla con las columnas Track, Issue, PR, State y Next gate.
- [ ] `ls kb/decisions/` muestra un registro, y ese registro contiene `status: accepted`.
- [ ] `git status --short` no muestra nada, y `gh pr list` muestra tu pull request (o ya tiene merge).
- [ ] Tus notas tienen respuestas "Antes" y "Después" a las mismas tres preguntas.
- [ ] Una sesión nueva señaló como incorrecta la fila plantada de `CSV export`.

## Reflexiona

- ¿Qué respuesta mejoró más entre "Antes" y "Después"? ¿Cuál no mejoró, y qué contexto faltaba?
- Lee tu `AGENTS.md` línea a línea y pregúntate en cada una: "¿Quitar esto haría que el agente cometiera errores?". ¿Qué líneas borrarías?
- ¿Qué corregiste en más de una sesión durante los laboratorios 0 a 3? ¿Es una entrada de memoria, una regla de `AGENTS.md` o una guarda?
- El paso 8 es la razón por la que ganan los sistemas vivos. ¿Dónde afirma todavía un documento de tu repositorio algo que el código ya no hace?

## Para ir más allá

- **Carga ACTIVE de forma determinista.** Añade un hook `SessionStart` que imprima `kb/ACTIVE.md`, para que esté en el contexto incluso después de compactar. En Claude Code, `.claude/settings.json` queda entonces con los dos hooks de los laboratorios 3 y 4:

  ```json
  {
    "hooks": {
      "SessionStart": [
        {
          "matcher": "startup|resume|clear|compact",
          "hooks": [{ "type": "command", "command": "cat \"${CLAUDE_PROJECT_DIR}/kb/ACTIVE.md\"" }]
        }
      ],
      "Stop": [
        {
          "hooks": [{ "type": "command", "command": "python3 \"${CLAUDE_PROJECT_DIR}/scripts/stop_gate.py\"", "timeout": 120 }]
        }
      ]
    }
  }
  ```

  En Codex, añade la misma entrada `SessionStart` a `.codex/hooks.json`, con `cat "$(git rev-parse --show-toplevel)/kb/ACTIVE.md"` como comando, y apruébala con `/hooks`.
- **Sustituye una decisión.** La estrategia cambió: al final los clubes de lectura necesitan el orden contrario. Pide al agente que registre una `D-0002` que invierta `D-0001`, que marque `D-0001` como sustituida con `superseded_on`, `superseded_by` y un aviso bajo su título, y que actualice la fila de ACTIVE. Comprueba que no se borró nada: `git diff --stat` muestra `D-0001` modificado, no eliminado.
- **Escribe una entrada de memoria.** Toma una corrección que le hiciste a un agente en los laboratorios 0 a 3 y pídele que la guarde como `kb/memory/<slug>.md` con **Rule**, **Why** y **How to apply**, más una línea en `kb/memory/README.md`. Haz commit de las dos.
- **Protege el presupuesto.** Amplía la puerta de Stop del laboratorio 3 para que también falle cuando `kb/ACTIVE.md` tenga más de 100 líneas, con un mensaje que le diga al agente qué quitar.
- **En tu propio repositorio:** repite los pasos 1 y 7 con tus pistas reales y la decisión que más veces se ha intentado reabrir. Comparte las respuestas de antes y después con un compañero.
