---
title: "Hacia dónde vamos"
kind: appendix
last_reviewed: 2026-09-17
---

# Hacia dónde vamos

Este apéndice es distinto del resto de la guía. Trata de la dirección en la que The Agile Monkeys está llevando esta práctica, incluidos dos proyectos que estamos construyendo.

> [!IMPORTANT]
> **No necesitas ninguno de los dos proyectos para aplicar esta guía.** Todo lo que hay en los módulos 00–10 funciona con una terminal, git, un agente de programación y un plan de pago. También existen otros enfoques, y enumeramos algunos al final.

## La práctica de esta guía funciona en portátiles

Repasa lo que la guía te ha pedido montar:

- terminales y un gestor de sesiones, con las sesiones agrupadas por pista de trabajo (track);
- repositorios locales y git worktrees, uno por pista;
- una base de conocimiento (knowledge base) de archivos Markdown en un repositorio git, que carga cada sesión;
- hooks y validadores que se ejecutan en tu máquina;
- bucles de revisión que llevas desde tus propias sesiones;
- una suscripción por persona, a veces dos.

Es un buen punto de partida. Es barato, todo es texto plano en git, puedes inspeccionar cada pieza y deshacer cualquiera de ellas. Para una persona, o para un equipo pequeño, puede que sea todo lo que vayas a necesitar.

## Dónde llega a sus límites

Cuando usamos esta práctica cada día en un equipo, aparecen una y otra vez los mismos límites:

- **Una sola máquina.** Los stacks locales completos agotan la memoria de un portátil hacia los cinco o seis (módulo 06). Cuando el portátil se suspende, las sesiones se paran. Después de un reinicio, averiguar qué estaba haciendo cada sesión es lento y propenso a errores.
- **La atención de una sola persona.** Las sesiones informan a quien las lanzó. Nadie más del equipo puede ver tus pistas en curso ni dirigir una mientras no estás. Un traspaso necesita un paquete de traspaso.
- **Contexto que vive en un repositorio.** La base de conocimiento es un repositorio git que el resto del equipo tiene que clonar y consultar con sus propios agentes. Las transcripciones de reuniones, los documentos y las decisiones solo entran cuando alguien los mete.
- **Difícil de compartir.** Las skills, las reglas y las guardas se copian de un repositorio a otro y acaban divergiendo.
- **Difícil de auditar.** La evidencia existe, pero está repartida entre logs de sesiones locales, hilos de PR, ejecuciones de CI y el chat. Responder a "¿quién aceptó este plan, qué modelo escribió este cambio y cuánto costó?" es arqueología. Es la pregunta de los sectores regulados del módulo 09.
- **Credenciales junto a los agentes.** Las sesiones en un portátil se ejecutan al lado de las credenciales de la persona, que es justo la situación que aprovechó el ataque s1ngularity (módulo 09).
- **Cuentas pensadas para una persona.** Las suscripciones y los límites de uso son por persona, y la gente descubre que una máquina está preparada para una sola cuenta (módulo 08).

Ninguno de estos límites impide que una persona trabaje así. Son lo que estorba cuando un equipo quiere compartir contexto, ver el trabajo en curso y demostrar qué pasó.

## Dirección 1: la base de conocimiento en la nube

**ProductPlot** (productplot.ai) está en desarrollo. Es una base de conocimiento de producto compartida que conecta el material de origen, las decisiones y la planificación de la entrega. Los agentes de cada persona la leen y la mantienen a través de MCP. Los agentes y las suscripciones de esta guía siguen haciendo el trabajo, pero el conocimiento vive en un único sitio compartido y no en un repositorio por persona o por equipo.

Apunta a dos de los límites de arriba: el contexto que vive en un repositorio y el conocimiento difícil de compartir en un equipo.

Está en una fase temprana. No enumeramos funcionalidades aquí porque todavía están cambiando. Cuando haya algo que puedas probar, este apéndice lo dirá.

## Dirección 2: la ejecución de agentes en la nube

