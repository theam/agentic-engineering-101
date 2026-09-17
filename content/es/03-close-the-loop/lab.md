---
title: "Laboratorio 3 — Dale al agente una forma de comprobar su trabajo"
module: 3
kind: lab
minutes: 45
level: foundation
last_reviewed: 2026-09-17
---

# Laboratorio 3 — Dale al agente una forma de comprobar su trabajo

## Objetivo

Añadir una barrera de seguridad (guardrail) determinista al proyecto de prácticas: un hook de Stop que no deja que el agente termine su turno mientras fallen los tests. Después, darle una tarea a un agente, pedirle que *no* ejecute los tests, y ver cómo el hook detecta su error y lo manda de vuelta a arreglar el código.

Vas a practicar cuatro ideas del [módulo 3](README.md): una especificación ejecutable (tests escritos primero), un hook que bloquea con el código de salida 2, probar una guarda antes de fiarte de ella, y demostrar que los tests fallan cuando se revierte el cambio.

## Antes de empezar

- Tu propia copia del proyecto de prácticas, preparada como en el [laboratorio 0](../00-start-here/lab.md), con `main` limpio y los tests pasando. Los pasos suponen que está en `~/code/shelf`; usa tu ruta si es otra.
- Python 3.10 o posterior. El script del hook solo usa la biblioteca estándar.
- Claude Code o Codex. Los pasos muestran primero Claude Code y marcan las diferencias de Codex.
- Unos 45 minutos.

**En tu propio repositorio:** elige un cambio de comportamiento pequeño que puedas describir en dos frases y un comando de tests que tarde menos de un minuto. El script del hook de abajo ejecuta `python3 -m unittest`; cambia esa línea por tu comando rápido (`npm test`, `pytest -q`, `go test ./...`). Si tu batería completa es lenta, pon la puerta sobre un subconjunto rápido y deja el resto para la CI.

> [!TIP]
> Los pasos fijan en los tests los mensajes de error exactos, siguiendo los criterios de aceptación de S6 del [catálogo de issues](../../../practice/issues/es.md): el pull request de este laboratorio cierra S6, así que tiene que cumplirlos. Fijar la redacción es a propósito: al agente que implemente la funcionalidad no le vas a decir la redacción, así que probablemente falle en el primer intento y podrás ver al hook hacer su trabajo.

## Pasos

### 1. Anota el punto de partida (2 minutos)

```bash
cd ~/code/shelf
git switch main && git pull
git switch -c lab-3-gate
python3 -m unittest
```

**Punto de control:** las últimas líneas dicen `Ran N tests` y `OK`. Apunta N. En una copia recién hecha son 13; más si hiciste merge de pull requests en laboratorios anteriores.

### 2. Escribe la especificación como tests que fallan (10 minutos)

La issue S6 ("Rechazar títulos vacíos y estados desconocidos") pide que `shelf add` rechace entradas incorrectas. Hoy `--status` acepta cualquier texto. Abre una sesión en tu copia y escribe:

```text
Vamos a implementar la issue S6: `shelf add` tiene que rechazar un título vacío
o formado solo por espacios y un --status desconocido. Todavía no implementes
nada. Escribe solo tests que fallen en tests/test_cli.py, dentro de la clase
AddCommandTest, usando el helper ShelfTestCase que ya existe. Para cada entrada
incorrecta, los tests tienen que esperar código de salida 2, un stderr que
contenga la línea de uso (usage: shelf add) y termine exactamente con una de
estas líneas, y que después no exista el archivo de la estantería:
  shelf add: error: title must not be empty
  shelf add: error: unknown status 'finished' (use to-read, reading or done)
Ejecuta python3 -m unittest y enséñame que solo fallan los tests nuevos, y por qué.
Después, para.
```

**Fíjate en:** que los tests nuevos fallen *por la razón correcta*: hoy el comando acepta la entrada y sale con 0, así que no coincide el código de salida o el mensaje. Un test que falla por una errata, un error de importación o un helper mal escrito es un test roto, no un test en rojo. Si ves eso, pide al agente que arregle el test y lo vuelva a ejecutar.

Haz commit de los tests en rojo en tu rama y después **cierra la sesión**:

```bash
git add tests
git commit -m "S6: failing tests for input validation"
```

**Punto de control:** `python3 -m unittest` termina en `FAILED`, entre los fallos solo aparecen los tests nuevos y `git status` está limpio.

> [!IMPORTANT]
> Cierra esa sesión antes del paso 3. Claude Code recarga la configuración de hooks mientras una sesión está abierta. Una sesión abierta con los tests en rojo quedaría bloqueada por la nueva puerta la próxima vez que intentara parar.

### 3. Instala la puerta a mano (5 minutos)

Crea tú los dos archivos de abajo, copiando y pegando.

> [!TIP]
> ¿Por qué a mano? Los tests están en rojo a propósito, y la puerta se ejecuta al final de cada turno del agente. Un agente que creara la puerta quedaría bloqueado por ella al final de ese mismo turno y se pondría a implementar S6. Una guarda y un estado en rojo deliberado no se llevan bien, y por eso, cuando ya existe una puerta, el rojo y el verde de TDD deberían ocurrir dentro del mismo turno del agente.

