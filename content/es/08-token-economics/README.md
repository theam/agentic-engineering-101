---
title: "Economía de tokens"
module: 8
kind: lesson
minutes: 45
level: advanced
last_reviewed: 2026-09-17
---

# 8. Economía de tokens

> **En una frase:** gasta tokens donde sustituyen atención humana, deja de gastarlos donde solo compran más rondas y juzga el resultado por el coste por PR mergeado, no por el coste por token.

## Lo que serás capaz de hacer

- Distinguir un consumo alto y sano del derroche.
- Elegir entre suscripciones y facturación por token de la API para cada tipo de uso.
- Calcular el coste por PR mergeado y leerlo junto con la tasa de retrabajo y los minutos humanos por PR.
- Encontrar los sumideros de tokens habituales en tu propio trabajo y corregirlos.
- Elegir modelos según su función y decidir cuándo paralelizar, cuándo ir en secuencia y cuándo delegar en un subagente.
- Medir el antes y el después sin dejarte engañar por las líneas de código ni por las impresiones personales.

## Por qué importa

Aquí tienes dos situaciones con una factura parecida.

Uno de nuestros ingenieros agotó en dos días el cupo semanal de un plan de la gama más alta. Tenía unos 20 agentes en marcha: unos escribiendo código, otros revisando los PR de los demás y otros manteniendo la base de conocimiento (knowledge base) del producto. No había nada roto. Eso es lo que consume esta forma de trabajar.

En el [módulo 7](../07-agents-review-agents/README.md) viste la otra situación: un bucle de revisión que trabajó toda la noche e hizo crecer un PR de 5.000 líneas hasta decenas de miles. Quemó tokens igual de rápido y dejó un PR más difícil de mergear que al principio.

Un contador de tokens no distingue entre las dos. El coste por PR mergeado, el retrabajo y los minutos humanos, sí. Esta lección va de gastar sin miedo en el primer tipo de trabajo y recortar el segundo.

## El consumo sigue a la habilidad

Cuanto más practiques lo que enseña esta guía, más tokens vas a usar. Cada sesión en paralelo lleva su propio contexto, los revisores vuelven a leer el código y el mantenimiento de la base de conocimiento ocurre en cada sesión. Quien lleva de 10 a 20 sesiones puede consumir un orden de magnitud más que quien conversa con un solo agente.

Algunas referencias públicas:

- La [documentación de costes de Claude Code](https://code.claude.com/docs/en/costs) indica que, en los despliegues empresariales, la media ronda los 13 $ por desarrollador por día activo y los 150–250 $ al mes, y que el 90 % de los usuarios se queda por debajo de 30 $ por día activo. Quien usa muchos agentes en paralelo está en la cola de esas medias. La misma página dice que los equipos de agentes usan unas 7 veces más tokens que las sesiones normales cuando los compañeros de equipo trabajan en modo plan.
- [Peter Steinberger](https://steipete.me/posts/just-talk-to-it) escribió en octubre de 2025 que pagaba cuatro suscripciones de OpenAI y una de Anthropic, «unos 1.000 al mes por tokens prácticamente ilimitados» (traducción propia).

> [!NOTE]
> **En The Agile Monkeys** varios de nuestros ingenieros llegan casi todas las semanas al límite de dos suscripciones de la gama más alta, una por proveedor. Es un dato indicativo, no un benchmark. También somos honestos con esto: probablemente buena parte de ese gasto todavía no es útil y hay que optimizarlo.

Así que no preguntes "¿cómo uso menos tokens?". Pregunta "¿qué compró cada token?". El gasto sano compra cosas que, si no, pagarías con tu atención: un PR verificado, un hallazgo de revisión real, una actualización de la base de conocimiento que le ahorra una hora a una sesión futura. El derroche compra rondas de más, reinicios y volver a deducir lo que ya sabías.

## Suscripciones, claves de API y los límites con los que te vas a topar

| | Suscripción (por persona) | API (pago por token) |
| --- | --- | --- |
| Cómo pagas | Una cuota mensual fija, con límites de uso por ventanas de tiempo | Por token, sin techo salvo que tú lo pongas |
| Sirve para | Uso interactivo intensivo de una persona | Automatización (bots de revisión, agentes de CI, tareas programadas), uso ligero o a ráfagas, atribución precisa |
| Ojo con | Límites que se reinician por ventanas; condiciones que definen qué cubre el plan; herramientas que suponen una sola cuenta iniciada por usuario de la máquina | Un bucle desbocado se convierte en una factura: pon límites de gasto antes de automatizar |

**Para un uso interactivo intensivo, las suscripciones suelen salir mucho más baratas.** Steinberger calculó que pagar por llamada a la API le habría costado unas diez veces más. [DHH](https://lexfridman.com/dhh-2/) hizo el port de una librería larga dentro de su suscripción y calculó que a precio por token le habría costado unos 550 $. Son estimaciones individuales, y los precios y los límites cambian a menudo. Por eso los detalles de cada herramienta viven en la [referencia de herramientas](../reference/tools.md), con fecha de revisión.

Patrones que funcionan:

- **Una suscripción de gama alta por proveedor** para quien practica de forma intensiva. Así tienes revisión entre proveedores ([módulo 7](../07-agents-review-agents/README.md)) y un plan de reserva cuando uno llega a su límite.
- **Claves de API con límite de gasto para todo lo que funciona sin una persona delante**, como bots de revisión, agentes que reparan la CI y tareas programadas. Los servicios que cobran por revisión suman rápido. La revisión gestionada de Claude Code cuesta de media entre 15 y 25 $ por revisión ([documentación](https://code.claude.com/docs/en/code-review)), y revisar en cada push multiplica esa cifra por el número de pushes.
- **Planifica la segunda cuenta antes de necesitarla.** Quien compra una segunda suscripción en mitad de una semana cargada descubre que sus herramientas suponen una sola cuenta iniciada por usuario de la máquina.

> [!WARNING]
> "Prácticamente ilimitado" nunca es literal. Lee las condiciones de tu plan antes de usar una suscripción personal para bots compartidos, la CI o el trabajo de otras personas. Ese uso suele corresponder a claves de API o a un plan de organización.

## Coste por PR mergeado

El coste por token te habla de tu proveedor. El coste por PR mergeado te habla de tu sistema.

- **Gasto en IA**: todo lo del periodo. Suscripciones prorrateadas al periodo, uso extra, claves de API de bots y CI, y servicios que cobran por revisión.
- **Coste por PR mergeado** = gasto en IA ÷ PR mergeados.
- **Tasa de retrabajo** = PR con retrabajo ÷ PR mergeados. Un PR con retrabajo es un PR mergeado que necesitó un arreglo posterior o una reversión en los 7 días siguientes.
- **Coste por PR mergeado neto** = gasto en IA ÷ (PR mergeados − PR con retrabajo).
- **Minutos humanos por PR mergeado**: tu tiempo leyendo, decidiendo y desbloqueando, a partir de una muestra cronometrada.

### Un ejemplo resuelto

> [!IMPORTANT]
> Son **números redondos inventados** para mostrar el cálculo. No son nuestros costes ni precios reales.

Entre la semana A y la semana B, una persona del equipo cambia tres cosas: cada PR lleva una declaración de intención y los bucles de revisión se cierran por decisión; el archivo de instrucciones que se carga siempre se reduce a la mitad; y lleva dos pistas de trabajo (tracks) más en paralelo.

| | Semana A | Semana B |
| --- | --- | --- |
| Suscripciones, prorrateadas a la semana | 100 $ | 100 $ |
| Uso extra y claves de API (bots, CI) | 40 $ | 80 $ |
| **Gasto en IA** | **140 $** | **180 $** |
| PR mergeados | 10 | 18 |
| PR con retrabajo (arreglados o revertidos en 7 días) | 3 | 2 |
| Minutos de revisión por PR (muestra) | 25 | 12 |

- Coste por PR mergeado: A = 140 ÷ 10 = **14,00 $**. B = 180 ÷ 18 = **10,00 $**.
- Tasa de retrabajo: A = 3 ÷ 10 = **30 %**. B = 2 ÷ 18 ≈ **11 %**.
- Coste por PR mergeado neto: A = 140 ÷ 7 = **20,00 $**. B = 180 ÷ 16 = **11,25 $**.
- Tiempo humano de revisión: A = 25 × 10 = **250 minutos**. B = 12 × 18 = **216 minutos**, para casi el doble de trabajo mergeado.

El gasto **subió** alrededor de un 29 %, y todos los números por unidad mejoraron. Así se ve "el consumo sigue a la habilidad" cuando funciona. Si solo miraras la factura, la semana B parecería un fracaso.

El intercambio que debes evitar es el contrario: ahorrar unos dólares de tokens por PR a cambio de minutos de tu propio trabajo. Ponle precio a tus minutos y la mayoría de los ahorros de tokens que cuestan tiempo de revisión dejan de parecer ahorros.

Matices:

- **No todos los PR son iguales.** Compara trabajo parecido en el mismo repositorio y mira la tendencia de varias semanas.
- **Mergeado no es lo mismo que valioso.** En un [estudio del despliegue en Microsoft](https://arxiv.org/abs/2607.01418) de agentes de programación de línea de comandos (un preprint), quienes los adoptaron mergearon aproximadamente un 24 % más de PR, y los autores insisten en que un PR mergeado «no es lo mismo que el valor que aporta» (traducción propia).
- **La ley de Goodhart.** En cuanto el coste por PR se convierte en objetivo, la gente parte los PR, y eso deshace [un PR, de principio a fin](../05-decompose-into-tracks/README.md). Vigila también el tamaño de los PR.
- **Parte del gasto nunca se convierte en un PR.** Planificar, investigar y mantener la base de conocimiento es trabajo real. Regístralo en una línea aparte en lugar de esconderlo.

## Dónde se desperdician los tokens

| Sumidero | Cómo lo notas | Solución |
| --- | --- | --- |
| Bucles de revisión que persiguen el crecimiento del alcance | El diff crece en cada ronda; los hallazgos de prioridad alta dejan de bajar | Declaración de intención, registro de triaje, cierre por decisión, un push por ronda ([módulo 7](../07-agents-review-agents/README.md)) |
| Contexto siempre cargado e hinchado | Se ignoran reglas; el contexto ya es grande antes de que escribas nada | Un `AGENTS.md` corto que funcione como mapa; los detalles en documentos y skills que se cargan cuando hacen falta ([módulo 4](../04-context-is-infrastructure/README.md)) |
| Demasiadas herramientas, plugins y skills | Los desgloses de uso les atribuyen una parte grande | Crea una skill cuando algo duele; quita las que no usas; prefiere CLI que el modelo ya conoce |
| Volver a deducir lo que ya se sabe | Cada sesión relee los mismos archivos y repite la misma investigación | "Lo que ya he comprobado" en los prompts de arranque; las decisiones, en la base de conocimiento |
| Sesiones largas más allá del contexto útil | Una sesión, muchas tareas sin relación; las correcciones se acumulan | Una tarea por sesión; empieza de cero tras dos correcciones fallidas |
| Salida de herramientas muy verbosa | Los logs de tests y compilación inundan el contexto | Un script envoltorio o un hook que imprima una línea si todo va bien y el motivo completo si algo falla ([módulo 3](../03-close-the-loop/README.md)); el trabajo ruidoso, en un subagente |
| Un modelo haciendo lo que debería hacer el código | El modelo reescribe números, consulta la CI en bucle, cruza datos | Scripts deterministas; llama al modelo solo cuando terminen las comprobaciones deterministas, con intentos limitados |
| Uso en segundo plano o en reposo | El uso sigue creciendo mientras no estás | Para los bucles y compañeros de equipo inactivos; nada de prompts programados sobre sesiones grandes |
| Trabajo que se tira | PR cerrados sin merge; pistas en paralelo que chocan | Prioriza por valor; planifica el orden de merge de las pistas en conflicto antes de que empiecen ([módulo 5](../05-decompose-into-tracks/README.md)) |

Por qué las sesiones largas cuestan tanto, según la [documentación de costes de Claude Code](https://code.claude.com/docs/en/costs): cada petición reenvía la conversación entera, así que una pregunta de una línea en una sesión abierta todo el día paga por todo el día. Compactar una conversación grande es en sí una petición grande, mientras que empezar de cero no cuesta nada. Las definiciones de herramientas también suman. Steinberger escribió en 2025 «Usa el MCP de GitHub y verás desaparecer 23.000 tokens» (traducción propia). Hoy Claude Code carga por defecto las definiciones de herramientas MCP solo cuando hacen falta, así que mide tu propia configuración en lugar de fiarte de números antiguos.

❌ **Prompt débil**

```text
El test de estadísticas falla. Averigua por qué.
```

✅ **Prompt mejor**

```text
test_finished_this_year, en tests/test_stats.py, empezó a fallar hoy, en la CI y
en mi portátil. Lo que ya he comprobado, así que empieza desde aquí y no lo vuelvas
a deducir: shelf/commands/stats.py no ha cambiado desde la última vez que pasó el
test (git log), y cada test tiene su propio SHELF_PATH y su propio HOME temporales
(tests/support.py), así que se descartan restos de archivos. Primera hipótesis:
el test tiene un año escrito a mano en vez de calcularlo, y el año acaba de
cambiar. Si no es eso, para y cuéntame lo que encontraste antes de probar otra cosa.
```

El prompt débil vuelve a pagar toda la investigación. El mejor solo paga lo que todavía no se sabe.

## Elegir el modelo según su función

**Usa por defecto el modelo más potente que tengas para planificar, diseñar la arquitectura, buscar la causa raíz de un fallo y revisar.** Los errores en esas fases se multiplican después. Un modelo más barato que necesita tres correcciones suele costar más en total: los tokens de los reintentos más tus minutos. [Boris Cherny](https://x.com/bcherny/status/2007179832300581177), creador de Claude Code, contó que usa el modelo más potente con razonamiento extendido para todo, porque es más lento pero hay que guiarlo menos.

**Baja de modelo solo con evidencia.** Ejecuta los dos modelos sobre las mismas issues reales en la misma CI y compara la tasa de éxito, las correcciones, los hallazgos de revisión, los tokens totales y el tiempo de reloj.

> [!NOTE]
> **En The Agile Monkeys** el modelo es una opción de configuración, no una elección fija en el código: el más potente por defecto, y solo bajamos con evaluaciones o con una presión de costes demostrada. Nuestros agentes automáticos guardan un recibo por ejecución con contadores de tokens y de coste, pero sin prompts ni transcripciones. Nuestro agente que repara la CI solo llama al modelo cuando terminan las comprobaciones deterministas, y con un número limitado de intentos.

El experimento de DHH muestra las dos caras. Pidió al modelo más potente que tenía que portara una librería de Python a Rust. Lo primero que hizo el modelo fue escribir un plan detallado de ocho pasos. Cuando se le acabaron los tokens de la suscripción, otro modelo terminó el port a partir de ese plan. Después dio el mismo plan a otros modelos. Varios completaron el trabajo por aproximadamente una décima parte del coste, y uno por una vigésima parte, aunque más despacio. Los más baratos fracasaron. Uno necesitó una docena de prompts solo para arrancar, y entonces:

> «Lo primero que hizo fue hacer trampa.» — DHH en [Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/) (traducción propia)

Encontró una implementación existente fuera de su directorio, la envolvió y dijo que había terminado. Qué sacar de esto:

1. **El plan era el artefacto valioso.** Gastar en el modelo más potente para el plan hizo posible una ejecución más barata.
2. **Los ejecutores más baratos pueden funcionar** cuando el plan es explícito y la verificación es sólida.
3. **Los más baratos pueden fallar en silencio o hacer trampa.** Verifica *cómo* se hizo el trabajo, no solo el resultado. [Simon Willison](https://simonwillison.net/2025/Oct/7/vibe-engineering/) describe a los agentes como «extraños aprendices digitales que harán trampa sin dudarlo si les das la oportunidad» (traducción propia).
4. **Fue una tarea en un dominio.** Prueba con tu propio trabajo antes de cambiar.

| Función | Por defecto | Cuándo puede encajar un modelo más barato o más rápido | Evidencia que pedir |
| --- | --- | --- | --- |
| Planificar, arquitectura, depuración | El más potente | Rara vez | Ninguna: quédate con el más potente |
| Implementar un plan explícito y aprobado | El más potente | Trabajo mecánico con buenos tests | La misma tasa de éxito y los mismos hallazgos de revisión en issues reales |
| Revisión | El más potente, de un proveedor distinto al del autor | Especialistas estrechos con una lista de comprobación | Detecta fallos sembrados; falsos positivos tolerables |
| Búsquedas, triaje de logs, consulta de documentación en subagentes | Un modelo rápido | Casi siempre | Los resúmenes siguen siendo correctos |

Los proveedores también pueden repartirse por funciones. Con los modelos actuales, el agente de un proveedor tiende a hablar más y nos ayuda a pensar, mientras que el de otro toma una tarea y la ejecuta, así que usamos mucho el segundo para revisar. Muchas herramientas también permiten bajar el esfuerzo de razonamiento en tareas sencillas. Los tokens de razonamiento se facturan como tokens de salida.

## Paralelizar, ir en secuencia o delegar

| Situación | Qué hacer | Por qué |
| --- | --- | --- |
| Issues independientes en archivos distintos, verificables por separado (S1, S2 y S4 del [proyecto de práctica](../../../practice/shelf/)) | Sesiones en paralelo en worktrees | El gasto crece de forma lineal y tu espera baja |
| Dos issues que cambian el mismo modelo o el mismo almacenamiento (C1 etiquetas, C2 versionado) | Implementa las dos en paralelo; pon en secuencia los merges y escribe el orden en las dos issues | La pista que va después hace merge de `origin/main` y se adapta; esperar convertiría dos pistas en una cola, y un orden sin planificar, en revisiones repetidas y trabajo descartado |
| El siguiente paso depende de lo que aprendas (una prueba de concepto, una API desconocida) | Primero una sesión exploratoria; después, repartir | Las apuestas en paralelo queman tokens en caminos que vas a descartar |
| Tu cola de revisión ya está llena | No empieces más; revisa y haz merge | [Faros AI](https://www.faros.ai/blog/ai-software-engineering) midió un 91 % más de tiempo de revisión en equipos con uso intensivo de IA |
| Una tarea acotada y verbosa cuyo resultado es un resumen | Subagente | Mantiene pequeño el contexto del orquestador |
| Trabajo que vas a tener que dirigir, o que termina en un PR | Sesión aparte | Visibilidad, control y un PR que se puede revisar |
| Un cambio mecánico en muchos archivos | Repartir tras un piloto con 2–3 archivos | Arregla el prompt antes de multiplicar sus errores |

Willison pone nombre al límite: «Solo puedo concentrarme en revisar e integrar un cambio importante a la vez» ([Embracing the parallel coding agent lifestyle](https://simonwillison.net/2025/Oct/5/parallel-coding-agents/), traducción propia).

**Los subagentes protegen el contexto, no los tokens.** Un subagente puede releer archivos que el orquestador ya vio, así que el total de tokens puede subir. Lo que compras es un orquestador que se mantiene pequeño y centrado. Anthropic describe subagentes que exploran usando «decenas de miles de tokens o más» (traducción propia) y devuelven resúmenes que a menudo ocupan entre 1.000 y 2.000 tokens ([Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). Steinberger prefiere ventanas separadas: «Lo que otros hacen con subagentes, yo suelo hacerlo con ventanas separadas» (traducción propia), porque así ve y dirige lo que vuelve.

## Mide el antes y el después

Parte de tu punto de partida del [laboratorio 1](../01-from-chatbot-to-system/lab.md), cambia una sola cosa cada vez y mide durante al menos dos semanas.

| Métrica | De dónde sale | Trampa |
| --- | --- | --- |
| PR mergeados por semana | `gh pr list --state merged` | El tamaño y el valor varían; partir PR la infla |
| Tiempo de ciclo (inicio → merge) | Fechas de issues y PR | Programar se acelera; esperar, no |
| Espera de revisión (listo → merge) | Historial del PR | Es donde se acumula el rendimiento extra de la IA |
| Tasa de retrabajo | Arreglos posteriores y reversiones en los 7 días siguientes a cada merge | Exige clasificar con honestidad, y esperar una semana |
| Tasa de fallos de cambios, tiempo de recuperación | Registros de despliegues e incidencias | Aparece semanas después |
| Gasto en IA por persona y por PR mergeado | Facturación y pantallas de uso del plan | Las cuotas fijas esconden el coste marginal |
| Minutos humanos por PR mergeado | Una muestra cronometrada | Las estimaciones se desvían; vuelve a muestrear |

[DORA](https://dora.dev/dora-report-2025/) sigue cinco métricas de entrega: tiempo de entrega de cambios, frecuencia de despliegue, tiempo de recuperación de un despliegue fallido, tasa de fallos de cambios y tasa de retrabajo de despliegues. Su investigación de 2025 dice que «el papel principal de la IA es el de amplificador, que magnifica las fortalezas y las debilidades que ya tiene una organización» (traducción propia), y asocia la adopción de IA a más rendimiento, pero también a más inestabilidad. Mide la estabilidad, no solo la velocidad.

Lo que dice la evidencia sobre cómo medir:

- **Las impresiones personales engañan.** En el [estudio de METR de 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), desarrolladores experimentados de open source tardaron un 19 % más con IA. Esperaban ir un 24 % más rápido y, después, seguían creyendo que habían ido alrededor de un 20 % más rápido.
- **El trabajo en paralelo rompe la medición simple del tiempo.** El [seguimiento de METR de 2026](https://metr.org/blog/2026-02-24-uplift-update/) encontró estimaciones que apuntan a una aceleración, pero sin significación estadística, y considera poco fiables sus mediciones de tiempo para quienes usan varios agentes a la vez, que es justo la forma de trabajar de esta guía.
- **Las tareas baratas desplazan a las valiosas.** El [análisis de sustitución de tareas](https://metr.org/blog/2026-05-08-task-substitution-and-uplift/) de METR vio que la gente se desplaza hacia las tareas que la IA abarató, así que las aceleraciones por tarea exageran el valor.
- **Más rendimiento desplaza el cuello de botella.** Faros AI (un proveedor, con datos correlacionales de más de 10.000 desarrolladores) vio que los equipos con uso intensivo de IA mergeaban un 98 % más de PR, mientras el tiempo de revisión subía un 91 %, el tamaño de los PR un 154 % y los fallos por desarrollador un 9 %, sin mejora significativa a nivel de empresa.
- **Las líneas de código son lo que más engaña.** DHH: «las líneas de código son una métrica estúpida en general» (traducción propia). Con esa métrica, el PR de 40.000 líneas del módulo 7 fue nuestro trabajo más productivo de esa semana.

Mide desde los sistemas: git, CI, facturación, incidencias. Usa las impresiones personales para saber cómo se sintió el trabajo, no para saber cuánto fue de rápido.

## Un ritmo sostenible

- **Una barra de uso que se reinicia no es una cuota que haya que llenar.** Steinberger ha escrito con franqueza sobre su «adicción a las máquinas de azar» de los agentes ([Just One More Prompt](https://steipete.me/posts/just-one-more-prompt), traducción propia). Arrancar a medianoche una sesión cuyo PR nadie va a revisar hasta la mañana no compra nada.
- **La persona se agota antes.** DHH, sobre su propio ritmo: «Esto no es sostenible en absoluto» (traducción propia). Deja de abrir pistas que no puedes revisar y protege tu descanso.
- **Presupuestos que siguen a la habilidad.** Los mismos presupuestos de tokens para todo el mundo frenan a quienes van más adelantados. Dale margen a quien más consume y revisa con esa persona sus números por unidad, no solo la factura.

## Otras formas de verlo

- **¿El modelo más potente para todo?** La documentación de costes de Claude Code recomienda un modelo de gama media para la mayoría de las tareas de programación y reservar la gama alta para arquitectura compleja y razonamiento en varios pasos. Steinberger dice que «si eres un buen conductor, puedes conseguir buenos resultados con cualquiera de los modelos de última generación» ([Lex Fridman Podcast #491](https://lexfridman.com/peter-steinberger-transcript/), traducción propia). Nosotros usamos el más potente por defecto y bajamos de modelo por función cuando hay evidencia, porque nuestro cuello de botella es la atención, no los tokens.
- **¿Merece la pena el gasto en paralelo?** [Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey) describe un camino de adopción cuidadoso sin varios agentes a la vez, y con las notificaciones desactivadas porque cambiar de contexto sale caro. Para algunas personas y algunos trabajos, la concentración compra más.
- **¿Contar tokens si domina el tiempo humano?** Hay quien dice que no. Nosotros los contamos, porque los patrones que desperdician tokens (bucles sin límite, contexto hinchado, volver a deducir) suelen desperdiciar también atención.
- **¿Sesiones enfocadas o largas y conectadas?** Dentro de nuestro propio equipo vemos las dos. Hay quien limita cada sesión a una tarea bien definida, le da a cada subagente exactamente el contexto que necesita y deja que un modelo potente planifique mientras otro más barato ejecuta. Según su experiencia, el contexto de negocio vago se cuela en el código como comentarios sueltos y desvíos. Otros mantienen unas pocas sesiones abiertas durante semanas, conectadas a sus fuentes ([módulo 4](../04-context-is-infrastructure/README.md#conecta-las-fuentes-y-señala-no-resumas)), las compactan varias veces al día y rara vez ven que pierdan el hilo. Cada enfoque sirve para algo distinto. Las sesiones enfocadas ganan cuando la tarea está bien definida: son más baratas, más predecibles y más fáciles de revisar. Las sesiones largas y conectadas ganan cuando necesitas explorar y decidir, o cuando una de ellas orquesta muchos hilos ([módulo 6](../06-run-sessions-in-parallel/README.md#una-sesión-orquestadora-para-cada-plan)), porque el contexto acumulado es justo lo que importa. En cualquier caso, separa en sesiones distintas lo que no tiene relación, y recuerda que cada petición de una sesión larga vuelve a enviar todo su historial.

## Ojo con

- **Racionar tokens verificando las cosas tú.** Cambias tokens baratos por minutos caros.
- **Bajar de modelo por precio** sin comparar resultados en tus propias tareas.
- **Presentar líneas de código o "sesiones lanzadas"** como productividad.
- **Revisar en cada push sin reglas de convergencia.** El coste se multiplica por push y las rondas no acaban.
- **Abrir más pistas en paralelo mientras crece tu cola de revisión.** Creas colas, no rendimiento.
- **Una sola sesión todo el día.** Cada pregunta paga la conversación de todo el día.

## Comprueba lo que has aprendido

1. Semana A: 100 $ de gasto, 10 PR mergeados, 3 de ellos con retrabajo. Semana B: 140 $, 11 PR mergeados, 1 con retrabajo. ¿Mejor o peor?

   <details><summary>Respuesta</summary>

   El coste por PR mergeado subió (10,00 $ → 12,73 $), pero el coste por PR mergeado neto se quedó casi igual (100 ÷ 7 ≈ 14,29 $ → 140 ÷ 10 = 14,00 $) mientras el retrabajo bajaba del 30 % a cerca del 9 %. Probablemente mejor. Mira los minutos humanos y más de una semana antes de decidir.

   </details>

2. Alguien de tu equipo propone usar un modelo más barato en toda la implementación para reducir el gasto a la mitad. ¿Qué pides?

   <details><summary>Respuesta</summary>

   Una comparación sobre las mismas issues reales en la misma CI: tasa de éxito, correcciones, hallazgos de revisión, tokens totales incluidos los reintentos, tiempo de reloj y una comprobación de que no hubo trampas (tests editados, código existente envuelto). Mantén la planificación y la revisión en el modelo más potente salvo que la evidencia diga lo contrario.

   </details>

3. ¿Cuál es más probablemente un sumidero de tokens: (a) un subagente que lee 40 archivos y devuelve un resumen de 1.500 tokens; (b) una sesión abierta desde la mañana que ha llevado seis tareas sin relación; (c) 12 sesiones en paralelo con issues independientes?

   <details><summary>Respuesta</summary>

   (b). Cada petición reenvía la conversación de todo el día, y el contexto irrelevante también empeora la calidad. (a) gasta tokens para proteger el contexto del orquestador. (c) está bien si tienes capacidad de revisión.

   </details>

4. ¿Por qué el tiempo por tarea es una mala medida para la forma de trabajar que enseña esta guía?

   <details><summary>Respuesta</summary>

   Con varios agentes a la vez, el tiempo dedicado a una tarea ni es continuo ni se puede atribuir, y el propio METR considera poco fiables sus mediciones de tiempo en ese escenario. Mide resultados desde los sistemas: PR mergeados, tiempo de ciclo, espera de revisión, retrabajo, incidencias y gasto.

   </details>

## Ideas clave

- El consumo sigue a la habilidad: un gasto alto es sano cuando compra trabajo verificado y mergeado.
- Para un uso interactivo intensivo, las suscripciones suelen salir mucho más baratas. Todo lo que funciona sin una persona delante usa claves de API con límite de gasto.
- Juzga por el coste por PR mergeado, junto con la tasa de retrabajo, los minutos humanos y el tamaño de los PR.
- Los mayores sumideros son los bucles de revisión sin límite, el contexto siempre cargado e hinchado, volver a deducir lo sabido y las sesiones largas.
- El modelo más potente para planes y revisión. Baja de modelo por función con evidencia y comprueba cómo se hizo el trabajo.
- Paraleliza el trabajo independiente, pon en secuencia los merges del que entra en conflicto y usa subagentes para proteger el contexto.
- Mide desde los sistemas, no con líneas de código ni impresiones, y cuida tu ritmo.

## Para profundizar

- [Claude Code: manage costs effectively](https://code.claude.com/docs/en/costs): seguimiento del uso, reducción de tokens, coste de los equipos de agentes.
- [Just Talk To It](https://steipete.me/posts/just-talk-to-it), de Peter Steinberger: suscripciones frente a API, CLI frente a servidores MCP, ventanas frente a subagentes.
- [DHH en Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/): el experimento del port con varios modelos.
- [METR 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) y [METR 2026](https://metr.org/blog/2026-02-24-uplift-update/): evidencia controlada y sus límites.
- [DORA 2025](https://dora.dev/dora-report-2025/): la IA como amplificador y las métricas de entrega que conviene vigilar.
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): por qué gana un contexto pequeño y con mucha señal.

Siguiente: [9. Equipos y organizaciones](../09-teams-and-organizations/README.md)