**[Facility](https://github.com/theam/facility)** es una herramienta open source (Apache 2.0) y autoalojada para ejecutar agentes de programación dentro de un proceso de entrega revisable. Su repositorio la describe en detalle. En resumen:

- Conectas repositorios de GitHub, y sus issues se convierten en **stories**.
- Una story es una unidad de trabajo duradera. Tiene una conversación compartida que continúan personas y agentes, un espacio de trabajo persistente con el entorno de desarrollo que declara el repositorio, sesiones de Claude Code o Codex que se pueden reanudar, y una rama y un pull request normales.
- **Los agentes se definen en el repositorio** como archivos Markdown: prompt, motor, modelo y disparadores (manual, la aplicación web, MCP, eventos de GitHub o una programación horaria). El conjunto inicial cubre roles de entrega: arquitecto, constructor, revisor de PR, agente que atiende la revisión, doctor de CI y auditoría de seguridad.
- Las personas dirigen la conversación y prueban el resultado en funcionamiento a través de previsualizaciones autenticadas. Los agentes entregan con ramas y pull requests normales. **Los puntos de control del propio repositorio siguen siendo la frontera:** ramas protegidas, CI obligatoria, revisiones obligatorias y una decisión humana de mergear.
- Cada turno de un agente registra el agente, el modelo, la sesión y el estado de Git antes y después, enlazado con los PR, revisiones y comprobaciones resultantes. Los costes se atribuyen por proyecto y por agente, y los presupuestos mensuales de cada proyecto se comprueban antes de nuevas llamadas al modelo.

Así encaja con la guía. Los worktrees y los malabares con sesiones del módulo 06 pasan a ser espacios de trabajo persistentes que no dependen de un portátil. Los puntos de control humanos del módulo 09 se quedan en el repositorio. El coste por PR mergeado (módulo 08) y la evidencia para auditoría (módulo 09) se registran mientras ocurre el trabajo, en lugar de reconstruirse después.

Lo que deberías saber antes de mirarlo:

- **Es anterior a la 1.0.** Su esquema, sus APIs, los manifiestos de agentes y la forma de desplegarlo pueden cambiar entre versiones `0.x`, y no se promete un camino de actualización entre ellas.
- **Tiene poco recorrido en producción.** En sus propias palabras: «Facility gestiona la entrega del equipo que lo construye, y de nadie más todavía.» ([README de Facility](https://github.com/theam/facility#readme), traducción propia)
- **Su modelo de confianza es un compromiso deliberado.** Todos los agentes tienen el mismo acceso de nivel maintainer a su espacio de trabajo y a los repositorios del proyecto. No hay perfiles de permisos por agente, y la frontera son los controles de merge. Es la opción de "un único modelo de confianza" del módulo 09, no la de identidades por agente con mínimos privilegios. Su README aconseja usarlo en repositorios «donde un pull request malo de un agente sea una molestia y no un incidente» (traducción propia), y leer su modelo de seguridad y sus notas de endurecimiento antes de nada más.
- **Lo operas tú.** Autoalojarlo significa mantener su base de datos, sus workers, su GitHub App y sus imágenes de espacio de trabajo.

## Lo que no cambia al pasar a la nube

Ninguno de los dos proyectos sustituye a la práctica. Sigues necesitando issues que funcionen como prompts, comprobaciones que un agente pueda ejecutar, trabajo dividido en pistas, revisiones que se cierran por decisión y personas en los puntos de control. Sacar la ejecución o el conocimiento de un portátil cambia dónde se ejecutan las cosas y quién puede verlas. No convierte una práctica floja en una sólida. Como dice el [informe DORA 2025](https://dora.dev/dora-report-2025/) de la IA en general, amplifica lo que ya hay, sea bueno o malo.

## Otros caminos

- **Agentes alojados por los proveedores.** Los principales proveedores de agentes de programación ofrecen sesiones en la nube, tareas en segundo plano y agentes programados o disparados por eventos. La [referencia de herramientas](../reference/tools.md) enumera lo que usamos y enlaza la documentación oficial.
- **Agentes en tu propia CI.** Ejecuta un agente en modo headless (no interactivo) ante eventos de issues o pull requests, por ejemplo con [Claude Code GitHub Actions](https://code.claude.com/docs/en/github-actions), y conserva tus puntos de control actuales.
- **Orquestadores y gestores de sesiones open source.** Varias herramientas gestionan por ti los worktrees y las sesiones en paralelo (módulo 06).
- **Esperar.** [DHH espera que los grandes laboratorios absorban la mayor parte de esto](https://lexfridman.com/dhh-2-transcript): «No todos vamos a tener que construir nuestros propios arneses de coordinación.» (traducción propia). Puede que tenga razón, y es un buen motivo para no construir el tuyo salvo que lo necesites.
- **Quedarte en portátiles.** Para personas y equipos pequeños, la práctica de esta guía es suficiente.

## Ayúdanos a hacerlo bien

Construimos en abierto porque preferimos que nos corrijan pronto. Si te has topado con estos límites y los has resuelto de otra forma, o crees que los hemos trazado mal, [cuéntanoslo](../../../CONTRIBUTING.es.md). Los comentarios sobre Facility son bienvenidos en [su gestor de issues](https://github.com/theam/facility/issues).