`scripts/stop_gate.py`:

```python
#!/usr/bin/env python3
"""Stop hook: the agent can't finish its turn while the test suite fails.

Works as a Claude Code or Codex Stop hook. Standard library only.
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

MAX_BLOCKS = 3   # consecutive blocks before we let the agent stop and warn you
TAIL_LINES = 40  # lines of test output sent back to the agent

event = json.load(sys.stdin)

# Test the project the agent is working in. `cwd` follows it into worktrees.
here = Path(event.get("cwd") or ".").resolve()
root = next((p for p in (here, *here.parents) if (p / "pyproject.toml").exists()), None)
if root is None:
    sys.exit(0)  # not inside the project: nothing to check

result = subprocess.run(
    [sys.executable, "-m", "unittest"], cwd=root, capture_output=True, text=True
)
counter = Path(tempfile.gettempdir()) / f"stop-gate-{event.get('session_id', 'unknown')}"

if result.returncode == 0:
    counter.unlink(missing_ok=True)
    sys.exit(0)  # silent success

# stop_hook_active is true when the agent is already continuing because a Stop hook blocked it.
blocks = int(counter.read_text()) if event.get("stop_hook_active") and counter.exists() else 0
if blocks >= MAX_BLOCKS:
    counter.unlink(missing_ok=True)
    warning = f"Stop gate: tests still fail after {MAX_BLOCKS} attempts. Don't trust this turn's work."
    print(json.dumps({"systemMessage": warning}))  # shown to you, not to the agent
    sys.exit(0)

counter.write_text(str(blocks + 1))
tail = "\n".join((result.stdout + result.stderr).strip().splitlines()[-TAIL_LINES:])
print(
    "The test suite fails, so you can't finish yet.\n"
    "Fix the code, not the tests: don't skip, delete or weaken a test.\n"
    f"Last lines of `python -m unittest`:\n{tail}",
    file=sys.stderr,
)
sys.exit(2)  # 2 blocks the stop; any other non-zero code would not
```

`.claude/settings.json` (para Claude Code):

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"${CLAUDE_PROJECT_DIR}/scripts/stop_gate.py\"",
            "timeout": 120
          }
        ]
      }
    ]
  }
}
```

**Codex:** crea en su lugar `.codex/hooks.json`, con la misma estructura y este comando: `"python3 \"$(git rev-parse --show-toplevel)/scripts/stop_gate.py\""` ([hooks de Codex](https://learn.chatgpt.com/docs/hooks)). Codex solo carga los hooks del proyecto si el proyecto es de confianza, y solo ejecuta un hook nuevo después de que lo revises y lo apruebes con `/hooks`.

El límite de reintentos importa sobre todo en Codex: Claude Code se rinde por su cuenta tras 8 bloqueos seguidos, pero la documentación de Codex no describe ningún límite parecido.

**Punto de control:** los dos comandos siguientes no muestran errores.

```bash
python3 -m json.tool .claude/settings.json
python3 -m py_compile scripts/stop_gate.py
```

### 4. Prueba la puerta antes de fiarte de ella (5 minutos)

Una guarda que nunca has visto fallar no es una guarda. Pásale al script un evento de Stop falso, el mismo JSON que enviaría la herramienta del agente:

```bash
echo '{"cwd": "'"$PWD"'", "session_id": "manual", "stop_hook_active": false}' \
  | python3 scripts/stop_gate.py
echo "exit code: $?"
```

En tu rama los tests están en rojo, así que deberías ver el final de los fallos y `exit code: 2`.

Ahora comprueba el camino en verde. Los archivos de la puerta, que aún no están en git, te acompañan al cambiar de rama:

```bash
git switch main
echo '{"cwd": "'"$PWD"'", "session_id": "manual", "stop_hook_active": false}' \
  | python3 scripts/stop_gate.py
