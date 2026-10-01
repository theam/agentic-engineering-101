---
title: "Construye tus propias skills"
kind: appendix
last_reviewed: 2026-10-01
---

# Construye tus propias skills

En The Agile Monkeys seguimos nuestro flujo de trabajo en local con [claude-dev-kit](https://github.com/theam/claude-dev-kit), un plugin open source que mantenemos, y estamos reuniendo en él las skills que compartimos como equipo. **No lo necesitas, ni ningún otro plugin, para seguir esta guía ni para dedicarte a la ingeniería agéntica.** Mucha gente prefiere construir sus propias skills, y construir una es la mejor forma de entender qué hace por ti cualquier plugin. Este apéndice explica cómo.

> [!IMPORTANT]
> **Comprobado con la documentación oficial el 2026-10-01.** Los formatos y las carpetas de las skills son jóvenes y siguen cambiando. Cada ruta y cada campo de esta página enlaza a su fuente. Cuando la documentación no coincida con esta página, manda la documentación: [abre una issue de "tool drift"](https://github.com/theam/agentic-engineering-101/issues/new?template=tool-drift.yml).

## Cuándo merece la pena una skill

Una skill empaqueta el oficio de una tarea recurrente: instrucciones que el agente carga cuando aparece la tarea, más los scripts o archivos de referencia que necesite. El [módulo 4](../04-context-is-infrastructure/README.md) da la regla que seguimos: crea una skill cuando algo ya duele, porque la descripción de cada skill ocupa contexto en cada turno. Buenos candidatos:

- un flujo que ejecutas varias veces por semana y que acabas explicando una y otra vez, como llevar una issue hasta un pull request o preparar una release;
- una corrección que ya has hecho dos veces y que necesita criterio, así que un script no puede imponerla;
- una lista de revisión para un tipo concreto de cambio.

Si una regla tiene que cumplirse siempre, no es una skill. Es un hook, un validador o una comprobación de CI ([módulo 3](../03-close-the-loop/README.md)). Las skills orientan; las guardas obligan.

## Anatomía de una skill

Una skill es una carpeta con un archivo `SKILL.md` dentro: front matter en YAML y, después, instrucciones en Markdown. Claude Code y Codex se basan en el estándar abierto [Agent Skills](https://agentskills.io/specification), así que la misma carpeta funciona en los dos.

```text
work-issue/
├── SKILL.md          # obligatorio: front matter e instrucciones
└── pr-template.md    # opcional: se carga solo cuando SKILL.md lo enlaza
```

- **`name`** identifica la skill. El estándar pide minúsculas, números y guiones, y que coincida con el nombre de la carpeta. En Claude Code es también el `/nombre` que escribes.
- **`description`** decide cuándo carga el agente la skill por su cuenta. Di qué hace, cuándo usarla y cuándo no. Es la parte que cuesta contexto en cada turno, así que cada palabra tiene que valer. El estándar la limita a 1.024 caracteres.
- **El cuerpo** solo se carga cuando se usa la skill. Mantenlo corto: tanto el estándar como la [documentación de skills de Claude Code](https://code.claude.com/docs/en/skills) recomiendan que `SKILL.md` no pase de 500 líneas y que el material de referencia vaya en archivos enlazados.

Dónde viven las skills:

| Alcance | Claude Code | Codex |
| --- | --- | --- |
| Un repositorio, compartida con el equipo | `.claude/skills/<nombre>/SKILL.md` | `.agents/skills/<nombre>/SKILL.md` |
| Tú, en todos tus repositorios | `~/.claude/skills/<nombre>/SKILL.md` | `~/.agents/skills/<nombre>/SKILL.md` |
| Ejecutarla de forma explícita | `/<nombre>` | `$<nombre>`, o elígela con `/skills` |

Fuentes: [skills de Claude Code](https://code.claude.com/docs/en/skills) y [skills de Codex](https://learn.chatgpt.com/docs/build-skills).

Para usar una misma skill en las dos herramientas, deja la carpeta en `.agents/skills/` y crea un enlace simbólico a ella desde `.claude/skills/`; Claude Code sigue las carpetas de skills enlazadas. Si quieres que la skill sea portable, usa solo los campos del estándar (`name`, `description`, `license`, `compatibility`, `metadata` y `allowed-tools`). Campos como `disable-model-invocation` son extensiones de Claude Code.

## Tu primera skill: de la issue al pull request

Este es el ciclo del [módulo 2](../02-one-agent-done-well/README.md) convertido en skill, escrito para el [proyecto de práctica](../../../practice/shelf/). Guárdalo como `.agents/skills/work-issue/SKILL.md`. Las instrucciones van en inglés, como todo artefacto persistente ([módulo 2](../02-one-agent-done-well/README.md)):

```markdown
---
name: work-issue
description: Take one GitHub issue to a pull request, with a plan the user approves before any code is written. Use when the user asks to work on, implement or fix a specific issue by number. Don't use it for questions about an issue or to review a pull request.
---

# Work an issue

The user gives you an issue number. Work on that issue only.

1. Read it with `gh issue view <number>`, then read the code it touches.
   Answer your own questions from the code before asking the user.
2. List what the issue doesn't settle, with options and a recommendation
   for each. Wait for the user's choices.
3. Write the plan in under 25 lines: the files you'll change, any change to
   stored data, an example of the output, the tests you'll add and why each
   would fail without the change, and what you won't do. Then wait. Don't
   write code until the user says "build".
4. Create a branch for the issue. Write the tests first and show them
   failing, then implement.
5. Run the whole suite with `python -m unittest` and show the output. If
   anything fails, fix it before you continue.
6. Answer two questions: do we have any side effects? What did you assume
   that you didn't check?
7. Open the pull request with `gh pr create`. In the description: what
   changes, the decisions from step 2, the command you ran to verify and its
   result, and "Closes #<number>".

Never merge, and never push to main.
```

Ejecútala con `/work-issue 3` en Claude Code, con `$work-issue 3` en Codex, o simplemente pide "vamos a trabajar en la issue 3". Cada línea sale de un módulo:

| Paso | Qué hace | De dónde viene |
| --- | --- | --- |
| 1 | Explorar y responder desde el código | [Módulo 2](../02-one-agent-done-well/README.md) |
| 2–3 | Conversar y revisar la intención antes de que exista código | [Módulo 2](../02-one-agent-done-well/README.md) |
| 4–5 | Primero en rojo, y pruebas en lugar de "terminado" | [Módulo 3](../03-close-the-loop/README.md) |
| 6 | Preguntas de seguimiento que encuentran lo que nadie buscaba | [Módulo 2](../02-one-agent-done-well/README.md) |
| 7 | Un pull request que lleva sus decisiones y sus pruebas | [Módulo 7](../07-agents-review-agents/README.md) |
| Última línea | El merge lo hacen las personas | [Módulo 9](../09-teams-and-organizations/README.md) |

Dos decisiones para tu propia versión:

- **Quién la arranca.** Un flujo que sube ramas y abre pull requests puede que prefieras arrancarlo tú. En Claude Code, `disable-model-invocation: true` en el front matter hace que solo `/work-issue` la ejecute; la documentación lo recomienda para flujos con efectos secundarios: «No quieres que Claude decida desplegar porque tu código parece listo» (traducción propia, [skills de Claude Code](https://code.claude.com/docs/en/skills)).
- **Lo que la skill no puede garantizar.** "Muestra la salida" es un consejo. Acompaña la skill con el Stop hook del [módulo 3](../03-close-the-loop/README.md), para que el agente no pueda terminar mientras la suite falla, siga o no la skill.

## Deja que el agente haga el borrador y después pruébala

No tienes que escribir la primera versión a mano. Codex incluye `$skill-creator`, que redacta una skill contigo. Con cualquier agente, describe el flujo, pide un `SKILL.md` que siga el estándar y revísalo como si fuera un plan.

Después pruébala como si fuera código:

1. **Ejecútala sobre una issue real en una sesión nueva.** La issue S3 del proyecto de práctica funciona bien: tiene decisiones que la issue no resuelve.
2. **Fíjate en dónde se desvía.** ¿Empezó a construir antes de "build"? ¿Se saltó el test que falla? ¿Hizo preguntas que el código podía responder?
3. **Arregla la skill, no la sesión.** Afina el paso que se saltó. Si el mismo paso se salta dos veces, pásalo a un hook.
4. **Comprueba cuándo se activa.** Haz una pregunta sobre una issue y confirma que la skill no se carga. Pide trabajar en una y confirma que sí.
5. **Pide al agente que la revise.** "Read the work-issue skill. Which step is ambiguous, and what would you do differently?"

Guarda las correcciones en el mismo registro que empezaste en el [laboratorio 2](../02-one-agent-done-well/lab.md).

## Compártela con tu equipo

- **En un repositorio:** haz commit de la carpeta de la skill. Una skill de equipo pasa por un pull request y se revisa como el código, porque todos los agentes del equipo la van a seguir ([módulo 9](../09-teams-and-organizations/README.md)).
- **Entre repositorios:** empaqueta tus skills como plugin en lugar de copiarlas. En Claude Code, un plugin es una carpeta con un manifiesto `.claude-plugin/plugin.json` y sus componentes, como `skills/`, `agents/` y `hooks/`. Un marketplace es un repositorio con un `.claude-plugin/marketplace.json` que enumera tus plugins. Mientras lo desarrollas, carga el plugin directamente desde su carpeta con `--plugin-dir` ([plugins de Claude Code](https://code.claude.com/docs/en/plugins)). Codex también puede empaquetar skills como plugins ([skills de Codex](https://learn.chatgpt.com/docs/build-skills)).
- **Vigila el coste:** las descripciones de las skills de un plugin activado están en el contexto en cada turno, incluso en sesiones que nunca las usan. En Claude Code, `/skill-doctor` muestra cuánto cuesta cada skill y con qué frecuencia se usa.

Eso es todo lo que es claude-dev-kit: un conjunto de skills, agentes y hooks en un solo plugin que se instala una vez. Si quieres ver un conjunto de skills más grande, [lee su código](https://github.com/theam/claude-dev-kit). Si prefieres construir las tuyas, las piezas de esta página son todo lo que necesitas.

## Ojo con

- ❌ Una skill para todo. ✅ Espera a que una tarea duela; cada descripción cuesta contexto en cada turno.
- ❌ Una descripción vaga, como "ayuda con las issues". ✅ Di qué hace, cuándo usarla y cuándo no.
- ❌ Reglas que tienen que cumplirse siempre, escritas como texto de una skill. ✅ Hooks, validadores y CI.
- ❌ La misma skill copiada en cada repositorio. ✅ Un solo sitio, un repositorio o un plugin, que cambia mediante pull requests revisados.
- ❌ Un `SKILL.md` de 900 líneas. ✅ Un cuerpo corto que enlaza archivos de referencia.
- ❌ Instalar la skill o el plugin de otra persona sin leerlo. ✅ Se ejecuta con tus permisos. Léelo antes ([seguridad de los plugins](https://code.claude.com/docs/en/plugins/security)).

## Para profundizar

- [Skills de Claude Code](https://code.claude.com/docs/en/skills): todos los campos del front matter, los argumentos y lo que cuesta cada skill.
- [Skills de Codex](https://learn.chatgpt.com/docs/build-skills): dónde busca Codex, uso explícito e implícito, `$skill-creator`.
- [Especificación de Agent Skills](https://agentskills.io/specification): el formato portable en el que se basan los dos.
- [Plugins de Claude Code](https://code.claude.com/docs/en/plugins): cuándo necesitas un plugin, ámbitos de instalación y marketplaces.
- [claude-dev-kit](https://github.com/theam/claude-dev-kit): nuestro plugin, open source, como ejemplo práctico.
