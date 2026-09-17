---
title: "Del chatbot al sistema"
module: 1
kind: lesson
minutes: 45
level: foundation
last_reviewed: 2026-09-17
---

# 1. Del chatbot al sistema

> **En una frase:** el agentic engineering no es un prompt mejor, sino un sistema que diseñas (contexto, descomposición, verificación, revisión y decisiones) para que los agentes escriban la mayor parte del código sin bajar el listón de calidad.

## Lo que serás capaz de hacer

- Definir el agentic engineering y distinguirlo del autocompletado y del vibe coding, incluido dónde personas respetadas usan estas palabras de forma distinta.
- Reconocer en tus propios hábitos el techo de "una ventana, un prompt, una tarea", y nombrar la pieza que falta detrás de cada síntoma.
- Describir cómo cambia el papel de quien programa, de escribir líneas a diseñar y editar un sistema, y qué sigue siendo humano.
- Leer con espíritu crítico los estudios de productividad: qué midieron METR, DORA, Faros AI y Microsoft, y qué no.
- Medir tu propio punto de partida, para poder saber más adelante si algo ha cambiado.

## Por qué importa

Piensa en alguien que adoptó un agente de programación hace seis meses. Las primeras semanas fueron emocionantes: el código repetitivo desapareció y los bugs pequeños se resolvían en minutos. Después, el progreso se estancó.

Hoy su día es así. Abre una ventana nueva y pega el mismo párrafo de contexto del proyecto. Mira cómo trabaja el agente. Ejecuta los tests en persona, porque la última vez que el agente dijo "todos los tests pasan" no los había ejecutado. Los diffs han crecido, así que las revisiones tardan más. Tiene la sensación de ir más rápido. No tiene claro que sea así.

Eso no lo arregla un modelo mejor ni un prompt más ingenioso. Lo que falta está fuera de la caja del prompt: un lugar donde viva el conocimiento del proyecto, una forma de que el agente compruebe su propio trabajo, un trabajo dividido para que varias tareas avancen a la vez y una revisión que no dependa de leer cada línea. Este módulo le pone nombre a ese cambio y mira con honestidad la evidencia.

## Tres formas de trabajar con un agente de programación

| | Autocompletado | Chatbot | Sistema |
|---|---|---|---|
| Quién escribe el código | Tú, con sugerencias | El agente, petición a petición | Agentes, en varias pistas a la vez |
| Tu trabajo principal | Escribir y aceptar | Escribir prompts, esperar, leer diffs | Diseñar el contexto, dividir el trabajo, decidir, revisar |
| Unidad de trabajo | Una línea o una función | Un prompt | Una pista que termina en un pull request mergeado |
| Quién verifica | Tú | Normalmente tú | Primero el agente, con comprobaciones que tú diseñas; después otro agente; y tú, donde importa |
| Dónde vive la memoria | En tu cabeza | En el chat, hasta que lo cierras | En archivos del repositorio que carga cada sesión |
| Dónde se rompe | Lento para cambios grandes | Te conviertes en el cuello de botella y en la memoria | Se multiplica cualquier debilidad de verificación o de contexto |

Definimos el **agentic engineering** (ingeniería agéntica) como la ingeniería de software en la que los agentes escriben la mayor parte del código y las personas diseñan el sistema que los rodea: el contexto con el que trabajan, cómo se descompone el trabajo, cómo se verifican y revisan los resultados y qué decisiones siguen siendo humanas.

Hay dos cosas que esta definición deja fuera a propósito. No dice cuántos agentes usas: un solo agente bien llevado ya es agentic engineering. Y no dice que dejes de leer código: dice que decides, según el riesgo, qué merece tu lectura.

## Qué significan las palabras y quién no está de acuerdo

El vocabulario es nuevo y cada cual lo usa a su manera. Vas a leer todos estos términos, así que conviene saber quién quiere decir qué.

