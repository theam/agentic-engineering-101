---
title: "Herramientas"
kind: reference
last_reviewed: 2026-09-17
---

# Herramientas

> [!IMPORTANT]
> **Última revisión: 2026-09-17.** Las herramientas cambian cada mes: los flags se renombran y las funciones salen de la fase de prueba o desaparecen. Comprobamos cada comando de esta página con la documentación oficial en esa fecha, y cada entrada enlaza a ella. Si algo ya no coincide con la documentación, [abre una issue de tipo "tool drift"](https://github.com/theam/agentic-engineering-101/issues/new?template=tool-drift.yml) con el enlace que muestra el cambio.

Esta página es el sitio, con fecha, para el detalle de herramientas que cambia a menudo. Las lecciones enseñan prácticas que funcionan con cualquier agente de programación capaz, y usan ejemplos concretos de herramientas cuando enseñan un principio, comprobados en la documentación oficial y enlazados; esta página te dice qué botones implementan hoy esas prácticas.

## Principios: las herramientas cambian cada mes, las prácticas perduran

1. **Elige herramientas por la práctica que sostienen.** Pregúntate qué aporta una herramienta al contexto, la verificación, el aislamiento o la revisión. Una herramienta nueva que no mejora nada de eso es una distracción, por buena que parezca la demo.
2. **Usa lo que tu agente ya trae antes de añadir otra capa.** Los worktrees, las sesiones en segundo plano, los subagentes y los comandos de revisión ya vienen integrados en los agentes principales. Peter Steinberger [advierte de la trampa](https://steipete.me/posts/just-talk-to-it) de construir orquestación en lugar de entregar, y DHH espera que los propios laboratorios de IA absorban esas capas de coordinación ([Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/)).
3. **Mantén un solo contrato para todos los agentes.** Pon las instrucciones compartidas en `AGENTS.md` y deja el archivo propio de cada herramienta (como `CLAUDE.md`) como un adaptador mínimo que apunta a él. Así cambiar o combinar herramientas no cuesta casi nada.
4. **Usa dos proveedores: uno escribe y el otro revisa.** Un revisor de otro proveedor no comparte los puntos ciegos de quien escribió.
5. **Prefiere una CLI a un servidor MCP cuando existen las dos.** La [guía de costes de Claude Code](https://code.claude.com/docs/en/costs) explica que herramientas de línea de comandos como `gh` usan el contexto de forma más eficiente que los servidores MCP, porque no añaden listados de herramientas al contexto.
6. **Aísla antes de dar autonomía.** Nunca desactives las confirmaciones de permisos en una máquina con credenciales. Usa antes un sandbox, un contenedor o una máquina virtual.
7. **Dale a una herramienta nueva una semana de trabajo real.** Compara herramientas con las mismas tareas, sobre tu código y con la misma verificación. La primera impresión con un proyecto de juguete engaña.
8. **Confía en la documentación antes que en esta página.** Usa los enlaces. Si no coinciden con lo que lees aquí, gana la documentación y esta página necesita una issue de "tool drift".

## Agentes de programación

### Claude Code

- **Qué es:** El agente de programación de Anthropic. Lee tu código, edita archivos y ejecuta comandos. Está disponible en la terminal, en extensiones para IDE, en una app de escritorio y en el navegador. Toma las instrucciones de `CLAUDE.md` y admite hooks, skills, subagentes, MCP y modos de permisos.
- **Cuándo lo usamos:** En The Agile Monkeys es nuestro harness principal para pensar y planificar. Abrimos una sesión en el repositorio de misión y conversamos sobre un diseño; tiende a explicar más, y eso nos ayuda a pensar. También lo usamos para implementar, a menudo con un subagente que trabaja en un worktree.
- **Documentación:** [Overview](https://code.claude.com/docs/en/overview) · [Best practices](https://code.claude.com/docs/en/best-practices) · [CLI reference](https://code.claude.com/docs/en/cli-reference) · [Commands](https://code.claude.com/docs/en/commands)

### Codex CLI

- **Qué es:** El agente de programación de OpenAI para la terminal. Inspecciona código, hace cambios y ejecuta comandos dentro de un sandbox, y se puede automatizar con `codex exec`. Lee `AGENTS.md`. Codex también funciona en la app de escritorio de ChatGPT, en una extensión para IDE y en la nube. El código fuente de la CLI está [en GitHub](https://github.com/openai/codex).
- **Cuándo lo usamos:** Cuando una tarea está bien especificada y queremos que el agente la tome y avance sin más. Lo usamos mucho como revisor de otro proveedor en los pull requests escritos con Claude Code.
- **Documentación:** [Codex CLI](https://learn.chatgpt.com/docs/codex/cli) · [Best practices](https://learn.chatgpt.com/guides/best-practices) · [Comandos y opciones](https://learn.chatgpt.com/docs/developer-commands?surface=cli)

### OpenCode

- **Qué es:** Un agente de programación de código abierto, disponible como interfaz de terminal, app de escritorio o extensión para IDE. Funciona con muchos proveedores de modelos en cuanto configuras sus claves de API, y su comando `/init` crea un `AGENTS.md`.
- **Cuándo lo usamos:** No lo usamos a diario. Es una buena opción si quieres un solo harness para varios proveedores de modelos, incluidos los modelos de pesos abiertos; DHH comenta que lo usa para eso.
- **Documentación:** [Documentación de OpenCode](https://opencode.ai/docs)

### Agentes de GitHub Copilot

- **Qué es:** GitHub Copilot ejecuta agentes en varios sitios: en la vista de chat de VS Code (el rol Agent implementa un cambio; el rol Plan propone antes un enfoque), en la terminal con Copilot CLI y como agente en la nube en GitHub, que trabaja a partir de una issue en su propia rama, en un entorno basado en GitHub Actions.
- **Cuándo lo usamos:** No es nuestro agente principal. Tiene sentido cuando un equipo ya vive en VS Code y GitHub y quiere agentes sin sumar otro proveedor. Copilot también revisa pull requests (lo vemos más abajo).
- **Documentación:** [Agents in VS Code](https://code.visualstudio.com/docs/agents/overview) · [Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli) · [About Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent)

### Cursor

- **Qué es:** Un editor de código con IA. Su Agent completa tareas de programación de varios pasos, ejecuta comandos en la terminal y edita código, con puntos de restauración para deshacer cambios.
- **Cuándo lo usamos:** No es nuestra herramienta principal, porque trabajamos desde la terminal. Es una elección razonable para quien quiere revisar diffs dentro de un editor mientras trabajan los agentes. Las prácticas de esta guía se aplican igual.
- **Documentación:** [Cursor Agent](https://cursor.com/docs/agent/overview)

## Gestores de sesiones y terminales

Primero los principios (los explica el [módulo 6](../06-run-sessions-in-parallel/README.md)): agrupa las sesiones por pista de trabajo, ordénalas por prioridad, atiende las notificaciones por turnos empezando por arriba, pon nombre a tus sesiones, guarda sus IDs y deja una shell normal junto a cada agente. Cualquiera de estas herramientas lo permite. Elige la que menos te estorbe.

### tmux

- **Qué es:** Un multiplexor de terminal. Ejecuta varios programas en una sola terminal y te permite desacoplarlos (siguen funcionando) y volver a conectarte después.
- **Cuándo lo usamos:** Es el mínimo común denominador: funciona con cualquier agente de línea de comandos, en tu portátil o en una máquina remota, sin instalar ninguna app nueva. No sabe nada de agentes, así que no recibes una notificación de "necesita tu respuesta" salvo que la añadas tú. DHH trabajaba con sus agentes en paneles de tmux antes de pasar a una herramienta pensada para agentes ([Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/)).
- **Documentación:** [Wiki de tmux](https://github.com/tmux/tmux/wiki)

### Warp

- **Qué es:** Una terminal que sus creadores llaman "Agentic Development Environment". Tiene su propio agente y ejecuta agentes de línea de comandos de terceros, como Claude Code, Codex y OpenCode, con extras como notificaciones y revisión de código.
- **Cuándo lo usamos:** Es donde viven hoy muchas de nuestras sesiones: agrupadas, ordenadas por importancia y atendidas cuando una notificación avisa de que una sesión terminó o necesita una decisión.
- **Documentación:** [Documentación de Warp](https://docs.warp.dev/)

### Superset

- **Qué es:** Una app de escritorio para ejecutar muchos agentes de programación de línea de comandos en paralelo, cada tarea aislada en su propio worktree de git, con su rama y su terminal. Para macOS, con versiones experimentales para Linux. Código disponible bajo la Elastic License 2.0.
- **Cuándo lo usamos:** La usamos antes de nuestra terminal actual. Ver el pull request de cada sesión junto a la sesión era muy cómodo. En nuestra experiencia era algo inestable cuando la usamos; comprueba la versión actual.
- **Documentación:** [Superset en GitHub](https://github.com/superset-sh/superset)

### Conductor

- **Qué es:** Una app para Mac que ejecuta agentes de Claude Code, Codex y Cursor en paralelo, en espacios de trabajo aislados, y te deja revisar y hacer merge de sus cambios.
- **Cuándo lo usamos:** No la hemos adoptado. Aparece aquí porque aplica el mismo principio (un espacio de trabajo aislado por tarea) con una interfaz visual.
- **Documentación:** [conductor.build](https://www.conductor.build/)

### claude-squad

- **Qué es:** Una app de terminal que gestiona varios agentes locales (Claude Code, Codex, Gemini, Aider) en espacios de trabajo separados, con sesiones de tmux para las terminales y worktrees de git para el código.
- **Cuándo lo usamos:** No la hemos adoptado. Es una opción ligera si te gusta tmux y quieres aislar con worktrees sin escribir tus propios scripts.
- **Documentación:** [claude-squad en GitHub](https://github.com/smtg-ai/claude-squad)

### Herdr

- **Qué es:** Un entorno de ejecución en segundo plano para agentes de programación: sesiones de terminal que mantienen agentes como Claude Code, Codex y OpenCode en marcha aunque te desconectes. De código abierto (Apache 2.0).
- **Cuándo lo usamos:** No lo hemos adoptado. DHH lo describe como tmux con notificaciones de agentes en [Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/).
- **Documentación:** [herdr.dev](https://herdr.dev/)

### Integrado: vista de agentes, sesiones en segundo plano y `--worktree` en Claude Code

- **Qué es:** `claude agents` abre la vista de agentes (agent view), una pantalla que muestra todas las sesiones en segundo plano y cuáles necesitan tu respuesta (en research preview). `claude --bg "…"` inicia una sesión en segundo plano. `claude --worktree <nombre>` inicia una sesión en un worktree de git nuevo dentro de `.claude/worktrees/<nombre>/`, en su propia rama.
- **Cuándo lo usamos:** Cuando quieres sesiones en paralelo sin instalar nada más. El flag de worktree es la forma más rápida de seguir nuestra norma por defecto: un worktree por cada pista de código.
- **Documentación:** [Agent view](https://code.claude.com/docs/en/agent-view) · [Worktrees](https://code.claude.com/docs/en/worktrees) · [CLI reference](https://code.claude.com/docs/en/cli-reference)

> [!TIP]
> No necesitas ninguna de estas herramientas para aislar el trabajo. Un simple `git worktree add` funciona con cualquier agente. Consulta la [documentación de git worktree](https://git-scm.com/docs/git-worktree). Codex ofrece worktrees desde la app de escritorio de ChatGPT: [worktrees en Codex](https://learn.chatgpt.com/docs/environments/git-worktrees).

## Revisores automáticos

### Revisión de código de Codex

- **Qué es:** Tres formas de conseguir una revisión de Codex. En la CLI, `/review` lanza un revisor dedicado contra una rama base, los cambios sin commit, un commit o unas instrucciones propias, sin tocar tu directorio de trabajo. `codex review` hace el mismo tipo de revisión en modo no interactivo. En GitHub, comenta `@codex review` en un pull request o activa las revisiones automáticas; ahí solo señala problemas P0 y P1 y sigue la sección `## Code Review Rules` de tu `AGENTS.md`.
- **Cuándo lo usamos:** Es nuestro revisor de otro proveedor por defecto. En nuestros repositorios vuelve a revisar cada push, y sus hallazgos van a nuestro registro de triaje ([módulo 7](../07-agents-review-agents/README.md)).
- **Documentación:** [Code review](https://learn.chatgpt.com/docs/code-review) · [Review GitHub pull requests with Codex](https://learn.chatgpt.com/docs/third-party/github)

### Revisión de código de GitHub Copilot

- **Qué es:** Copilot revisa pull requests, encuentra problemas y sugiere correcciones que puedes aplicar. Las revisiones pueden ejecutarse automáticamente al abrir un pull request o en cada push, y las instrucciones del repositorio en `.github/copilot-instructions.md` las orientan. Por defecto, sus revisiones no cuentan como aprobaciones obligatorias.
- **Cuándo lo usamos:** Como revisor independiente adicional en repositorios de GitHub, junto a un modelo de otro proveedor. DHH dice que «no para de encontrar cosas que están rotas de verdad» (traducción propia) en [Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/).
- **Documentación:** [About Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review)

### Claude Code GitHub Actions y Code Review

- **Qué es:** Dos productos. [Claude Code GitHub Actions](https://github.com/anthropics/claude-code-action) ejecuta Claude Code en tus propios workflows: menciona `@claude` en una issue o un pull request, o lánzalo con cualquier evento de GitHub; `/install-github-app` lo configura. Code Review es un servicio gestionado (en research preview, para planes Team y Enterprise) en el que varios agentes revisan cada pull request y publican hallazgos clasificados por gravedad; nunca aprueba ni bloquea un merge, y se ajusta con un `REVIEW.md` o con `CLAUDE.md`. En local, `/code-review` (alias `/review`) revisa el diff actual.
- **Cuándo lo usamos:** GitHub Actions, cuando quieres un job de agente en la CI que tú defines y controlas. El `/code-review` local, como comprobación rápida con contexto limpio antes de abrir un pull request.
- **Documentación:** [GitHub Actions](https://code.claude.com/docs/en/github-actions) · [Code Review](https://code.claude.com/docs/en/code-review)

> [!WARNING]
> Un revisor automático que no conoce el objetivo del pull request persigue problemas rebuscados y hace crecer el cambio. Dale a cada revisor la declaración de intención y el contexto del proyecto. El [módulo 7](../07-agents-review-agents/README.md) explica cómo.

## Estándares

### AGENTS.md

- **Qué es:** Un formato abierto para instrucciones de agentes: un archivo predecible donde los agentes de programación buscan cómo compilar, probar y trabajar en un proyecto. Los archivos anidados se aplican a sus subcarpetas, y gana el más cercano. Lo custodia la Agentic AI Foundation, dentro de la Linux Foundation, y lo leen muchos agentes, entre ellos Codex, GitHub Copilot, Cursor y OpenCode.
- **Cuándo lo usamos:** En todos los repositorios. Es nuestro único contrato compartido. Claude Code lee `CLAUDE.md` en su lugar, así que nuestro `CLAUDE.md` contiene una importación `@AGENTS.md` ([documentación de memoria de Claude Code](https://code.claude.com/docs/en/memory)).
- **Documentación:** [agents.md](https://agents.md/) · [AGENTS.md en Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

### MCP (Model Context Protocol)

- **Qué es:** Un estándar de código abierto para conectar aplicaciones de IA con sistemas externos: fuentes de datos, herramientas y flujos de trabajo. Lo admiten Claude Code (`claude mcp`), Codex (`codex mcp`) y muchos editores.
- **Cuándo lo usamos:** Para sistemas sin una buena CLI, y para que los agentes de cada persona lean y escriban en un sistema compartido. Cada servidor conectado cuesta contexto, así que conecta solo lo que necesita cada repositorio.
- **Documentación:** [What is MCP?](https://modelcontextprotocol.io/)

## Sandbox y aislamiento

### Sandbox de Claude Code

- **Qué es:** Un sandbox para la herramienta Bash que impone el sistema operativo: defines qué archivos y dominios de red pueden alcanzar los comandos, y Claude ejecuta comandos dentro de ese límite sin preguntar cada vez. Se activa con `/sandbox`. Funciona en macOS, Linux y WSL2, no en Windows nativo. Anthropic cuenta que internamente [redujo un 84 % las confirmaciones de permisos](https://www.anthropic.com/engineering/claude-code-sandboxing).
- **Cuándo lo usamos:** Cuando el cansancio de tanto confirmar tienta a alguien a saltarse los permisos. El sandbox es la respuesta más segura.
- **Documentación:** [Sandboxing](https://code.claude.com/docs/en/sandboxing) · [Choose a sandbox environment](https://code.claude.com/docs/en/sandbox-environments)

### Sandbox de Codex

- **Qué es:** Codex ejecuta por defecto los comandos del agente dentro de un sandbox. `--sandbox` elige entre `read-only`, `workspace-write` y `danger-full-access`, y `codex exec` empieza en solo lectura. `/permissions` cambia las aprobaciones durante una sesión.
- **Cuándo lo usamos:** Mantenlo activado. Las propias [best practices de Codex](https://learn.chatgpt.com/guides/best-practices) recomiendan mantener estrictos por defecto las aprobaciones y el sandbox, y relajarlos solo en repositorios de confianza. Usa `danger-full-access` solo en un runner o contenedor aislado.
- **Documentación:** [Sandbox](https://learn.chatgpt.com/docs/sandboxing) · [Permissions](https://learn.chatgpt.com/docs/permission-modes)

### Dev containers

- **Qué es:** Una [especificación abierta](https://containers.dev/) para contenedores de desarrollo definidos en `devcontainer.json`. Con el agente instalado dentro, los comandos que ejecuta corren en el contenedor, no en tu máquina.
- **Cuándo lo usamos:** Cuando un equipo quiere el mismo entorno aislado para cada persona, o ejecutar un agente con menos confirmaciones. Lee el aviso de la documentación de Claude Code: con los permisos desactivados, un proyecto malicioso aún puede extraer cualquier cosa que haya dentro del contenedor, incluidas las credenciales del agente.
- **Documentación:** [Claude Code in dev containers](https://code.claude.com/docs/en/devcontainer)

### container-use

- **Qué es:** Una herramienta experimental de código abierto de Dagger que da a cada agente un contenedor nuevo en su propia rama de git. Funciona con agentes que admiten MCP.
- **Cuándo lo usamos:** No la hemos adoptado. Merece un vistazo si quieres aislar cada agente en un contenedor sin construirlo tú; espera cambios, porque sus mantenedores dicen que está en una fase temprana de desarrollo.
- **Documentación:** [container-use en GitHub](https://github.com/dagger/container-use)

> [!WARNING]
> En el [ataque a la cadena de suministro s1ngularity](https://nx.dev/blog/s1ngularity-postmortem) de 2025, un paquete malicioso ejecutó las CLI de IA instaladas con flags para saltarse los permisos y buscar secretos. Nunca dejes un alias que se salte los permisos en una máquina con credenciales.

## Claude Code ↔ Codex: equivalencias

Solo incluimos filas que comprobamos en la documentación de los dos proveedores el 2026-09-17. Cuando una fila deje de ser cierta, abre una issue de "tool drift".

| Lo que quieres | Claude Code | Codex CLI |
| --- | --- | --- |
| Archivo de instrucciones del proyecto | `CLAUDE.md`; importa `AGENTS.md` con `@AGENTS.md` ([memory](https://code.claude.com/docs/en/memory)) | `AGENTS.md` ([AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)) |
| Generar un archivo de instrucciones inicial | `/init` crea `CLAUDE.md` ([commands](https://code.claude.com/docs/en/commands)) | `/init` crea `AGENTS.md` ([commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli)) |
| Ejecutar un prompt sin sesión interactiva | `claude -p "…"` ([modo no interactivo](https://code.claude.com/docs/en/headless)) | `codex exec "…"` ([modo no interactivo](https://learn.chatgpt.com/docs/non-interactive-mode)) |
| Retomar una sesión anterior | `claude --resume`, `claude --continue`, `/resume` ([CLI](https://code.claude.com/docs/en/cli-reference)) | `codex resume`, `/resume` ([commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli)) |
| Empezar de cero con el contexto vacío | `/clear` | `/new` (o `/clear`, que además limpia la terminal) |
| Resumir para liberar contexto | `/compact` | `/compact` |
| Planificar antes de editar | Modo plan: `Shift+Tab`, `/plan` o `--permission-mode plan` ([permission modes](https://code.claude.com/docs/en/permission-modes)) | Modo plan: `/plan` o `Shift+Tab` ([best practices](https://learn.chatgpt.com/guides/best-practices)) |
| Seguir trabajando hasta que se cumpla una condición | `/goal <condición>` ([goal](https://code.claude.com/docs/en/goal)) | `/goal <objetivo>` ([commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli)) |
| Revisar cambios locales | `/code-review` (alias `/review`) | `/review`; `codex review` en modo no interactivo ([code review](https://learn.chatgpt.com/docs/code-review)) |
| Revisar un pull request en GitHub | `@claude review` con Code Review, o `@claude` con GitHub Actions | `@codex review` ([GitHub](https://learn.chatgpt.com/docs/third-party/github)) |
| Trabajar en un worktree aislado | `claude --worktree <nombre>` ([worktrees](https://code.claude.com/docs/en/worktrees)) | Opción Worktree en la app de escritorio de ChatGPT ([worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees)); en otros casos, `git worktree add` |
| Controlar qué se ejecuta sin preguntar | Modos de permisos y reglas de `/permissions`; `/sandbox` | `/permissions`; `--sandbox` y `--ask-for-approval` ([CLI](https://learn.chatgpt.com/docs/codex/cli)) |
| Saltarse todas las confirmaciones (solo en entornos aislados) | `--dangerously-skip-permissions` | `--dangerously-bypass-approvals-and-sandbox` (alias `--yolo`) |
| Scripts deterministas en el ciclo de vida | [Hooks](https://code.claude.com/docs/en/hooks) | [Hooks](https://learn.chatgpt.com/docs/hooks) |
| Delegar en agentes auxiliares | [Subagents](https://code.claude.com/docs/en/sub-agents) | [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) |
| Conectar herramientas externas | `claude mcp` | `codex mcp` |

> [!NOTE]
> **En The Agile Monkeys** mantenemos hooks equivalentes en los dos agentes, así que una regla que se aplica en Claude Code también se aplica en Codex. Las reglas compartidas viven en `AGENTS.md`; cada herramienta tiene un adaptador mínimo.

## Informar de cambios en las herramientas

¿Algo de esta página ha dejado de ser cierto? Es normal, y es la contribución más útil que puedes hacer a esta página. [Abre una issue de tipo "tool drift"](https://github.com/theam/agentic-engineering-101/issues/new?template=tool-drift.yml) con:

- la herramienta y la entrada de esta página,
- qué cambió (un flag renombrado, una función eliminada, un valor por defecto nuevo),
- un enlace a la documentación oficial o al changelog que lo muestra.

Si corriges la página tú, actualiza `last_reviewed` en el front matter y en el aviso del principio.