echo "exit code: $?"
git switch lab-3-gate
```

**Punto de control:** en `lab-3-gate` viste `exit code: 2` con los nombres de los tests que fallan, y en `main` viste `exit code: 0` sin ninguna otra salida. Haz commit de la puerta:

```bash
git add scripts .claude          # Codex: git add scripts .codex
git commit -m "Add a Stop hook that runs the tests"
```

### 5. Deja que el agente se tope con la puerta (15 minutos)

Abre una sesión **nueva** en tu copia. En Claude Code, escribe `/hooks` y confirma que aparece un hook de Stop de Project Settings. En Codex, aprueba el hook en `/hooks`. Después:

```text
Implementa esto: `shelf add` tiene que rechazar un título vacío o formado solo
por espacios y un --status desconocido. Trata los dos casos como errores de uso,
igual que el resto de la línea de comandos: la línea de uso, después un mensaje
de error claro, código de salida 2 y sin guardar nada. Que el cambio sea
pequeño. Solo para este ejercicio: no leas ni ejecutes los tests. Para en cuanto
creas que el código está terminado.
```

**Fíjate en:**

- Cuando el agente para, el hook lo bloquea. En Claude Code, la transcripción muestra el mensaje del hook con los tests que fallan.
- El agente lee los fallos y cambia **el código**, casi seguro `shelf/commands/add.py` y quizá `shelf/cli.py`: la redacción del mensaje, la línea de uso, el código de salida (hoy `cli.py` convierte un error de un comando en código 1, no 2), o varias de esas cosas. Un primer intento habitual es usar `choices=` de argparse para `--status`: sale con 2, pero su propio mensaje no coincide con la especificación.
- Intenta parar otra vez, y la puerta vuelve a ejecutarse. Cuenta las rondas.

Si el agente edita un test para que coincida con su propia redacción, interrúmpelo y escribe: `Revierte tus cambios en tests/. Los mensajes de los tests son la especificación.` Es el trinquete de la verificación de la lección, en directo.

Si el agente lo hizo todo bien a la primera, la puerta se quedó en silencio, y eso también es correcto. Confírmalo con `python3 -m unittest`.

**Punto de control:** `python3 -m unittest` pasa, y esto no muestra nada (el agente no tocó la especificación):

```bash
git diff HEAD -- tests/
```

### 6. Demuestra que los tests pueden fallar (3 minutos)

Quita la implementación, deja los tests y ejecútalos. La implementación todavía no tiene commit, así que usa la receta del stash de [la lección](README.md), que también guarda cualquier archivo que el agente haya añadido en `shelf/`:

```bash
git stash list           # apunta lo que ya hay
git stash push --include-untracked -m revert-check -- shelf/
git stash list           # la entrada de arriba tiene que decir revert-check
python3 -m unittest      # lo esperado: los tests de S6 vuelven a fallar
git stash pop            # solo si la entrada de arriba es revert-check
python3 -m unittest      # lo esperado: OK
```

**Punto de control:** rojo sin el cambio, verde con él.

### 7. Haz commit y quédate con la puerta (5 minutos)

```bash
git add shelf
git commit -m "S6: validate title and status in shelf add"
git push -u origin lab-3-gate
gh pr create --fill
```

Haz merge del pull request cuando te convenza. Los laboratorios siguientes ejecutan muchas sesiones a la vez, y todas heredarán esta puerta. S6 ya está hecha: cuando el [laboratorio 5](../05-decompose-into-tracks/lab.md) convierta el catálogo en issues de GitHub, creará S6 y la cerrará con un enlace a este pull request.

## Cómo saber que has terminado

- [ ] `python3 -m unittest` muestra `OK`, con más tests que el N que apuntaste en el paso 1.
- [ ] `git log --oneline main..lab-3-gate` muestra tres commits: los tests en rojo, la puerta y la implementación.
- [ ] `git log --oneline main..lab-3-gate -- tests/` muestra exactamente un commit: el agente nunca cambió la especificación.
- [ ] Viste la puerta devolver el código 2 a mano (paso 4), y la viste bloquear al agente al menos una vez, o confirmaste que el agente acertó a la primera.
- [ ] Con `shelf/` en el stash, los tests fallan (paso 6).

## Reflexiona

- ¿Cuántas veces bloqueó la puerta al agente y qué cambió él cada vez? ¿Le bastó con la salida del fallo o tuvo que adivinar?
- La puerta también impide que el agente pare para hacerte una pregunta mientras los tests están en rojo. ¿Dónde te haría daño eso en tu propio repositorio? ¿Es 3 el límite adecuado?
- ¿Qué regla de tu repositorio sigue siendo solo prosa y se ha incumplido al menos dos veces? ¿Qué peldaño de la escalera (hook, validador, CI, servidor) la haría cumplir?
- Tu puerta vive en archivos que el agente puede editar. ¿Qué impide que un agente la debilite, y quién se daría cuenta?

## Para ir más allá

- **Haz mecánico el trinquete.** Amplía `stop_gate.py` para que también falle si baja el número de tests o si hay tests saltados. `unittest` imprime `Ran N tests` y cuenta los tests saltados como ejecutados, así que busca también `skipped=`. Guarda el mínimo en `scripts/min_tests.txt` y súbelo, nunca lo bajes, cuando crezca la batería.
- **Añade niveles de permisos.** En `.claude/settings.json`, permite `Bash(python3 -m unittest *)`, pregunta por `Bash(git push *)` y `Bash(gh pr create *)`, y deniega `Read(./.env)`. Comprueba que las preguntas que te siguen llegando son las que importan ([permisos](https://code.claude.com/docs/en/permissions)).
- **Usa la misma puerta en las dos herramientas.** Si tienes Claude Code y Codex, configura los dos archivos y dale la misma tarea a cada uno. Compara cómo muestra el bloqueo cada herramienta y cómo reacciona cada agente.
- **En tu propio repositorio:** añade la puerta con tu comando de tests más rápido y mantenla una semana. Apunta cada bloqueo: ¿era un error real, un test inestable o una puerta demasiado lenta?
