---
title: "Fuentes"
kind: reference
last_reviewed: 2026-09-17
---

# Fuentes

Todas las fuentes externas en las que se apoya esta guía, agrupadas por tipo. Cada entrada da el título, el autor u organización, la fecha y una línea sobre por qué importa. Mantenemos los títulos en su idioma original. Comprobamos los enlaces el 2026-09-17.

Dos notas antes de usar esta lista:

- **Las fechas importan.** Los consejos sobre agentes de programación envejecen rápido. Un flujo de trabajo de mediados de 2025 se diseñó para modelos más débiles que uno de 2026, y algunos autores cambiaron de opinión entre un artículo y otro (lo señalamos cuando lo sabemos).
- **Proveedores y profesionales tienen sus intereses.** Los artículos de proveedores describen sus propios productos, y los profesionales famosos trabajan en condiciones poco habituales (proyectos en solitario, tokens casi ilimitados). Los citamos porque son útiles, no porque sean neutrales.

Nuestra propia práctica, la que aparece en la guía como "En The Agile Monkeys", no está en esta lista: sale de nuestro trabajo interno, y marcamos nuestros números como indicativos.

> [!TIP]
> ¿Conoces una fuente que debería estar aquí, o has encontrado un enlace roto? Abre un pull request que la añada con el mismo formato. [CONTRIBUTING.es.md](../../../CONTRIBUTING.es.md) explica cómo.

## Podcasts y charlas