**Vibe coding.** [Andrej Karpathy](https://karpathy.bearblog.dev/sequoia-ascent-2026/) acuñó el término a principios de 2025 para referirse a construir software a base de prompts sin preocuparse por el código. [DHH](https://lexfridman.com/dhh-2/) da la definición más nítida que conocemos:

> «No miras la implementación. Eso, para mí, es lo que separa el vibe coding de programar» — DHH en [Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/) (traducción propia)

**Agentic engineering.** A principios de 2026, Karpathy [propuso "agentic engineering"](https://x.com/karpathy/status/2019137879310836075) para el trabajo profesional con agentes y más supervisión. En una charla posterior separó los dos términos así:

> «El agentic engineering consiste en preservar el listón de calidad del software profesional.» — Andrej Karpathy, [Sequoia Ascent 2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/) (traducción propia)

[Simon Willison](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/) usa el término para el desarrollo de software con agentes de programación, es decir, agentes que ejecutan herramientas en bucle, y traza la línea en si el autor ha llevado el código a un nivel apto para producción. [Addy Osmani](https://addyosmani.com/blog/agentic-engineering/) lo resume en una línea: «la IA hace la implementación; la persona es responsable de la arquitectura, la calidad y la corrección» (traducción propia).

**Augmented coding.** [Kent Beck](https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes) usa otro nombre para una idea parecida: «En el augmented coding te importa el código, su complejidad, los tests y su cobertura» (traducción propia).

**Vibe coding, el otro significado.** El libro [*Vibe Coding*](https://itrevolution.com/product/vibe-coding-book/) de Gene Kim y Steve Yegge usa "vibe coding" para el trabajo profesional y disciplinado con IA, algo muy parecido a lo que todos los anteriores llaman agentic engineering. [Peter Steinberger](https://lexfridman.com/peter-steinberger-transcript/) va en la dirección contraria y dice que "vibe coding" es un insulto.

Así que, cuando alguien diga "vibe coding", comprueba qué significado le da antes de estar de acuerdo o en desacuerdo. En esta guía, "vibe coding" es la definición de DHH: nadie mira la implementación. "Agentic engineering" es el sistema descrito arriba.

> [!IMPORTANT]
> La línea que importa no es cuánto código escribe el agente. Es si alguien ha diseñado una forma de fiarse del resultado. Lo dice una frase que Karpathy cita y a la que vuelve una y otra vez: «Puedes externalizar tu pensamiento, pero no puedes externalizar tu comprensión» (traducción propia).

## El techo de adopción

La mayoría de quienes adoptan un agente se quedan en la fase de chatbot. No es pereza. La fase de chatbot compensa enseguida, así que nada duele lo suficiente como para empujarte más allá, y cada paso siguiente cambia algo *fuera* del prompt: tests que el agente puede ejecutar, una base de conocimiento (knowledge base), issues que una sesión nueva puede ejecutar, worktrees, una rutina de revisión. Cada una parece trabajo extra la semana en que la añades y compensa semanas después.

Los pocos que hacen esos cambios acumulan ventaja. Las correcciones se convierten en reglas de un archivo de instrucciones, las comprobaciones repetidas en scripts que ejecuta el agente y los flujos repetidos en skills. Su entorno mejora cada semana, mientras que quien usa el agente como chatbot empieza de cero en cada sesión. Por eso la brecha se abre en lugar de cerrarse.

> [!NOTE]
> **En The Agile Monkeys** vimos este techo dentro de nuestros propios equipos. Un puñado de ingenieros tiene muchas sesiones en paralelo sobre trabajo real; la mayoría sigue usando el agente como un chatbot. Nadie había puesto esas prácticas por escrito en un solo sitio, así que lo hicimos.

La adopción se extiende de persona a persona, no con anuncios: un [estudio amplio sobre el despliegue de Microsoft a principios de 2026](https://arxiv.org/abs/2607.01418) de Claude Code y GitHub Copilot CLI encontró que «el primer uso se difundió sobre todo a través de las redes de contactos» (traducción propia). Para que un equipo supere el techo, alguien tiene que enseñárselo, no solo contárselo.

### Diagnostica tu propio techo

| Síntoma | Qué falta | Dónde se enseña |
|---|---|---|
| Pegas el mismo contexto en cada sesión nueva | Un ciclo de contexto: archivos de instrucciones y una base de conocimiento | [Módulo 04](../04-context-is-infrastructure/README.md) |
| Ejecutas tú los tests después de que el agente diga "hecho" | Verificación que el agente ejecuta por su cuenta | [Módulo 03](../03-close-the-loop/README.md) |
| Escribes largos "prompts perfectos" | Contexto y conversación, no más palabras | [Módulo 02](../02-one-agent-done-well/README.md) |
| Miras cómo trabaja el agente porque no tienes otra cosa que hacer | Trabajo descompuesto en pistas de trabajo (tracks) independientes | [Módulos 05](../05-decompose-into-tracks/README.md) y [06](../06-run-sessions-in-parallel/README.md) |
| Lees cada diff línea a línea con la misma atención | Revisión escalonada por riesgo, con agentes que revisan primero | [Módulo 07](../07-agents-review-agents/README.md) |
| Llegas a los límites del plan y no sabes qué compraron esos tokens | Una visión de coste por resultado | [Módulo 08](../08-token-economics/README.md) |

## La práctica está convergiendo

Personas que no trabajan juntas están llegando a una forma de trabajar parecida. Los detalles y los matices cambian; la forma se repite.

- **DHH** ([Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/)) trabaja con agentes desde herramientas de terminal, hace que el modelo de un proveedor escriba y el de otro revise («Es mi revisor favorito. No para de encontrar cosas», traducción propia) y se reserva la decisión final. Sus matices importan igual: sigue revisando la forma de todo el código y las líneas concretas de las partes críticas, encuentra los productos grandes «sorprendentemente difíciles de acelerar del todo con agentes» (traducción propia) y reconoce que su ritmo «no es sostenible en absoluto» (traducción propia).
- **Peter Steinberger** ([The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code)) trabaja con cinco a diez agentes en un proyecto que lleva casi en solitario, y nombra la idea central: «tienes que cerrar el ciclo. Tiene que poder depurarse y probarse a sí mismo» (traducción propia). Su matiz, sobre tener todos sus agentes en una misma carpeta: «Normalmente trabajo solo; si trabajas en un equipo más grande, ese flujo obviamente no funcionará» ([Shipping at Inference-Speed](https://steipete.me/posts/2025/shipping-at-inference-speed), traducción propia).
- **Andrej Karpathy** explica por qué la verificación es la palanca: «los LLM y el aprendizaje por refuerzo automatizan lo que puedes verificar» ([Sequoia Ascent 2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/), traducción propia).
- **Simon Willison** está recopilando los patrones en abierto, desde red/green TDD hasta subagentes, en su guía [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/).
- **La guía de los proveedores** coincide. [Las buenas prácticas de Claude Code](https://code.claude.com/docs/en/best-practices) empiezan con "Give Claude a way to verify its work" (dale a Claude una forma de verificar su trabajo) y describen una separación entre quien escribe y quien revisa con contexto limpio. [Las buenas prácticas de Codex](https://learn.chatgpt.com/guides/best-practices) recomiendan planificar el trabajo complejo, un AGENTS.md corto y preciso, y worktrees para las tareas en paralelo.

Los elementos comunes encajan con esta guía: el agente verifica su propio trabajo (módulos 02–03), el contexto vive en el repositorio (04), el trabajo se divide en pistas aisladas (05–06), otro agente revisa (07) y las personas son responsables de las decisiones y de los merges (09).

Pero que los pioneros converjan es una señal, no una prueba. La mayoría de estas voces son de ingenieros con mucha experiencia, a menudo trabajando solos o en productos propios: un contexto más amable que el de un equipo grande con un código de diez años y normas de cumplimiento estrictas.

## De escribir líneas a diseñar el sistema

Cuando los agentes escriben la mayor parte del código, tu trabajo no desaparece. Se desplaza.

> «No tengo una comprensión del código línea a línea. Eso, eso es lo que Codex hace por mí, pero yo soy el arquitecto» — Peter Steinberger en [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code) (traducción propia)

DHH usa otra imagen: un maestro cuyo workshop de aprendices hace el cincelado mientras él dice cuándo las proporciones no están bien. Eso incluye decirles a los agentes algo que rara vez hacen por su cuenta: «de verdad tienes que decirles: "Hazlo más simple"» (traducción propia).

Lo que sigue siendo humano, en todos los relatos que nos parecen fiables:

- **El criterio de producto.** DHH: «Tienen un cuello de botella en las ideas. Tienen un cuello de botella en la visión. Tienen un cuello de botella en el gusto» (traducción propia).
- **La coherencia.** Muchos cambios de agentes, razonables uno a uno, pueden erosionar una arquitectura. El [módulo 09](../09-teams-and-organizations/README.md) muestra un caso real.
- **El diseño de la verificación y las decisiones en los puntos de control.** Qué significa "correcto"; quién acepta planes, hace merge y ejecuta comandos con privilegios.
- **La comprensión.** La suficiente para saber cuándo se equivoca el agente.

> [!NOTE]
> **En The Agile Monkeys**, quienes trabajan así describen su día como conversaciones, no como prompts. Planifican dentro de una sesión que ya contiene el contexto del proyecto, piden al agente que convierta el plan en issues y le piden que explique qué va a hacer antes de que arranque una tarea. Su tiempo se va en aceptar planes, decidir y revisar, no en escribir código.

Este cambio no es una buena noticia para todo el mundo. DHH lo dice sin rodeos: «lo vas a pasar mal para adaptarte a la nueva realidad si lo único que te gustaba de programar era la parte mecánica» (traducción propia). Steinberger descubrió lo contrario sobre sí mismo: «Siempre pensé que me gustaba programar, pero en realidad me gusta construir» (traducción propia). Mucha gente disfrutaba de las dos cosas, y el oficio sigue ahí cuando te apetece.

También cansa más de lo que parece. Willison dice que trabajar con varios agentes es «sorprendentemente eficaz, aunque agotador mentalmente» (traducción propia), y el [módulo 06](../06-run-sessions-in-parallel/README.md) trata la sostenibilidad como parte de la práctica.

## Qué dice la evidencia, con honestidad

El entusiasmo es fácil de encontrar; la evidencia sólida, no. Esto es lo que encontraron los estudios principales, con sus límites.

**METR, 2025: desarrolladores con experiencia fueron más lentos y creían ir más rápido.** En un [ensayo controlado aleatorizado](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), 16 desarrolladores de código abierto con experiencia hicieron 246 tareas reales en repositorios que conocían bien, con herramientas de principios de 2025. Cuando podían usar IA, tardaron un **19 % más**. Esperaban ir un 24 % más rápido y, al terminar, seguían creyendo que habían ido un 20 % más rápido. METR insiste en que esto no demuestra que la IA no acelere a la mayoría de los desarrolladores. Demuestra algo más limitado y más incómodo: su sensación sobre su propia velocidad estaba equivocada.

**METR, seguimiento de 2026: probablemente más rápidos ahora, pero el diseño del estudio se rompió.** En un [seguimiento](https://metr.org/blog/2026-02-24-uplift-update/), quienes repetían tardaron, según la estimación, un 18 % menos con IA (intervalo de confianza: del 38 % menos al 9 % más) y quienes participaban por primera vez, un 4 % menos (del 15 % menos al 9 % más). Las dos apuntan a una aceleración; ninguna es estadísticamente significativa. Los sesgos de selección fueron serios: algunos desarrolladores no quisieron participar porque no querían trabajar sin IA, entre el 30 % y el 50 % evitó enviar tareas para las que quería usar IA, y los tiempos no eran fiables en quienes usaban varios agentes a la vez. METR está rediseñando el estudio.

**DORA 2025: la IA amplifica lo que ya existe.** El [informe DORA](https://dora.dev/dora-report-2025/), con casi 5.000 profesionales de la tecnología, encontró que alrededor del 90 % usa IA y más del 80 % dice que le ha hecho más productivo, pero el 30 % confía poco o nada en el código generado por IA. La adopción de IA ya se asocia a un mayor ritmo de entrega, y sigue asociándose a más inestabilidad. En palabras de DORA: «El papel principal de la IA es el de amplificador: magnifica las fortalezas y las debilidades que ya tiene una organización» (traducción propia). Entre las capacidades que hacen que la IA compense incluye los lotes pequeños, un control de versiones sólido y datos internos accesibles para la IA.

**Faros AI 2025: las personas se aceleran, las organizaciones (todavía) no.** [Faros AI](https://www.faros.ai/blog/ai-software-engineering), un proveedor que analizó datos de más de 10.000 desarrolladores, encontró que los equipos con mucha adopción completaron un 21 % más de tareas e hicieron merge de un 98 % más de pull requests, mientras que el tiempo de revisión subió un 91 %, el tamaño de los PR un 154 % y los bugs por desarrollador un 9 %, sin una mejora significativa a nivel de empresa. Es correlacional y viene de un proveedor, pero el patrón es plausible: el cuello de botella se desplaza a la revisión.

**Microsoft 2026: más pull requests mergeados, de forma sostenida.** El [estudio sobre el despliegue de Microsoft](https://arxiv.org/abs/2607.01418) siguió a decenas de miles de ingenieros: quienes adoptaron las herramientas hicieron merge de aproximadamente un 24 % más de pull requests de los que habrían hecho sin ellas, de forma sostenida durante cuatro meses. La advertencia de los autores: «un PR mergeado no es lo mismo que el valor que aporta» (traducción propia). Es un preprint.

### Por qué los resultados no coinciden

- **El contexto.** METR 2025 estudió a expertos en repositorios grandes y maduros que conocían a fondo: donde las personas son más fuertes y más pesa el conocimiento implícito.
- **La época.** Karpathy observó que los agentes de programación «básicamente no funcionaban antes de diciembre y básicamente funcionan desde entonces» ([según cita Simon Willison](https://simonwillison.net/2026/Feb/26/andrej-karpathy/), traducción propia), refiriéndose a diciembre de 2025.
- **El entorno y la habilidad.** Un agente que puede ejecutar los tests y tiene contexto se comporta de forma muy distinta a uno que no, y alguien en sus primeras semanas no es alguien en su segundo año. Pocos estudios registran ninguna de las dos cosas.
- **Qué se mide.** El tiempo por tarea, los pull requests, los incidentes y el valor de negocio son cosas distintas. Las percepciones subjetivas son la medida más débil de todas.
- **El resto del sistema.** Las mejoras individuales se esfuman si la revisión, la CI y el despliegue no pueden absorber más cambios (Faros, DORA).

La lección práctica para ti: no te fíes de tu sensación de velocidad ni de la cifra titular de nadie, incluidas las nuestras. Mídete antes y después, con resultados. Eso es el [laboratorio 1](lab.md).

### Nuestras propias cifras, y por qué no son benchmarks

> [!NOTE]
> **En The Agile Monkeys**, en nuestra plataforma interna de operaciones, quienes trabajan como describe esta guía resuelven del orden de **cinco historias por persona al día**. El proyecto llegó a la **issue #1000 en unos tres meses**. Varios ingenieros llegan a los límites de **dos suscripciones del plan más alto, una por proveedor**, la mayoría de las semanas. *Estas cifras son orientativas, no benchmarks.*

Comparan peras con manzanas, y este es el motivo:

- Nuestras historias las escriben agentes, así que tienden a ser más pequeñas y numerosas que las escritas a mano. Contarlas nos favorece.
- Es una herramienta interna con un número limitado de usuarios, un contexto más amable que el de un producto público con requisitos estrictos de disponibilidad.
- No hay grupo de control.
- El uso de las suscripciones incluye revisión automática y mantenimiento de la base de conocimiento, no solo programación, y no todo fue útil. Ese gasto también hay que optimizarlo ([módulo 08](../08-token-economics/README.md)).

Tómalas como un punto de referencia de que esta forma de trabajar es posible, no como un objetivo.

## Otras formas de verlo

**"Con un agente basta."** [Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey) describe un camino cuidadoso (dejar el chatbot, reproducir tu propio trabajo con un agente, convertir cada error del agente en parte del entorno, tener siempre un agente en marcha), mantiene las notificaciones desactivadas porque «Cambiar de contexto es muy caro» (traducción propia) y no trabaja con varios agentes. [Simon Willison](https://simonwillison.net/2025/Oct/5/parallel-coding-agents/) solo puede centrarse en revisar e integrar un cambio importante a la vez. Los dos tienen razón sobre el coste: el trabajo en paralelo está limitado por la revisión y la atención, no por cuántos agentes puedes arrancar.

**"No persigas la vanguardia."** El consejo de DHH a quien vive con ansiedad: «No intentes anticipar nada. Te volverás literalmente loco» (traducción propia). También espera que los proveedores absorban la mayor parte de la orquestación a medida que la gente se construye hoy.

**Lo que hacemos nosotros.** Trabajamos con muchas sesiones, porque en nuestro trabajo la ventaja es real. Pero tratamos el paralelismo como el último paso, que se gana con verificación y contexto, y diseñamos el ciclo externo para proteger la atención humana. Si tus mediciones muestran que tu mejor configuración son dos sesiones, es un buen resultado, no un fracaso.

## Ojo con

- ❌ **Medir líneas de código o número de agentes.** DHH: «las líneas de código son una métrica estúpida en general» (traducción propia). ✅ Mide pull requests mergeados, tiempo de ciclo, retrabajo (pull requests mergeados que necesitaron un arreglo posterior o una reversión en 7 días), minutos humanos por pull request y coste por pull request mergeado.
- ❌ **Fiarte de tu sensación de velocidad.** Los desarrolladores de METR se equivocaron sobre su propia velocidad en unos 40 puntos. ✅ Registra una semana real antes de cambiar nada.
- ❌ **Escalar antes de verificar.** Más pull requests por el mismo proceso de revisión convierten la revisión en la cola. ✅ Haz primero que el agente compruebe su propio trabajo.
- ❌ **Hacer vibe coding en un código compartido.** DHH describe un producto en el que dejar que la gente "fuera a su aire" produjo «muchos PR que, uno a uno, quizá podían justificarse durante un momento, pero que, todos juntos, destruyeron la arquitectura del sistema» (traducción propia). ✅ Que alguien sea responsable de la forma del sistema.
- ❌ **Construir tu propia plataforma de orquestación antes de entregar nada.** Steinberger lo llama "la trampa agéntica". ✅ Empieza con sesiones normales, worktrees y tests.
- ❌ **Ignorar el coste humano.** Más producción puede significar más agotamiento. ✅ Decide tu horario antes de que lo decidan los agentes.

La diferencia entre chatbot y sistema se ve incluso en un solo prompt:

❌ **Prompt débil**

```text
añade exportación a csv a shelf
```

✅ **Prompt mejor**

```text
Implementa la issue #4 (léela con gh issue view 4). Escribe primero los tests
y enséñame que fallan; después implementa. Ejecuta python -m unittest y pega
la salida. Si algo no se puede ejecutar, dime exactamente qué no se ejecutó
y por qué. Abre un pull request que cierre la #4.
```

El prompt mejor es corto porque se apoya en un sistema: una issue que ya contiene la especificación, tests que el agente puede ejecutar y un pull request donde se revisará el resultado.

## Comprueba lo que has aprendido

1. Una compañera dice: "Yo hago agentic engineering. El agente lo escribe todo y nunca miro el código." ¿Cómo lo llamaría DHH y qué falta según Karpathy y Osmani?

   <details><summary>Respuesta</summary>

   Según la definición de DHH, no mirar la implementación es vibe coding. Karpathy y Osmani vinculan el agentic engineering a mantener el listón de calidad profesional: alguien es responsable de la arquitectura, la calidad y la corrección. No leer cada línea puede estar bien; lo que falta es un sistema que haga fiable el resultado (verificación, revisión según el riesgo y una persona responsable del diseño).

   </details>

2. El estudio de METR de 2025 encontró que desarrolladores con experiencia eran un 19 % más lentos con IA. Da dos motivos por los que el resultado podría no aplicarse a ti y uno para tomárselo en serio de todos modos.

   <details><summary>Respuesta</summary>

   Podría no aplicarse porque usó herramientas de principios de 2025 y porque estudió a expertos en repositorios grandes que conocían a fondo, el contexto en el que las personas tienen más ventaja. Hay que tomárselo en serio porque los desarrolladores creían ir más rápido cuando iban más lentos: tu sensación de velocidad no es una prueba.

   </details>

3. Faros AI encontró un 98 % más de pull requests mergeados, pero un 91 % más de tiempo de revisión y ninguna mejora a nivel de empresa. ¿En qué sugiere eso que inviertas después?

   <details><summary>Respuesta</summary>

   En lo que ocurre después de escribir el código: agentes que verifican su propio trabajo, pull requests más pequeños, revisión automática antes de la humana y revisión escalonada por riesgo. Sin eso, producir más solo mueve la cola a la revisión.

   </details>

4. Te das cuenta de que vuelves a explicar el proyecto al principio de casi todas las sesiones. ¿Qué ciclo falta y dónde se enseña?

   <details><summary>Respuesta</summary>

   El ciclo de contexto: archivos de instrucciones y una base de conocimiento que carga cada sesión nueva. Se enseña en el módulo 04.

   </details>

5. ¿Por qué decimos que nuestras propias cifras comparan peras con manzanas?

   <details><summary>Respuesta</summary>

   Porque las historias escritas por agentes son más pequeñas y numerosas, el contexto es una herramienta interna con pocos usuarios, no hay grupo de control y el uso de las suscripciones incluye trabajo de revisión y de base de conocimiento que no siempre es útil. Muestran que la práctica es posible; no son un benchmark.

   </details>

## Ideas clave

- El agentic engineering significa que los agentes escriben la mayor parte del código mientras las personas diseñan el sistema que los rodea: contexto, descomposición, verificación, revisión y decisiones.
- El vibe coding, en la definición de DHH, significa que nadie mira la implementación. Algunos autores usan el término de otra forma, así que comprueba el significado.
- La mayoría se estanca en "una ventana, un prompt, una tarea", y la brecha con quienes van más allá sigue creciendo porque su entorno acumula mejoras.
- El papel pasa de escribir líneas a hacer de arquitecto y editor. El criterio de producto, la coherencia, el diseño de la verificación, las decisiones en los puntos de control y la comprensión siguen siendo humanos.
- La evidencia es mixta: las personas juzgan mal su propia velocidad, la IA amplifica fortalezas y debilidades existentes y las mejoras individuales pueden esfumarse en la revisión.
- Las cifras, incluidas las nuestras, son orientativas. Mide tu propio antes y después.

## Para profundizar

- [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/), de Simon Willison: ensayos de patrones breves y prácticos, que se mantienen al día.
- [Sequoia Ascent 2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/), de Andrej Karpathy: vibe coding frente a agentic engineering, y por qué importa que algo sea verificable.
- [Augmented Coding: Beyond the Vibes](https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes), de Kent Beck: cuidar la calidad del código mientras un agente escribe.
- [Agentic Engineering](https://addyosmani.com/blog/agentic-engineering/), de Addy Osmani: por qué los tests son el mayor factor diferencial.
- [El estudio de METR de 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) y [su actualización de 2026](https://metr.org/blog/2026-02-24-uplift-update/): el intento más cuidadoso de medir la velocidad, incluido lo que salió mal.
- [DORA State of AI-assisted Software Development 2025](https://dora.dev/dora-report-2025/): las capacidades que hacen que la IA compense a nivel de equipo.
- [How to Build an Agent](https://ampcode.com/notes/how-to-build-an-agent), de Thorsten Ball: un agente es un modelo, un bucle y unas pocas herramientas. Leerlo quita la magia.
- [My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey), de Mitchell Hashimoto: un contrapeso reflexivo a la idea de que más agentes es siempre mejor.

Siguiente: [2. Un agente, bien usado](../02-one-agent-done-well/README.md)