- **[DHH: Future of Programming, AI, Agentic Engineering, Vibe Coding & Linux](https://lexfridman.com/dhh-2/)** — Lex Fridman Podcast #501 con David Heinemeier Hansson, 2026-08-26 ([transcripción](https://lexfridman.com/dhh-2-transcript)). Un flujo de trabajo centrado en agentes descrito en detalle (sin IDE, un proveedor construye y otro revisa, las personas deciden), con advertencias honestas sobre los códigos grandes y la sostenibilidad.
- **[The creator of Clawd: "I ship code I don't read"](https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code)** — podcast The Pragmatic Engineer, Gergely Orosz con Peter Steinberger, 2026-01-28 ([vídeo](https://www.youtube.com/watch?v=8lF7HmQ_RgY)). La fuente de "cerrar el ciclo", el radio de impacto y trabajar con 5 a 10 agentes, junto con el aviso del presentador de que es un proyecto en solitario y "YOLO".
- **[OpenClaw: The Viral AI Agent that Broke the Internet (transcripción)](https://lexfridman.com/peter-steinberger-transcript/)** — Lex Fridman Podcast #491 con Peter Steinberger, 2026-02. Los prompts de seguimiento que usamos ("lee más código", "¿qué harías distinto?") y su advertencia sobre construir herramientas en lugar de entregar.
- **[DHH's new way of writing code](https://newsletter.pragmaticengineer.com/p/dhhs-new-way-of-writing-code)** — podcast The Pragmatic Engineer, Gergely Orosz con David Heinemeier Hansson, 2026-04-08. Una etapa anterior del mismo cambio, con por qué hoy se benefician más los perfiles sénior.
- **[Sequoia Ascent 2026 summary](https://karpathy.bearblog.dev/sequoia-ascent-2026/)** — Andrej Karpathy, 2026-04-30 (su resumen de la charla). Por qué los modelos pueden automatizar lo que se puede verificar, y una frase que cita y a la que vuelve una y otra vez: puedes externalizar tu pensamiento, pero no tu comprensión.

## Artículos y guías

### Qué es agentic engineering

- **[Post en X que da nombre a "agentic engineering"](https://x.com/karpathy/status/2019137879310836075)** — Andrej Karpathy, 2026-02-04. Separa el vibe coding del trabajo profesional con agentes, que requiere más supervisión y escrutinio.
- **[A quote from Andrej Karpathy](https://simonwillison.net/2026/Feb/26/andrej-karpathy/)** — Simon Willison, 2026-02-26. Recoge la observación de Karpathy de que los agentes de programación empezaron a funcionar de verdad a finales de 2025, lo que explica por qué envejecen los consejos anteriores.
- **[Vibe engineering](https://simonwillison.net/2025/Oct/7/vibe-engineering/)** — Simon Willison, 2025-10-07. Los agentes amplifican la experiencia que ya tienes; los tests, la planificación, la documentación y la cultura de revisión importan más, no menos.
- **[Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/)** — Simon Willison, guía en curso desde 2026-02-23. Ensayos breves sobre patrones y prompts comentados; el modelo de nuestra página de [patrones de prompts](prompt-patterns.md). Capítulos que citamos: [Red/green TDD](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/) y [First run the tests](https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/).
- **[Agentic Engineering](https://addyosmani.com/blog/agentic-engineering/)** — Addy Osmani, 2026-02-04. Un contraste claro con el vibe coding, y el argumento de que los tests son lo que más marca la diferencia.
- **[Augmented Coding: Beyond the Vibes](https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes)** — Kent Beck, 2025-06-25. TDD y "tidy first" con agentes, y las señales de alarma de un agente que se desvía (bucles, funciones que nadie pidió, tests borrados).
- **[Vibe Coding: Production-Grade Software with AI](https://itrevolution.com/product/vibe-coding-book/)** (libro) — Gene Kim y Steve Yegge, IT Revolution, 2025-10-21. Usa "vibe coding" para trabajo serio en producción, al contrario que Karpathy y Willison; léelo teniendo en cuenta esa diferencia.
- **[The Three Developer Loops: A New Framework for AI-Assisted Coding](https://itrevolution.com/articles/the-three-developer-loops-a-new-framework-for-ai-assisted-coding/)** — Leah Brown sobre el marco de Gene Kim y Steve Yegge, IT Revolution, 2025-10-20. Los ciclos interno, intermedio y externo que adapta la columna vertebral de esta guía.

### Cómo trabajan los profesionales

- **[Just Talk To It: the no-bs Way of Agentic Engineering](https://steipete.me/posts/just-talk-to-it)** — Peter Steinberger, 2025-10-14. Prompts cortos, radio de impacto, commits atómicos en una sola carpeta y unas 800 líneas de `AGENTS.md` escritas por el agente.
- **[Shipping at Inference-Speed](https://steipete.me/posts/2025/shipping-at-inference-speed)** — Peter Steinberger, 2025-12-28. Diseño CLI primero para que los agentes cierren el ciclo, por qué evita los worktrees (y su aviso de que eso no funciona en equipos grandes) y el modo plan como un "apaño".
- **[My Current AI Dev Workflow](https://steipete.me/posts/2025/optimal-ai-development-workflow)** — Peter Steinberger, 2025-08-25. Un flujo anterior basado en el modo plan; útil para ver cómo cambian los consejos con cada generación de modelos.
- **[Just One More Prompt](https://steipete.me/posts/just-one-more-prompt)** — Peter Steinberger, 2025-08-19. Un relato honesto del efecto "tragaperras" de los agentes y de lo que le hace al sueño.
- **[Promoting AI agents](https://world.hey.com/dhh/promoting-ai-agents-3ee04945)** — David Heinemeier Hansson, 2026-01-07. Su postura antes del cambio: lejos de que los agentes escribieran la mayor parte de su código.
- **[Let the agents democratize open source](https://world.hey.com/dhh/let-the-agents-democratize-open-source-9fd630a9)** — David Heinemeier Hansson, 2026-06-01. Argumenta en contra de prohibir las contribuciones con IA, aunque admite que el slop es un problema.
- **[Hilo en X sobre su configuración](https://x.com/bcherny/status/2007179832300581177)** — Boris Cherny, creador de Claude Code, 2026-01-02. Una configuración "sorprendentemente normal": sesiones en paralelo, modo plan primero y darle al agente una forma de verificar su trabajo.
- **[Hilo en X con consejos del equipo de Claude Code](https://x.com/bcherny/status/2017742741636321619)** — Boris Cherny, 2026-01-31. Los worktrees como la mayor mejora de productividad, un segundo agente que revisa los planes y actualizar `CLAUDE.md` después de cada corrección.
- **[Anthropic's Claude Code creator says he manages tens of thousands of AI agents at once](https://fortune.com/2026/06/08/anthropics-boris-cherny-creator-of-claude-code-says-there-are-days-he-manages-tens-of-thousands-of-ai-agents-at-once/)** — Fortune, 2026-06-08. Cifras de escala de alguien de dentro con tokens prácticamente ilimitados; sirve de contexto, no de objetivo.
- **[My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey)** — Mitchell Hashimoto, 2026-02-05. Un contrapeso sólido: un agente cada vez, notificaciones desactivadas y "harness engineering" después de cada error.
- **[Embracing the parallel coding agent lifestyle](https://simonwillison.net/2025/Oct/5/parallel-coding-agents/)** — Simon Willison, 2025-10-05. Qué tareas se paralelizan bien, y por qué el límite real es revisar un cambio importante cada vez.
- **[The Code Agent Orchestra: what makes multi-agent coding work](https://addyosmani.com/blog/code-agent-orchestra/)** — Addy Osmani, 2026-03-26. De director a orquestador: subagentes, equipos de agentes y agentes en la nube, con la descomposición y la verificación como cuellos de botella.
- **[Gas Town](https://yegge.ai/gastown)** — Steve Yegge, 2026-01. Un extremo experimental: orquestar decenas de agentes con una cola de merge. Útil para ver dónde está el techo, no como punto de partida.
- **[My LLM codegen workflow atm](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/)** — Harper Reed, 2025-02-16. La entrevista de especificación con una pregunta cada vez, y después un plan y pasos pequeños con tests.
- **[Agentic Coding Recommendations](https://lucumr.pocoo.org/2025/6/12/agentic-coding/)** — Armin Ronacher, 2025-06-12. Stacks simples, herramientas rápidas, logs que los agentes pueden leer y saltarse permisos solo dentro de un contenedor.
- **[How to Build an Agent](https://ampcode.com/notes/how-to-build-an-agent)** — Thorsten Ball, 2025-04-15. Un agente es un modelo, un bucle y unas pocas herramientas en unos cientos de líneas; la mejor forma de desmitificar lo que estás usando.

### Verificación, revisión y seguridad

- **[The lethal trifecta for AI agents: private data, untrusted content, and external communication](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)** — Simon Willison, 2025-06-16. Datos privados, contenido no confiable y comunicación externa juntos hacen posible la filtración de datos.
- **[Ralph Wiggum as a "software engineer"](https://ghuntley.com/ralph/)** — Geoffrey Huntley, 2025-07-14. La técnica original de "ejecutar el mismo prompt en bucle", con los tests y los tipos como contrapresión.
- **[Superpowers: How I'm using coding agents in October 2025](https://blog.fsck.com/2025/10/09/superpowers/)** — Jesse Vincent, 2025-10-09. Una librería de skills que impone lluvia de ideas, plan, worktrees, TDD y revisión entre tareas: un proceso más pesado que merece la pena comparar con el nuestro.
- **[Agentic Code Review](https://addyosmani.com/blog/agentic-code-review/)** — Addy Osmani, 2026-06-15. Revisión por niveles según el riesgo, pedir evidencia primero, examinar los tests reescritos; el merge es cosa de personas.
- **[How Anthropic secures its AI-native software development lifecycle](https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle)** — Jason Clinton, Anthropic, 2026-07-21. Agentes revisores con alcance limitado, revisión humana ponderada por riesgo, identidades de agente con mínimos privilegios. Un proveedor describiéndose a sí mismo.
- **[S1ngularity: What Happened, How We Responded, What We Learned](https://nx.dev/blog/s1ngularity-postmortem)** — Nx, 2025-08 (con el [análisis de Wiz](https://www.wiz.io/blog/s1ngularity-supply-chain-attack)). Un ataque a la cadena de suministro que usó las CLI de IA instaladas con flags para saltarse los permisos y buscar secretos.
- **[How we built Claude Code auto mode: a safer way to skip permissions](https://www.anthropic.com/engineering/claude-code-auto-mode)** — Anthropic Engineering, 2026-03-25. Por qué el cansancio de aprobar convierte las confirmaciones manuales en una protección débil, y los límites de un clasificador.
- **[Making Claude Code more secure and autonomous with sandboxing](https://www.anthropic.com/engineering/claude-code-sandboxing)** — Anthropic Engineering, 2025-10-20. Aislamiento de sistema de archivos y de red, y la reducción interna de las confirmaciones de permisos.

### Contexto, especificaciones y harnesses

- **[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)** — Anthropic Engineering, 2025-09-29. El contexto más pequeño y con más señal, recuperación justo a tiempo, compactación, notas y subagentes.
- **[Building effective agents](https://www.anthropic.com/research/building-effective-agents)** — Anthropic, 2024-12-19. Empieza simple; el patrón evaluador-optimizador es el bucle escritor/revisor con otro nombre.
- **[How Anthropic teams use Claude Code](https://claude.com/blog/how-anthropic-teams-use-claude-code)** — Anthropic, 2025-07-24. Bucles autónomos para el trabajo periférico, supervisión cercana para la lógica central y empezar desde un estado de git limpio.
- **[Advanced Context Engineering for Coding Agents](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md)** — HumanLayer, 2025-08. Investigar, planificar e implementar con compactación intencionada; revisar con más dureza la investigación y los planes.
- **[12-Factor Agents](https://github.com/humanlayer/12-factor-agents)** — HumanLayer, repositorio vivo. Controla tu ventana de contexto; construye agentes pequeños y enfocados.
- **[Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)** — Birgitta Böckeler, martinfowler.com, 2025-10-15. Una mirada crítica a las herramientas de especificación primero y a la falsa sensación de control que pueden dar.
- **[Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)** — OpenAI, 2026-02-11 (resumen en [InfoQ](https://www.infoq.com/news/2026/02/openai-harness-engineering-codex)). Un `AGENTS.md` corto como índice, el repositorio como fuente de verdad y aplicación mecánica de las reglas. El experimento de un proveedor en un proyecto nuevo.

### Escribir y enseñar

- **[Patterns in confusing explanations](https://jvns.ca/blog/confusing-explanations/)** — Julia Evans, 2021-08-19. El estilo que sigue esta guía: primero ejemplos concretos, explicar el porqué, señalar los enfoques equivocados.

## Documentación oficial

Las páginas de herramientas (terminales, gestores de sesiones, sandboxes) están, con su contexto, en [Herramientas](tools.md). Todos estos son documentos vivos; la fecha es la de nuestra última comprobación.

### Claude Code (Anthropic), comprobado el 2026-09-17

- [Overview](https://code.claude.com/docs/en/overview), [Best practices](https://code.claude.com/docs/en/best-practices) y [Glossary](https://code.claude.com/docs/en/glossary): el flujo de trabajo oficial (explorar, planificar, implementar, commit), la verificación y la gestión del contexto.
- [Memory](https://code.claude.com/docs/en/memory): `CLAUDE.md`, importar `AGENTS.md` y la memoria automática.
- [Hooks](https://code.claude.com/docs/en/hooks), [Permission modes](https://code.claude.com/docs/en/permission-modes), [Sandboxing](https://code.claude.com/docs/en/sandboxing) y [Security](https://code.claude.com/docs/en/security): barreras de seguridad (guardrails) deterministas y autonomía segura.
- [Worktrees](https://code.claude.com/docs/en/worktrees), [Agent view](https://code.claude.com/docs/en/agent-view), [Agent teams](https://code.claude.com/docs/en/agent-teams), [Subagents](https://code.claude.com/docs/en/sub-agents) y [Sessions](https://code.claude.com/docs/en/sessions): trabajo en paralelo.
- [Non-interactive mode](https://code.claude.com/docs/en/headless), [Goal](https://code.claude.com/docs/en/goal) y [Routines](https://code.claude.com/docs/en/routines): ejecuciones sin supervisión.
- [Code Review](https://code.claude.com/docs/en/code-review) y [GitHub Actions](https://code.claude.com/docs/en/github-actions): revisión automática de pull requests.
- [Costs](https://code.claude.com/docs/en/costs): gasto típico y formas prácticas de reducir el consumo de tokens.

### Codex (OpenAI), comprobado el 2026-09-17

- [Best practices](https://learn.chatgpt.com/guides/best-practices): estructura del prompt (objetivo, contexto, restricciones, cuándo está terminado), un `AGENTS.md` corto, planificación y revisión.
- [Codex CLI](https://learn.chatgpt.com/docs/codex/cli), [comandos y opciones](https://learn.chatgpt.com/docs/developer-commands?surface=cli) y [Non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode).
- [AGENTS.md en Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md): cómo se descubren y combinan los archivos de instrucciones.
- [Code review](https://learn.chatgpt.com/docs/code-review) y [Review GitHub pull requests with Codex](https://learn.chatgpt.com/docs/third-party/github).
- [Sandbox](https://learn.chatgpt.com/docs/sandboxing) y [Permissions](https://learn.chatgpt.com/docs/permission-modes).

### Estándares y otras herramientas

- [AGENTS.md](https://agents.md/) — Agentic AI Foundation (Linux Foundation). El formato abierto para instrucciones de agentes.
- [Model Context Protocol](https://modelcontextprotocol.io/) — el estándar abierto para conectar aplicaciones de IA con herramientas y datos.
- [Agents in VS Code](https://code.visualstudio.com/docs/agents/overview), [Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent) y [Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review) — GitHub y Microsoft.
- [git worktree](https://git-scm.com/docs/git-worktree) — proyecto Git. La pieza sobre la que se construyen todas las herramientas de sesiones en paralelo.
- [GitHub CLI](https://cli.github.com/) — GitHub. Cómo leen y escriben los agentes issues y pull requests desde la terminal.
- [Spec Kit](https://github.com/github/spec-kit) — GitHub; y [Kiro specs](https://kiro.dev/docs/specs/) — Kiro. Flujos guiados por especificaciones con una aprobación humana en cada fase, para comparar.

## Investigación y datos

- **[Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)** — METR, 2025-07-10. En un ensayo aleatorizado, desarrolladores con experiencia fueron un 19 % más lentos con IA mientras creían ir más rápido. Lee los límites que el propio METR pone a lo que demuestra.
- **[We are Changing our Developer Productivity Experiment Design](https://metr.org/blog/2026-02-24-uplift-update/)** — METR, 2026-02-24. El seguimiento apunta a una aceleración, pero METR lo califica de evidencia muy débil, en parte porque hubo desarrolladores que se negaron a trabajar sin IA.
- **[Task Substitution and Uplift](https://metr.org/blog/2026-05-08-task-substitution-and-uplift/)** — METR, 2026-05-08. La gente se desplaza hacia las tareas que la IA abarató, así que la aceleración por tarea exagera el valor.
- **[Measuring the Self-Reported Impact of Early-2026 AI on Technical Worker Productivity](https://metr.org/blog/2026-05-11-ai-usage-survey/)** — METR, 2026-05-11. Una encuesta a 349 trabajadores; útil y declaradamente autoinformada.
- **[State of AI-assisted Software Development 2025](https://dora.dev/dora-report-2025/)** — DORA (Google Cloud), 2025-09-23. La IA amplifica lo que ya es un equipo: más volumen de entrega y menos estabilidad si no hay buenas prácticas.
- **[The AI Productivity Paradox Research Report](https://www.faros.ai/blog/ai-software-engineering)** — Faros AI, 2025-07-23. Más PR mergeados, pero revisiones mucho más largas y PR más grandes; datos de un proveedor, correlacionales.
- **[Adoption and Impact of Command-Line AI Coding Agents: A Study of Microsoft's Early 2026 Rollout of Claude Code and GitHub Copilot CLI](https://arxiv.org/abs/2607.01418)** — Emerson Murphy-Hill et al. (Microsoft), preprint en arXiv, 2026-07-01. La adopción se extendió entre compañeros; quienes adoptaron mergearon alrededor de un 24 % más de PR durante cuatro meses. El número de PR no es valor.
- **[Stack Overflow Developer Survey 2025: AI](https://survey.stackoverflow.co/2025/ai)** — Stack Overflow, 2025. "Casi bien, pero no del todo" es la mayor frustración de los desarrolladores con lo que produce la IA.
- **[Cost per Shipped Outcome: The Engineering Metric That Makes the AI Budget Conversation Make Sense](https://larridin.com/blog/cost-per-shipped-outcome-engineering-metric)** — Larridin, artículo de proveedor sin fecha. La definición de coste por resultado aceptado, con la advertencia de que más bajo no es automáticamente mejor.
- **[A First Look at Coding Agents' Compliance with AI Contribution Rules in Open-Source Communities](https://arxiv.org/abs/2607.26819)** — Wenhao Yang et al., preprint en arXiv, 2026-07-29. Los agentes casi nunca consultan por su cuenta las reglas de contribución, y por eso nuestro `AGENTS.md` repite nuestra política de IA.
- **["We Permit the Use of AI, but \[...\]": The Landscape of AI Policies in Popular Open Source Projects](https://arxiv.org/abs/2609.07542)** — Andre Hora et al., preprint en arXiv, 2026-09-07. 281 políticas: la mayoría permite la IA con condiciones, y muchas exigen declararla.

## Cursos

- **[Agentic Coding](https://missing.csail.mit.edu/2026/agentic-coding/)** — MIT, The Missing Semester of Your CS Education, 2026. Una clase universitaria sobre el mismo tema, con ejercicios.
- **[Claude Code: A Highly Agentic Coding Assistant](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant)** — DeepLearning.AI, en colaboración con Anthropic. Un curso práctico y breve sobre una herramienta.
- **[Anthropic Academy](https://anthropic.skilljar.com/)** — Anthropic. Los cursos de Anthropic sobre Claude y Claude Code.
- **[Practical Deep Learning for Coders](https://course.fast.ai/)** — fast.ai. El enfoque de enseñar primero "el juego completo" en el que se basa nuestro laboratorio 0.
- **[Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)** y **[AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)** — Microsoft. Lecciones numeradas con un esqueleto fijo y preguntas de comprobación, una estructura que tomamos prestada.
- **[Episode Structure](https://carpentries.github.io/sandpaper-docs/episodes.html)** y **[Live Coding is a Skill](https://carpentries.github.io/instructor-training/17-live.html)** — The Carpentries. Minutos por episodio, ideas clave y técnicas de workshop que usa nuestra guía para facilitadores.

## Políticas de código abierto y práctica de la comunidad

### Políticas sobre contribuciones con IA

- **[AI_POLICY.md](https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md)** — Ghostty. Una política breve y explícita; compárala con [nuestra propia política de IA](../../../AI_POLICY.es.md).
- **[LLVM AI Tool Use Policy](https://llvm.org/docs/AIToolPolicy.html)** — LLVM. Una persona en el bucle, un trailer `Assisted-by:` y el rechazo de las "contribuciones extractivas".
- **[AI Coding Assistants](https://docs.kernel.org/process/coding-assistants.html)** — documentación del kernel de Linux. Los agentes no pueden añadir `Signed-off-by`; la asistencia se declara con `Assisted-by:`.
- **[Policy on AI-Assisted Contributions](https://docs.fedoraproject.org/en-US/council/policy/ai-contribution-policy/)** — Fedora Council, 2025-10. Una política para todo el proyecto: quien contribuye responde de todo lo que envía, y el uso sustancial de IA se declara.
- **[On AI use in curl](https://curl.se/dev/contribute.html#on-ai-use-in-curl)** — curl. Declarar la asistencia de IA, mantener el nivel de calidad y esperar una expulsión si inventas informes.
- **[Use of AI-generated content](https://www.qemu.org/docs/master/devel/code-provenance.html#use-of-ai-generated-content)** — QEMU. El extremo restrictivo del espectro: rechaza las contribuciones generadas con IA porque no se puede certificar su licencia.
- **[open-source-ai-contribution-policies](https://github.com/melissawm/open-source-ai-contribution-policies)** — cuenta de GitHub melissawm, catálogo vivo. Muchas más políticas de proyectos sobre contribuciones generadas con IA, para comparar.

### Hacia dónde vamos (apéndice)

- **[Facility](https://github.com/theam/facility)** — The Agile Monkeys, código abierto. Herramientas autoalojadas para ejecutar agentes de programación dentro de un proceso de entrega revisable. No lo necesitas para aplicar esta guía; el [apéndice](../appendix/where-we-are-heading.md) explica dónde encaja.

### Cómo está construida esta guía

- **[Limina](https://github.com/theam/limina)** — The Agile Monkeys, código abierto. El harness de investigación del que nació nuestro repositorio de misión.
- **[Diátaxis](https://diataxis.fr/)** — Daniele Procida. Tutoriales, guías prácticas, referencia y explicación como tipos de contenido separados.
- **[The Turing Way](https://github.com/the-turing-way/the-turing-way)** — comunidad The Turing Way. Un manual comunitario con contenido CC BY, código MIT y comprobaciones en CI.
- **[The Rust Programming Language](https://doc.rust-lang.org/book/)** — proyecto Rust. Capítulos de conceptos más capítulos de proyecto, y ejemplos marcados de código que no funciona.
- **[javascript.info](https://javascript.info/)** — Ilya Kantor y colaboradores. Ejercicios con solución, y traducciones que se reservan mediante issues de seguimiento.
- **[Hello Algo](https://github.com/krahets/hello-algo)** — krahets y colaboradores. Traducciones redactadas con IA y revisadas por hablantes nativos en precisión y fluidez.
- **[Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/)** — Google. Los principios antes que las prácticas, y una parte final sobre equipos.
- **[Localizing Kubernetes documentation](https://kubernetes.io/docs/contribute/localization/)** y **[Human-Centered Automation for Kubernetes Localization in the AI Era](https://www.kubernetes.dev/blog/2026/06/26/human-centered-automation-kubernetes-localization-ai-era/)** — Kubernetes, 2026-06-26 el artículo del blog. Árboles de contenido paralelos por idioma, con el inglés como fuente de verdad.
- **[Lunaria](https://lunaria.dev/)** y **[Starlight internationalization](https://starlight.astro.build/guides/i18n/)** — Lunaria y Astro. Seguimiento del estado de las traducciones, y un posible sitio web futuro para esta guía.
- **[Contributor Covenant 3.0](https://www.contributor-covenant.org/version/3/0/code_of_conduct/)** — Organization for Ethical Source. Nuestro código de conducta.
- **[Syntax for issue forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms)** y **[contributions under repository license](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service#6-contributions-under-repository-license)** — GitHub. Cómo funcionan nuestros formularios de issues, y por qué la licencia "inbound = outbound" hace innecesario un CLA.
- **[Creative Commons FAQ](https://creativecommons.org/faq/)** — Creative Commons. Por qué la prosa es CC BY y el código usa una licencia de software.
- **[markdownlint-cli2-action](https://github.com/DavidAnson/markdownlint-cli2-action)** — David Anson; y **[lychee-action](https://github.com/lycheeverse/lychee-action)** — lychee. Las comprobaciones de estilo Markdown y de enlaces de nuestra CI.
