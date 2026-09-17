---
title: "Guía para facilitadores"
kind: facilitator-guide
last_reviewed: 2026-09-17
---

# Guía para facilitadores

[Read in English](../en/facilitator-guide.md) ·
[Formatos y agendas de los workshops](README.md) ·
[Índice de la guía](../../content/es/README.md)

Esta guía es para quienes imparten la sesión de introducción, el intensivo o el
seguimiento, y para sus ayudantes. Léela junto con la
[página de workshops](README.md), que tiene las agendas, el trabajo previo y las
métricas.

Da una cosa por supuesta: **has hecho todos los laboratorios tú mismo, con la
versión actual de las herramientas que vas a enseñar, en las últimas dos
semanas.** Los agentes de programación cambian cada semana. Una demo que
funcionaba el mes pasado puede comportarse distinto hoy, y eso quieres
descubrirlo en casa, no delante de veinte personas.

Muchas de las técnicas de esta guía vienen de
[The Carpentries](https://carpentries.github.io/instructor-training/17-live.html),
que llevan años enseñando programación en workshops: programación en directo,
notas adhesivas, tarjetas de un minuto, ayudantes. Las hemos adaptado a una
materia con una propiedad nueva: la herramienta da una respuesta distinta cada
vez.

## Principios

1. **Programación en directo con agentes reales.** Escribe (o dicta) los prompts
   en directo, con las mismas herramientas que usan los participantes. Sigue el
   consejo de The Carpentries: ve despacio, usa una fuente grande, enseña cada
   paso, deja que la gente te siga. No sustituyas las demos por grabaciones si la
   red funciona. Una grabación enseña que los agentes son predecibles, y esa es
   la lección equivocada.
2. **Narra tus decisiones, no tus pulsaciones.** La habilidad que enseñamos es
   el criterio. Di en voz alta qué lees, qué te saltas y por qué, cuándo paras al
   agente y cuándo tiras trabajo. Por ejemplo: "No estoy leyendo este archivo de
   tests línea a línea. Estoy comprobando que un test falla si deshago el
   cambio. El código de almacenamiento *sí* lo leo, porque es donde se pierden
   datos."
3. **Cuenta con los fallos y aprovéchalos.** Los agentes dirán que han terminado
   sin ejecutar los tests, se saldrán del alcance y llegarán a los límites del
   plan, a menudo justo el día que presentas. Cuando pase: para, nombra el
   fallo, pregunta a la sala qué haría, y recupérate con la práctica del módulo.
   Un fallo recuperado en directo enseña más que una demo sin tropiezos. Cada
   módulo de abajo recoge sus fallos habituales y una forma de recuperarse. Si
   la recuperación también falla, pasa al plan B (el kit para ponerse al día o
   una grabación, avisando de que lo es) y coméntalo después.
4. **Manos en el teclado pronto; charlas cortas.** Ninguna charla de más de 25
   minutos. El primer laboratorio empieza antes de que pasen 35 minutos desde la
   apertura.
5. **Principios por encima de herramientas.** Una sala con varios proveedores es
   una buena sala: demuestra que la práctica no depende de un producto. No dejes
   que los debates sobre herramientas se coman el tiempo de laboratorio:
   apúntalos en una hoja de "temas aparcados" y retómalos en un descanso.
6. **Números honestos.** Nuestros números son indicativos, no benchmarks, y la
   investigación es mixta. Dilo cada vez que aparezca un número.
7. **Da ejemplo de hábitos seguros.** Nunca uses en tu equipo de demo un modo que
   se salte los permisos, nunca enseñes un secreto, nunca dejes que un agente haga
   merge. Lo que haces en el proyector es lo que la gente copia.
8. **Protege la energía de la gente.** Trabajar con varios agentes es, en
   [palabras de Simon Willison](https://simonwillison.net/2025/Oct/7/vibe-engineering/),
   «sorprendentemente eficaz, aunque agotador mentalmente» (traducción propia).
   Haz respetar los descansos. Nunca clasifiques a las personas.

## Antes del workshop

### Lista de comprobación previa

**Dos semanas antes:**

- [ ] Has hecho todos los laboratorios de principio a fin, con las versiones
  actuales de las herramientas que vas a enseñar, en los últimos 14 días.
- [ ] Has revisado la fecha `last_reviewed` de la
  [referencia de herramientas](../../content/es/reference/tools.md). Si un
  comando o una función ha cambiado, has abierto una
  [issue de "tool drift"](https://github.com/theam/agentic-engineering-101/issues/new?template=tool-drift.yml)
  y has ajustado tu demo.
- [ ] Has preparado el kit para ponerse al día (ver más abajo).
- [ ] Has grabado vídeos cortos de cuatro demos clave, como plan B si falla la
  red: el juego completo (laboratorio 0), el momento "terminado sin tests"
  (módulo 03), tres worktrees en paralelo (módulo 06) y una revisión con
  contexto limpio (módulo 07).
- [ ] Has calculado el presupuesto de costes de la sala y has preparado la
  reserva de emergencia (consulta
  [Presupuesto de costes para la sala](#presupuesto-de-costes-para-la-sala)).
- [ ] Has preparado a los ayudantes (30 minutos: las listas de fallos de esta
  guía, la regla de los cinco minutos, seguridad).

**Tres días antes:**

- [ ] Has revisado las confirmaciones del trabajo previo y has contactado con
  quien estaba atascado.
- [ ] Has asignado itinerarios de aprendizaje a partir de las respuestas de la
  inscripción y has planificado las parejas (consulta
  [Gestionar niveles mixtos](#gestionar-niveles-mixtos)).
- [ ] En remoto: salas de grupos, tablero de estado, formulario de tarjetas de
  un minuto y formulario de la encuesta, listos.

**El día anterior, o esa misma mañana:**

- [ ] **Equipo de demo:** otro usuario del sistema operativo o una máquina
  virtual sin credenciales de producción; notificaciones de chat y correo
  desactivadas (las de los agentes, activadas, porque vas a enseñar el reparto
  por turnos); fuente grande en el terminal; historial de la shell limpio; un
  perfil de navegador sin cuentas personales.
- [ ] **Ninguna regla privada que se cuele en la demo.** Los archivos de
  instrucciones y de memoria a nivel de usuario se aplican a todas las sesiones y
  pueden contener normas de la empresa o datos personales. Comprueba qué carga tu
  agente a nivel global (por ejemplo, la
  [memoria de Claude Code](https://code.claude.com/docs/en/memory) y
  [AGENTS.md en Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md)),
  o usa un usuario limpio.
- [ ] Dos proveedores de agentes con la sesión iniciada, el modelo más potente al
  que tengas acceso seleccionado, y sabes cuánto plan te queda.
- [ ] Una copia nueva del proyecto de práctica para las demos, más una copia de
  repuesto por si la primera se ensucia.
- [ ] La red probada en la sala con varios portátiles ejecutando sesiones de
  agente; un punto de acceso con la batería cargada.
- [ ] Copias impresas o sin conexión del [catálogo de issues](../../practice/issues/es.md)
  y de la anatomía de un prompt de arranque de la
  [lección 05](../../content/es/05-decompose-into-tracks/README.md), para las
  actividades sin conexión.
- [ ] Notas adhesivas de dos colores para todo el mundo, fichas, marcadores, un
  temporizador, y una pizarra o una pared para el tablero del sprint.

### Ayudantes

Los ayudantes hacen o deshacen un workshop práctico. Cuenta con uno por cada 8–10
participantes.

- Han hecho todos los laboratorios.
- Acuden primero a las notas adhesivas de "ayuda". Preguntan "¿Qué le pediste
  al agente?" y "¿Qué te respondió?" antes de tocar nada.
- **No toman el control del teclado.** Guían.
- **Regla de los cinco minutos:** si un problema no se resuelve en cinco
  minutos, el participante hace pareja con alguien de al lado, el ayudante apunta
  el problema y vuelve a él en el descanso.
- Recogen historias de fallos para las puestas en común, con permiso de quien
  las vivió.
- Vigilan los descuidos de seguridad: un secreto en pantalla, un modo que se
  salta los permisos en un portátil con credenciales.

### El kit para ponerse al día

Prepáralo una vez a partir de tu propio recorrido y reutilízalo:

- Un `AGENTS.md`, un `kb/ACTIVE.md` y un registro de decisión de referencia para
  el proyecto de práctica (de tu laboratorio 4).
- Una barrera de seguridad (guardrail) que funcione (de tu laboratorio 3).
- Tres prompts de arranque (kickoff prompts) para el laboratorio 6 (de tu
  laboratorio 5), uno por pista: pista A (S4 y S5), pista B (C1) y pista C (C2),
  con la nota sobre cómo chocan C1 y C2.
- La descripción de un pull request con una declaración de intención y un
  ejemplo de registro de triaje (ledger) (de tu laboratorio 7).

Comparte las piezas en el chat de la sala o en un documento compartido cuando
alguien se quede atrás. Las issues S1–S6 son independientes, así que quien no
termine un laboratorio puede empezar el siguiente desde donde esté: los
laboratorios dicen adónde va una issue que siga abierta. Solo dos pasos dependen
de un resultado anterior. El laboratorio 5 reutiliza el registro de la decisión
sobre C1 y C2 del laboratorio 4, y el inicio del día 2 necesita las issues y los
prompts de arranque del laboratorio 5. El kit cubre los dos.

## Señales y comentarios en la sala

### Notas adhesivas y equivalentes en remoto

Da a cada participante notas adhesivas de dos colores. Una nota en la tapa del
portátil significa "necesito ayuda". El otro color significa "he terminado" o
"todo bien". Sin nota significa "trabajando".

- **Úsalas como encuestas instantáneas:** "Pon tu nota de 'terminado' cuando tus
  tests pasen en `main`." Ves el estado de la sala en cinco segundos.
- **Elige colores que todo el mundo distinga.** La tradición de The Carpentries
  es rojo y verde, que muchas personas con alteraciones de la visión del color no
  distinguen. Usa dos colores con distinta luminosidad (por ejemplo, amarillo y
  rosa oscuro) y escribe en ellas **AYUDA** y **OK**.
- **En remoto:** usa las reacciones o la mano levantada de la plataforma o,
  mejor, un tablero de estado compartido: una tabla con una fila por participante
  y una columna de estado con `OK`, `AYUDA` o `TRABAJANDO`. También sirve un
  canal de chat dedicado donde la gente escribe `AYUDA: <una línea>`. Un ayudante
  vigila el tablero a tiempo completo.

### Tarjetas de un minuto

En la comida y al final de cada día, cada participante escribe dos cosas en una
ficha, de forma anónima: **una cosa que funcionó** y **una cosa que cambiar, o
que todavía no está clara**. Léelas en el descanso. Abre la siguiente sesión
dedicando dos minutos a los dos temas principales. Así la gente ve que la
escuchas, y la confusión se detecta antes de que se acumule. En remoto: un
formulario anónimo de dos preguntas, con el enlace publicado cinco minutos
antes del descanso.

### Control del tiempo y lista de recortes

- Ten un temporizador visible en cada laboratorio. Avisa cuando queden 10
  minutos y cuando queden 2.
- Al final de un laboratorio, si más de la mitad de la sala sigue con notas de
  "ayuda", alarga una vez, hasta 10 minutos. Después enseña el final y comparte
  el kit para ponerse al día.
- Cuando vayas con retraso, recorta en este orden:
  1. La puesta en común después del laboratorio 0 baja a 5 minutos.
  2. El laboratorio 8 pasa a ser tarea, hecha en la semana 4 del seguimiento con
     datos reales.
  3. El laboratorio 1 se termina en casa (casi todo el punto de partida es
     trabajo previo).
  4. El sprint se reduce a 60 minutos.
- **Nunca recortes** el laboratorio 3 (barreras de seguridad), el laboratorio 5
  (el día 2 depende de él) ni el laboratorio 7 (revisión).

## Gestionar niveles mixtos

Toda sala mezcla los tres itinerarios de aprendizaje del
[módulo 00](../../content/es/00-start-here/README.md). Haz estas preguntas en el
formulario de inscripción:

1. La semana pasada, ¿cuántas sesiones de agente llegaste a tener trabajando a
   la vez, como máximo? (0 / 1 / 2–4 / 5+)
2. ¿Con qué frecuencia usas un agente de programación? (nunca / cada semana /
   cada día)
3. ¿Has usado worktrees de git? (no / los he probado / habitualmente)
4. ¿Lideras un equipo o decides cómo trabaja tu equipo? (sí / no)
5. En una escala de 1 a 5, ¿cuánta confianza tienes en: diseñar tareas que un
   agente pueda verificar; mantener el contexto entre sesiones; ejecutar tres o
   más sesiones en paralelo; revisar pull requests de agentes con agentes;
   estimar el coste por PR mergeado?
6. ¿Qué quieres llevarte?

Los recién llegados suelen responder "nunca" o "cada semana", con 0–1 sesiones.
Los usuarios diarios de un solo agente responden "cada día", con 1 sesión. Los
líderes técnicos respondieron "sí" a la pregunta 4, y quien ya está en 2–4 o 5+
sesiones sigue los apartados "Para ir más allá" de ese itinerario.

| | Recién llegado a los agentes | Usuario diario de un solo agente | Líder técnico, o ya trabaja en paralelo |
|---|---|---|---|
| **Antes del día 1** | Trabajo previo, más una tarea pequeña con el agente en el proyecto de práctica | Trabajo previo | Trabajo previo, y un vistazo a las lecciones 05–07 |
| **En los laboratorios** | Solo los pasos básicos; en pareja en los laboratorios 0–2 | Pasos básicos y, si da tiempo, "Para ir más allá" | Apartados "Para ir más allá"; la pista de C1/C2; S7 |
| **Objetivo en paralelo el día 2** | 2 sesiones | 3–4 sesiones | 5 o más |
| **Papel en la sala** | Lleva el teclado en pareja | — | Referente de mesa: responde preguntas antes que los ayudantes, sin tomar el control del teclado |
| **Vigila** | Saturación; copiar prompts sin leer la respuesta | Viejos hábitos: prompts largos "perfectos", leer cada línea de cada diff | Aburrimiento; construir herramientas en lugar de hacer el laboratorio; acaparar a su pareja |

Sienta a un líder técnico en cada mesa. Forma parejas de niveles distintos en
los laboratorios 0–2, donde las preguntas de la persona con experiencia ayudan.
Forma parejas del mismo nivel en los laboratorios 6–7, donde cada cual avanza a
un ritmo muy distinto.

Peter Steinberger llama a la forma de fallar típica de los líderes técnicos "la
trampa agéntica": dedicar el tiempo a la orquestación, a comandos a medida y a
herramientas caseras en lugar de entregar (consulta
["Just Talk To It"](https://steipete.me/posts/just-talk-to-it)). Nómbrala con
amabilidad y reconduce hacia el laboratorio.

## Notas por módulo

Cada módulo tiene las mismas cinco partes: cuándo ocurre, qué enseñar en la
demo, la idea que debe calar, los fallos habituales y cómo recuperarse, y una
pregunta para la sala. Las horas se refieren a la agenda del intensivo en la
[página de workshops](README.md).

### Sesión de introducción

**Bloque:** los 90 minutos completos.

**Demo:** el juego completo, rápido. Prepara una copia nueva del proyecto de
práctica, pero haz en directo la discusión, el plan y la construcción.

**La idea que debe calar:** *el ingeniero pasó la sesión decidiendo, no
tecleando.*

**Fallos habituales:**

- **El agente va lento y la demo se atasca.** No esperes en silencio. Pasa a la
  parte siguiente (crear el worktree, arrancar S2) y vuelve cuando llegue la
  notificación. *Esa* es la lección: DHH describe a los agentes en el
  [Lex Fridman Podcast](https://lexfridman.com/dhh-2/) como «a la vez demasiado
  rápidos y demasiado lentos» (traducción propia), y las sesiones en paralelo
  son la respuesta a la espera.
- **El agente termina S1 a la perfección y ejecuta los tests por su cuenta.**
  Bien. Para el momento del fallo, enseña la barrera bloqueando un test que
  rompes a propósito.

**Pregunta a la sala:** "¿Qué paso te pareció trabajo del agente y cuál trabajo
tuyo?"

### Módulo 00 — Empieza aquí (laboratorio 0)

**Bloque:** día 1, 09:20–10:35 (charla de 15 minutos, laboratorio de 45 minutos,
puesta en común de 15 minutos).

**Demo:** no enseñes el laboratorio completo antes de que la gente lo haga.
Enseña solo los dos primeros prompts (pedir al agente que explique el proyecto,
discutir S1) y después deja trabajar a la sala mientras das vueltas. El trabajo
previo cubría la sección "Antes de empezar" del laboratorio. A quien se la haya
saltado, un ayudante le acompaña con esos comandos al fondo de la sala mientras
empieza el laboratorio.

**La idea que debe calar:** *en 45 minutos tuviste un agente construyendo, otro
trabajando en paralelo y un tercero revisando. No entendiste cada paso, y
todavía no hacía falta.*

**Fallos habituales:**

- **`gh pr create` falla.** Normalmente no hay sesión iniciada o la copia nunca
  se subió. Comprueba `gh auth status` y `gh repo view`. Si sigue fallando,
  sáltate el PR y haz que la sesión nueva revise la rama en local, a partir de
  `git diff main...s1-status-filter`.
- **El agente pide permiso cada vez que ejecuta los tests.** Enseña cómo
  permitir el comando de tests en la configuración de permisos del agente (para
  Claude Code, consulta los
  [modos de permisos](https://code.claude.com/docs/en/permission-modes)). No
  cambies a un modo que se salte los permisos.
- **Alguien arranca S2 en la misma carpeta que S1.** Pregunta qué pasa cuando
  dos agentes editan archivos en el mismo checkout a la vez. Crea el worktree en
  ese momento. Es el módulo 06 en una pregunta.
- **No se encuentra `python`** (habitual en macOS). Usa `python3 -m unittest` y
  díselo al agente en la sesión para que deje de reintentarlo.
- **El revisor lo aprueba todo.** Para el laboratorio 0 está bien. Pregunta al
  revisor "¿Qué haría que este PR no pasara la revisión?" y remite al módulo 07.

**Pregunta a la sala:** "¿Qué hizo el agente que no le habías pedido?"

### Módulo 01 — Del chatbot al sistema

**Bloque:** día 1, 10:50–11:30 (charla de 20 minutos, laboratorio de 20
minutos). Los participantes registraron su semana en casa, así que los 20
minutos cubren solo la última parte del laboratorio 1: calcular los números,
escribir el punto de partida y fijar objetivos.

**Demo:** sin código. Repite la encuesta del formulario de inscripción con notas
adhesivas en la pared (0 / 1 / 2–4 / 5+ sesiones la semana pasada). Presenta
los resultados de METR con honestidad: en el
[estudio de 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/),
desarrolladores experimentados esperaban ir más rápido, la medición dijo que
fueron más lentos, y aun así creían haber ido más rápido.

**La idea que debe calar:** *el techo no es el prompt, es el sistema alrededor
del agente. Y sentir que vas más rápido no es una prueba: por eso mides tu
propio punto de partida.*

**Fallos habituales:**

- **Un debate sobre la evidencia se apodera de la sesión.** Dale dos minutos a
  cada postura, apúntalo en la hoja de temas aparcados y vuelve a "vas a medir
  tus propios números".
- **No hay datos de partida** (alguien se saltó el trabajo previo). Reconstruye
  la semana pasada: PR mergeados con `gh pr list`, sesiones de memoria, y marca
  cada número como estimado.
- **Alguien siente que va por detrás.** La encuesta del punto de partida puede escocer. Dilo con claridad: aquí no se clasifica a nadie, cada persona llega desde un punto distinto, y esta brecha se cierra en semanas, no en años. Remite a la cita de DHH del módulo 00.
- **Alguien escéptico siente que la sala le está vendiendo algo.** Dale la
  bienvenida. Lo que defiende la guía es la calidad primero, y cada lección tiene
  un apartado "Otras formas de verlo" con los desacuerdos abiertos.
- **Nuestros números indicativos se toman como objetivos** (por ejemplo, las
  historias por persona al día). Repite que comparan peras con manzanas: son una
  referencia, no un benchmark.

**Pregunta a la sala:** "¿Qué te convencería, con tus propios números, de que
esto funciona, o de que no funciona?"

### Módulo 02 — Un agente, bien usado

**Bloque:** día 1, 11:30–12:45 (demo de 20 minutos, laboratorio de 55 minutos).

**Demo:** usa S7, la petición vaga a propósito, solo para la discusión, así no
resuelves S3, que es el laboratorio:

```text
Vamos a discutir la issue S7 antes de construir nada: "Haz que shelf sea más
útil para clubes de lectura." Lee primero el código. Dame tres opciones con sus
ventajas e inconvenientes. No cambies ningún archivo hasta que te diga que
construyas.
```

Elige una opción en voz alta y di por qué. Pide un plan. Si da tiempo,
construye una porción pequeña, verifícala y termina con "Ahora que lo has
construido, ¿qué habrías hecho de otra forma?"

Los participantes llevan S7 por esta misma discusión en el sprint del día 2, así
que presenta tu opción como un ejemplo, no como la respuesta.

**La idea que debe calar:** *los mensajes cortos funcionan cuando la sesión
tiene contexto. Revisa la intención (el plan) antes de revisar líneas.*

**Fallos habituales:**

- **El agente empieza a construir durante la discusión.** Páralo y dilo
  explícitamente: "Estamos discutiendo; no edites archivos." Descarta los cambios
  (por ejemplo, `git restore .` para los archivos versionados, y pide al agente
  que borre los archivos nuevos que haya creado). Tirar trabajo es barato. Dilo
  también en voz alta.
- **Hay participantes que se pasan 15 minutos puliendo un prompt perfecto.**
  Pídeles que envíen la versión en bruto y dejen que el agente haga las
  preguntas.
- **El registro de correcciones está vacío.** Pregunta: "¿Cuál de sus
  decisiones habrías cuestionado en el pull request de un compañero?"
- **Modo plan frente a conversación acaba en discusión.** Las dos valen. La
  prueba es si revisaste la intención antes de que existiera el código.
- **Un participante no puede juzgar el Python.** Ponlo en pareja, y que pida al
  agente que explique el diff en lenguaje llano y enseñe el test que lo
  demuestra.
- **Los tests de S3 dependen de la fecha de hoy.** Los tests de "libros
  terminados este año" que construyen sus datos con el reloj real pasan hoy y
  pueden fallar el 1 de enero. Pregunta a la sala: "¿Este test seguiría pasando
  el año que viene?" Después haz que el agente fije la fecha en el test en lugar
  de leer el reloj.

**Pregunta a la sala:** "¿Dónde corregiste al agente, y esa corrección podría
haber ido al contexto?"

### Módulo 03 — Cerrar el ciclo

**Bloque:** día 1, 13:45–14:50 (demo de 20 minutos, laboratorio de 45 minutos).

**Demo:** usa una petición cuya implementación obvia rompa un test existente. En
`shelf`, `tests/test_store.py` fija los campos exactos que se guardan de cada
libro, así que algo como esto funciona:

```text
Añade una opción --notes opcional a shelf add y guarda las notas con el libro.
Que sea breve.
```

En directo, lánzala sin barrera. Si el agente dice "terminado" sin ejecutar los
tests, ejecuta tú `python3 -m unittest` en pantalla: falla el test del formato
guardado. Después añade la barrera, por ejemplo un
[hook](https://code.claude.com/docs/en/hooks) de tipo Stop que ejecute los tests
o, para agentes sin hooks, un hook `pre-commit` de git, y lanza la petición
otra vez.

La misma demo enseña la diferencia entre actualizar un test y debilitarlo.
Añadir un campo a propósito implica cambiar los campos fijados, y eso es
correcto. Borrar la comprobación para que todo pase no lo es. Pregunta a la sala
cuál de las dos hizo el agente.

Sé honesto cuando el agente se porte bien: puede que ejecute los tests por su
cuenta y acierte. Di "Hoy lo ha hecho. La barrera convierte 'normalmente' en
'siempre'", y después rompe un test a propósito y enseña cómo bloquea la
barrera.

Como dice Peter Steinberger en
[The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code):
«tienes que cerrar el ciclo. Tiene que poder depurarse y probarse a sí mismo.
Ese es el gran secreto» (traducción propia).

**La idea que debe calar:** *la prosa pide; los hooks obligan. Cuando falla una
comprobación, arregla el cambio, no la comprobación.*

**Fallos habituales:**

- **El agente dice "terminado", pero no se ejecutaron los tests.** No discutas la
  afirmación. Pide pruebas: "Enséñame la salida de los tests." Después añade la
  barrera. La lección es pedir pruebas, no afirmaciones.
- **El agente "arregla" el fallo debilitando, saltándose o borrando un test.** Es
  el mejor momento didáctico del día. Para, enseña el diff del archivo de tests y
  ponle nombre. En ["Vibe engineering"](https://simonwillison.net/2025/Oct/7/vibe-engineering/),
  Simon Willison llama a los agentes «becarios digitales raros que harán trampa
  sin dudarlo si les das la oportunidad» (traducción propia). Restaura el test,
  añade una regla a `AGENTS.md` y recuerda que la revisión (módulo 07) es la
  segunda línea de defensa.
- **La barrera nunca salta.** Normalmente está en el sitio equivocado, no es
  ejecutable o está asociada al evento equivocado. Antes de fiarte de una
  barrera, pruébala con un test que falle a propósito. Empieza con un hook que
  solo imprima una línea.
- **La barrera bloquea para siempre.** Un test inestable, un entorno roto o un
  intérprete que falta mantienen al agente en bucle quemando tokens. Para la
  sesión. Haz que la barrera distinga "los tests fallaron" de "los tests no se
  pudieron ejecutar", y que el agente informe exactamente de qué no se ejecutó y
  por qué.
- **Alguien quiere un modo que se salte los permisos "para ir más rápido".** No
  en este equipo. Explica que saltarse los permisos solo tiene sentido en un
  entorno aislado sin nada que robar. El módulo 09 cubre el resto.

**Pregunta a la sala:** "¿Qué regla de tu proyecto real se incumple una y otra
vez, y qué comprobación la detectaría siempre?"

### Módulo 04 — El contexto es infraestructura

**Bloque:** día 1, 15:05–16:10 (demo de 20 minutos, laboratorio de 45 minutos).

**Demo:** abre una sesión nueva en una copia de práctica sin archivos de
instrucciones y sin base de conocimiento (knowledge base), y pregunta:

```text
¿Qué estamos haciendo en este repositorio y por qué? ¿Qué hemos decidido sobre
las etiquetas y sobre versionar el formato de almacenamiento?
```

Nada en el código puede responder a la segunda pregunta, así que la respuesta es
genérica o inventada. Añade el `AGENTS.md`, el `kb/ACTIVE.md` y el registro de
decisión de tu kit para ponerse al día, abre una sesión nueva y vuelve a
preguntar. Después enseña cómo "recuerda esto" convierte una corrección en una
nota.

**La idea que debe calar:** *toda sesión empieza con amnesia. Una base de
conocimiento abarata "una sesión nueva con todo el contexto", y la escribe el
agente, no tú.*

**Fallos habituales:**

- **Hay participantes que escriben la base de conocimiento a mano.** Reconduce:
  que hablen con el agente y le dejen escribir; cuando se equivoque, se le
  corrige en una frase.
- **`AGENTS.md` crece, largo y genérico** ("escribe código limpio"). Aplica a
  cada línea la prueba de las
  [buenas prácticas de Anthropic](https://code.claude.com/docs/en/best-practices):
  ¿quitarla provocaría un error? Mantén `ACTIVE.md` por debajo de 100 líneas.
- **La comparación de antes y después parece igual.** El proyecto de práctica es
  pequeño y el agente puede leerlo entero en segundos. Pregunta por el *porqué* y
  por *lo siguiente* (decisiones, opciones aparcadas), que el código no puede
  responder. Sé honesto: la diferencia es mucho mayor en repositorios reales con
  historia.
- **No se hace commit de la base de conocimiento.** Ejecuta `git status` al final
  del laboratorio: un cambio en la base de conocimiento sin commit no ha
  ocurrido.
- **Claude Code ignora `AGENTS.md`.** Lee `CLAUDE.md`; añade un `CLAUDE.md` que
  importe `@AGENTS.md` (consulta la
  [memoria](https://code.claude.com/docs/en/memory)).
- **Los líderes técnicos se ponen a construir una biblioteca de skills.** Crea
  una skill cuando algo duela, no por adelantado: las skills cuestan contexto.

**Pregunta a la sala:** "¿Qué le has explicado este mes a un agente que mañana
tendrás que volver a explicar?"

### Módulo 05 — Descomponer en pistas

**Bloque:** día 1, 16:10–17:10 (charla de 15 minutos, laboratorio de 45 minutos).

**Demo:** solo los dos primeros minutos del laboratorio. Pide al agente que
explique cómo va a crear y agrupar las issues *antes* de crear ninguna. Enseña
que revisas la agrupación, no el cuerpo de cada issue.

El prompt del catálogo deja fuera a propósito la nota de seguridad en paralelo
de cada issue, así que el agente tiene que encontrar los conflictos por su
cuenta. El catálogo termina con una clave de respuestas (archivos por issue,
solapamientos verificados y un reparto sugerido en tres pistas). Léela antes del
workshop y pide a los participantes que no la abran hasta terminar el
laboratorio.

**La idea que debe calar:** *dimensiona por radio de impacto. Las pistas de
trabajo (tracks) independientes tocan archivos disjuntos, no títulos
disjuntos. El orden de merge no es el orden de trabajo.*

**Fallos habituales:**

- **El agente no ve que C1 y C2 chocan.** Pídele que enumere los archivos y las
  estructuras de datos que cambia cada issue. Verá que las dos cambian
  `shelf/models.py`, `shelf/store.py` y el test del formato guardado en
  `tests/test_store.py`. Esa es la lección: los conflictos aparecen en el radio
  de impacto, no en los títulos.
- **El agente marca como conflicto cualquier archivo compartido.** S5, C1 y C2
  tocan las tres `shelf/store.py`, pero S5 solo añade un método en una parte del
  archivo que las otras dos no cambian, y git lo integra sin conflictos. Si S1 o
  S6 siguen abiertas, cada una tiene un solapamiento textual pequeño con C1
  (`shelf/commands/list_books.py` y `shelf/commands/add.py`) que git o un agente
  resuelven en minutos. C1 frente a C2 es otra cosa: un conflicto semántico que
  necesita una decisión humana. Pide al agente que distinga los dos tipos.
- **El agente parte una issue en PR1/PR2/PR3, o crea muchas microissues.** Un PR
  de principio a fin. La revisión humana es el paso caro, y las instrucciones de
  alcance no sobreviven a las fases.
- **Issues duplicadas.** El agente reintentó un comando que en realidad había
  funcionado. Lístalas con `gh issue list` y cierra las duplicadas con
  `gh issue close`. Lección: después de escribir a través de un CLI o una API,
  vuelve a leer y verifica.
- **Los prompts de arranque ocupan una línea, o tres páginas.** Compáralos con la
  anatomía de la [lección 05](../../content/es/05-decompose-into-tracks/README.md):
  qué he comprobado ya, decisiones ya tomadas, cómo saber que has terminado, qué
  hay que informar.
- **Crear muchas issues muy deprisa.** GitHub puede tomarlo por spam: el bot de
  DHH quedó marcado tras crear 28 issues de golpe. El catálogo es pequeño; no
  pidas al agente que genere docenas más.
- **A la sala se le acaba el tiempo.** Reparte los prompts de arranque del kit
  para ponerse al día, para que todo el mundo pueda empezar el día 2.

**Pregunta a la sala:** "¿Cuáles de estas pistas podrían avanzar a la vez que
las demás, y cómo lo sabes?"

### Apertura del día 2

Dedica dos minutos a las tarjetas de un minuto. Después haz una comprobación con
notas adhesivas: árbol de trabajo limpio, las issues existen (`gh issue list`),
los tres prompts de arranque con commit, el uso del plan del día 1 apuntado.
Reparte el kit para ponerse al día a quien le falte alguna pieza.

### Módulo 06 — Ejecutar sesiones en paralelo

**Bloque:** día 2, 09:15–11:00 (demo de 25 minutos, laboratorio de 80 minutos).

**Demo:** crea los tres worktrees del laboratorio 6 a partir de un
`origin/main` recién traído, con `--no-track` para que ninguna rama siga a
`origin/main` (la
[lección 06](../../content/es/06-run-sessions-in-parallel/README.md#una-receta-de-worktrees-que-no-muerde)
explica por qué):

```bash
git fetch origin
git worktree add --no-track -b s4-export ../shelf-a origin/main
git worktree add --no-track -b c1-tags ../shelf-c1 origin/main
git worktree add --no-track -b c2-file-version ../shelf-c2 origin/main
git worktree list
```

(Claude Code también puede crearlos con
[`claude --worktree <name>`](https://code.claude.com/docs/en/worktrees).)
Arranca una sesión por worktree con su prompt de arranque y ponle nombre a cada
una. Ten una shell normal al lado de cada sesión. Cuando lleguen notificaciones,
atiéndelas por turnos (round-robin), primero la de mayor prioridad. Termina
eliminando un worktree con `git worktree remove`.

Presenta el desacuerdo: nosotros usamos las notificaciones para guiar el reparto
por turnos, mientras que Mitchell Hashimoto recomienda lo contrario en
["My AI Adoption Journey"](https://mitchellh.com/writing/my-ai-adoption-journey):
«Desactiva las notificaciones de escritorio de los agentes. Cambiar de contexto
sale muy caro» (traducción propia).

**La idea que debe calar:** *esperar a un solo agente mata el ritmo. Con tres en
marcha siempre estás decidiendo, y el techo lo pone tu atención, no los
agentes.*

**Fallos habituales:**

- **Dos pistas en paralelo chocan (C1 y C2).** Está previsto, y es más sutil de
  lo que parece. Git hace merge de `shelf/models.py` y `shelf/store.py` sin
  quejarse y solo se detiene en `tests/test_store.py`. Tomes el lado que tomes de
  ese test, falla un test del formato guardado, porque nadie ha decidido qué
  contiene la versión 2 del archivo. Un merge textual limpio no es un conflicto
  resuelto: ejecuta los tests. Cómo recuperarse: haz merge primero de la pista A.
  Después para y toma la decisión humana en voz alta. **C1 primero:** la versión
  2 incluye `tags`, y la migración desde la versión 1 da a los libros antiguos
  una lista de etiquetas vacía; una sola versión, menos código. **C2 primero:**
  C1 sube `SCHEMA_VERSION` a 3 y añade una migración desde la versión 2; más
  código, pero es lo que hace un proyecto real cuando la versión 2 ya está
  publicada. Deja escrita la decisión y, en el segundo worktree, ejecuta
  `git fetch origin` y `git merge origin/main` y dale al agente esa decisión con
  los tests como árbitro. Pregunta a la sala qué orden elegiría. Ninguno es
  incorrecto. El error es dejar que el agente elija por accidente.
- **El agente "resuelve" el conflicto entre C1 y C2 borrando el test del otro
  lado.** La suite se pone en verde y una comprobación desaparece. Trátalo como
  cualquier test debilitado: restáuralo, toma la decisión de arriba y haz que el
  agente actualice la comprobación a propósito.
- **Las tres sesiones trabajan en la misma carpeta.** Los archivos se
  sobrescriben y los tests pasan y fallan alternativamente. Para las tres,
  ejecuta `git status`, descarta lo que nadie sepa explicar, crea los worktrees y
  vuelve a empezar desde los prompts de arranque. Empezar de nuevo es más barato
  que desenredar.
- **Las sesiones ven los libros de las demás.** Los tests usan un archivo
  temporal, pero cuando un agente prueba el comando a mano usa el archivo de
  datos por defecto (`~/.shelf.json`), compartido por todos los worktrees. Define
  `SHELF_PATH` con un archivo distinto en cada worktree. Es la versión pequeña de
  las bases de datos y los puertos compartidos que te encontrarás en proyectos
  reales.
- **Git se niega a crear un worktree porque la rama ya está en uso en otro.**
  Ejecuta `git worktree list` y elige otro nombre de rama o elimina el worktree
  antiguo. Si has borrado carpetas de worktrees a mano, `git worktree prune`
  limpia los restos.
- **Un participante se bloquea con tres notificaciones pendientes.** Que baje a
  dos sesiones y atienda primero la de arriba. Es normal.
- **Se alcanzan los límites del plan a mitad de laboratorio.** En pareja: quien
  aún tiene cuota lleva las sesiones; la otra persona planifica los merges, lee
  los diffs y lleva el registro. Pasa una pista de poco riesgo a un segundo
  proveedor si alguien lo tiene. Apunta cuándo ocurrió: son datos para el
  laboratorio 8.
- **Un prompt acaba en la sesión equivocada.** Para eso tienen nombre las
  sesiones. Si la sesión se ha confundido, límpiala (`/clear` en Claude Code) o
  vuelve a arrancarla desde su prompt de arranque.
- **Quedan worktrees abandonados.** `git worktree list` y `git worktree remove`
  forman parte de "terminado".

**Pregunta a la sala:** "¿Qué hiciste mientras los tres agentes trabajaban, y
fue un buen uso de tu atención?"

### Módulo 07 — Agentes que revisan agentes

**Bloque:** día 2, 11:15–12:30 (demo de 20 minutos, laboratorio de 55 minutos).

**Demo:** abre una sesión *nueva* en el worktree del pull request:

```text
Revisa el pull request <number> de este repositorio. No recuerdas cómo se
construyó. Intención: <una frase>. Contexto: shelf es una herramienta local de
línea de comandos para un solo usuario; no está expuesta a internet. Informa
solo de errores de corrección, tests que falten para el comportamiento previsto
y desviaciones de la intención. Para cualquier otra cosa, pregúntame en lugar
de recomendarla. Da archivo:línea y pruebas de cada hallazgo.
```

Después ejecuta un revisor de un segundo proveedor (consulta la
[referencia de herramientas](../../content/es/reference/tools.md)). Construye en
directo el registro de triaje, con un veredicto por hallazgo: FIX_NOW,
DEFER_TO_ISSUE o DISCARD, cada uno con un motivo de una línea. Cierra el bucle
por decisión.

El laboratorio 7 está escrito para 75 minutos de trabajo por tu cuenta. En los
55 minutos de la sala, haz una ronda de revisión, aplica un lote de arreglos y
pasa directamente a la decisión de cierre. La segunda ronda queda como tarea.

**La idea que debe calar:** *quien escribe no debería ser el único revisor. La
declaración de intención es la regla de medir, y los bucles de revisión terminan
por decisión, no por agotamiento.*

**Fallos habituales:**

- **El revisor provoca que crezca el alcance.** Por ejemplo, "sanea la entrada
  contra inyección SQL" en una herramienta que guarda JSON, o "añade un sistema
  de plugins para los exportadores". Compara cada hallazgo con la intención y
  márcalo DISCARD o DEFER_TO_ISSUE con un motivo. Un buen ejemplo real sale de
  S5: un revisor puede darse cuenta de que, al borrar el libro más reciente, su
  id se puede reutilizar. La issue lo deja fuera de alcance, así que es
  DEFER_TO_ISSUE, no FIX_NOW. Cuenta aquí nuestra historia.

  > [!NOTE]
  > **En The Agile Monkeys** nuestro primer agente de triaje de revisiones
  > aceptaba todos los comentarios. Un pull request de unas 5.000 líneas
  > cambiadas creció hasta 20.000–40.000 mientras el revisor perseguía amenazas
  > improbables en una herramienta interna. La solución fue dar a los revisores el
  > objetivo del PR y el contexto del proyecto, y hacer que preguntaran a una
  > persona cuando tuvieran dudas.

- **El revisor lo aprueba todo.** Pide pruebas: "¿Qué test falla si se deshace
  este comportamiento? Deshazlo y ejecuta ese test." O apóyate en el revisor del
  segundo proveedor.
- **La tercera ronda encuentra problemas causados por los arreglos de la
  segunda.** Los hallazgos se han vuelto derivados. Clasifica, responde,
  resuelve y abre una única issue de seguimiento. En el workshop, dos rondas como
  máximo. Uno de nuestros pull requests grandes pasó por unas 20 rondas de
  revisión automática y más de 200 hilos antes de que aprendiéramos esto
  (indicativo).
- **Nadie en la mesa tiene un segundo proveedor.** Usa el mismo proveedor en una
  sesión nueva con un papel adversario, o intercambia pull requests con alguien
  que use otro proveedor.
- **Los comentarios de revisión publicados en GitHub inundan las notificaciones
  de todo el mundo.** Deja la primera ronda dentro de la sesión. Publica en
  GitHub una sola vez, para practicar responder y resolver hilos.
- **Aparece un hallazgo de seguridad en un proyecto de juguete.** Los hallazgos
  de seguridad nunca se descartan sin más. Clasifícalo con el contexto (una
  herramienta local de un solo usuario) y deja escrito el razonamiento. Ese
  hábito es la lección.

**Pregunta a la sala:** "¿Qué hallazgo descartaste, y defenderías esa decisión
ante un compañero?"

### Módulo 08 — Economía de tokens

**Bloque:** día 2, 13:30–14:20 (charla de 20 minutos, laboratorio de 30 minutos).

**Demo:** tus propios números, preparados de antemano: las cuotas de tus planes
prorrateadas a una semana, divididas entre los PR que mergeaste esa semana.
Después, tus principales sumideros de tokens. Oculta los datos de facturación y
de tu cuenta.

**La idea que debe calar:** *mide el coste por PR mergeado, no el coste por
token. Un uso intenso no es derroche si acaba en merge, y un uso escaso no es
ahorro si no se entrega nada.*

> [!NOTE]
> **En The Agile Monkeys** uno de nuestros ingenieros agotó en dos días el cupo
> semanal de un plan de gama alta, con unos 20 agentes que programaban, revisaban los pull
> requests de los demás y mantenían la base de conocimiento del producto. No
> había nada roto. El consumo sigue a la habilidad.

**Fallos habituales:**

- **Los planes gestionados por la empresa ocultan el uso.** Estima, marca el
  número como estimado y pregunta más tarde a quien administre las cuentas.
- **Un debate sobre precios de proveedores.** Los precios cambian cada pocos
  meses; el método no. Remite a las páginas de precios de los propios
  proveedores y sigue adelante.
- **Vergüenza, en cualquier dirección.** Un uso alto o bajo no es una nota. Lo
  que importa es la proporción con los resultados.
- **Los números del workshop parecen no significar nada** (dos PR en un día). Es
  así. El laboratorio 8 ensaya el cálculo, y el número real llega en la semana 4
  del seguimiento.
- **Llegar a los límites del plan como medalla.** Un límite es una señal para
  buscar sumideros: bucles de revisión que persiguen alcance nuevo, contexto
  cargado siempre e hinchado, sesiones que siguen mucho después de agotar su
  contexto útil.

**Pregunta a la sala:** "¿Qué único cambio reduciría tu uso de tokens sin
reducir lo que mergeas?"

### Sprint en paralelo

**Bloque:** día 2, 14:20–16:30 (presentación de 10 minutos, sprint de 90
minutos, revisión de 30 minutos).

**Preparación:** dibuja un tablero en la pared o en un documento compartido con
cuatro columnas: **Planificación** (agente), **En curso** (agente), **Listo para
una persona** (decide una persona), **Mergeado** (persona). Adelanta las
columnas humanas y de agentes del módulo 09. Al lado, lleva los totales de la
sala sin nombres: el máximo de sesiones que sostuvo una persona, PR mergeados,
rondas de revisión, PR revertidos.

**Presentación:** lee en voz alta las reglas del sprint de la
[página de workshops](README.md) y los objetivos por itinerario.

**Variante para grupos con experiencia:** tríos que comparten *un* repositorio.
Las carreras por hacer merge se vuelven reales. Nombra un responsable de merge
que rote cada 30 minutos; solo esa persona hace merge.

**Durante el sprint:** recorre la sala. En el minuto 25, haz una encuesta con
notas adhesivas: "Nota de OK si ya tienes escrita la conclusión de la discusión
sobre S7 y existen tus issues nuevas." En el minuto 45: "Nota de OK si ya has
mergeado al menos un PR." Recoge historias de fallos. Recuerda a la gente que se tome un descanso mientras sus
sesiones trabajan.

**Revisión del sprint:** enseña los totales, un registro de triaje en pantalla
(pide antes un voluntario) y el mejor fallo recuperado. Celebra las
recuperaciones.

**Fallos habituales:**

- **Todo el mundo llega a los límites del plan más o menos a la vez.** Parejas,
  abre la reserva de emergencia y pasa a quien se quede sin cuota a revisar pull
  requests de otras personas.
- **No se mergea nada porque las revisiones nunca se cierran.** Cierra por
  decisión tras dos rondas.
- **`main` se rompe después de un merge** (variante de repositorio compartido).
  Se paran los merges. Quien hizo el merge arregla hacia delante con un agente
  y después añade una barrera para lo que se rompió.
- **Alguien construye herramientas de orquestación en lugar de entregar.**
  Nombra la trampa agéntica y reconduce hacia las issues.
- **S7 se construye sin discusión.** Pide ver la conclusión de la discusión. Si
  no la hay, esa es la lección.
- **La discusión sobre S7 se come el sprint.** Córtala hacia los 20 minutos.
  Una opción suficientemente buena, dividida en dos issues pequeñas, enseña más
  que un plan perfecto sin nada mergeado.
- **Dos issues nuevas de S7 editan los mismos archivos.** Pide al agente que
  clasifique cada solapamiento, como en el laboratorio 5. Mismas líneas sin
  contrato compartido, por ejemplo dos opciones nuevas en `shelf list`, es un
  solapamiento textual: ejecuta las dos y resuélvelo al hacer merge. Dos issues
  que añaden campos al libro guardado son un conflicto semántico, otra vez C1 y
  C2: solo una puede quedarse con el siguiente `SCHEMA_VERSION`, así que decide
  el orden antes de que arranque cualquiera de las dos sesiones.
- **Una opción de S7 cambia el formato del archivo.** Casi todas las ideas para
  clubes de lectura lo hacen, y C2 ya lo versionó. La nueva issue tiene que subir
  `SCHEMA_VERSION` y añadir una migración. Buen trabajo para quienes tienen más
  experiencia.

### Seguimiento: módulos 09 y 10

**Bloque:** cuatro sesiones semanales (consulta la [página de workshops](README.md)).

**Cómo llevar las sesiones:**

- Se habla de números y de patrones, no de código. El código real solo va a la
  pantalla con permiso.
- La ronda de un número, breve, y nunca se clasifica a nadie.
- Las demos, con el proyecto de práctica, nunca con el repositorio de un
  participante.

**Demo de seguridad opcional (clínica de la semana 3):** en tu equipo de demo
aislado, sin ningún secreto, crea en el repositorio de práctica una issue cuyo
cuerpo contenga instrucciones dirigidas a un agente (por ejemplo, pedirle que
imprima las variables de entorno). Después pide a un agente que haga triaje de
las issues abiertas y observa si las sigue. Comenta con la sala la entrada no
confiable, la [trifecta letal](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
y por qué es una persona quien ejecuta los comandos con privilegios de
producción. Nunca lo hagas en un equipo con credenciales.

**Dónde se atasca la gente, semana a semana:**

- **Semana 1 (contexto).** Diseñan la base de conocimiento perfecta o se pasan
  la semana escribiendo documentación a mano. Presupuesto: una hora, y que la
  escriba el agente.
- **Semana 2 (barreras de seguridad).** Pasan días perfeccionando hooks. Basta
  con una barrera, para una regla que el agente se saltó de verdad. Vuelve a
  mencionar la trampa agéntica.
- **Semana 3 (pistas en paralelo).** Los repositorios reales necesitan
  servicios: puertos, bases de datos y archivos de entorno para cada worktree. En
  nuestros equipos, la memoria se agota con unos cinco o seis entornos locales
  completos (indicativo). Empieza por pistas que no necesiten el entorno (tests,
  documentación, herramientas de línea de comandos, refactorizaciones) y añade
  entornos por rama más adelante. Los compañeros que no estuvieron en el workshop
  pueden resistirse al acuerdo de trabajo: preséntalo como una propuesta
  respaldada por tus números.
- **Semana 4 (revisión y economía).** No se recogieron números. Reconstrúyelos
  con `gh pr list` y la vista de uso, y márcalos como estimados.

**Otras situaciones habituales:**

- **La empresa no permite agentes en el repositorio elegido.** No incumplas la
  política. Usa una herramienta interna o un proyecto de código abierto en el
  que el participante colabore, y lleva el acuerdo de trabajo al equipo como
  propuesta de piloto.
- **Hay abandonos.** Cuenta con ellos. Envía el mensaje semanal con un único
  objetivo y mantén los tríos como compañeros de compromiso.
- **Sectores regulados.** No conocemos a nadie que tenga todavía un flujo a la
  vez eficiente con agentes y que dé el control y la trazabilidad que exige el
  trabajo regulado. Dilo, recoge ideas e invita a abrir una issue de "share your
  practice".

## Planes B

| Problema | Primer paso (5 minutos o menos) | Si persiste | Prevención |
|---|---|---|---|
| **Cae la red del lugar** | El facilitador, al punto de acceso; los participantes pausan sus agentes | Pasa a un bloque sin conexión: descomponer el catálogo de issues impreso, revisar un plan y un diff impresos, construir un registro de triaje a partir de una revisión impresa, redactar un `AGENTS.md`. Proyecta las demos grabadas | Probar la red con agentes en marcha; llevar punto de acceso e impresiones |
| **Un proveedor sufre una caída** | Consultar la página de estado del proveedor; pasar a un segundo proveedor | Reordenar la agenda: charlas y trabajo sin conexión ahora, laboratorios después | Facilitadores con sesión en dos proveedores; pedir a quien tenga un segundo plan que lo traiga |
| **Límites de uso o del plan** | Parejas | Abrir la reserva de emergencia; pasar gente a tareas de revisión; bajar el número de sesiones en paralelo | Comprobación del plan en el trabajo previo; presupuesto de la sala |
| **Instalación rota** | Un ayudante, cinco minutos | Pareja con quien esté al lado; usar un entorno de desarrollo en la nube preparado de antemano | Comandos del trabajo previo y formulario de confirmación |
| **Portátil corporativo bloqueado** (proxy, sin permisos de administrador, CLI bloqueado) | Parejas | Un equipo de repuesto o una máquina virtual; pedir a la persona que traiga otro equipo el día 2 | Preguntarlo en el formulario de inscripción |
| **Un agente hace algo destructivo** | Parar la sesión; `git status`; restaurar desde git | Una copia nueva del proyecto de práctica | Ninguna credencial de producción; subir la copia de práctica a menudo |
| **Tu demo falla estruendosamente** | Nombrarlo; intentar una recuperación | Usar el kit para ponerse al día o la grabación, avisando; comentar el fallo | Ensayar en los 14 días anteriores |
| **Límites de GitHub o marcas de spam** | Parar las acciones masivas; ir más despacio | Seguir trabajando en ramas locales y revisar los diffs en local | Catálogo de issues pequeño; nada de generación masiva |
| **Vas con retraso** | Aplicar la lista de recortes | — | Temporizador visible |

Los agentes que usa esta guía funcionan con modelos en la nube, así que los
laboratorios necesitan red. No hay una versión sin conexión, y por eso existe el
bloque sin conexión.

## Presupuesto de costes para la sala

Alguien paga los tokens. Decide quién antes de abrir la inscripción.

**Tres formas de pagar:**

1. **Cada cual trae su plan.** Lo habitual en workshops abiertos. El trabajo
   previo pide comprobar los límites. Cuenta con que algunos planes de entrada
   se agoten el día 2.
2. **Licencias de la organización.** Asigna una licencia por persona al menos
   una semana antes, para que cada participante pueda prepararse en casa.
3. **Claves de API con límite de gasto estricto.** Una clave por participante o
   por pareja, cada una con su límite. Revócalas todas el mismo día en que acaba
   el workshop.

Nunca compartas con los participantes el acceso a una suscripción personal. Es
un problema de seguridad, y los planes suelen estar pensados para una sola
persona.

**Hoja de cálculo: mide, no adivines.**

| Línea | Cómo obtenerla |
|---|---|
| A. El día 1 de un participante | Haz tú todos los laboratorios del día 1 al ritmo del workshop y mira tu vista de uso |
| B. El día 2 de un participante | Haz los laboratorios 6–8 y un sprint de 90 minutos con 3–5 sesiones, y mira tu vista de uso. El día 2 suele costar varias veces lo que el día 1, porque las sesiones van en paralelo y los revisores vuelven a leer el código |
| C. Por participante | (A + B) × un margen de seguridad, por ejemplo 1,5, porque los participantes reintentan más que tú |
| D. La sala | C × número de participantes |
| E. Reserva de emergencia | Suficiente para que una quinta parte de la sala termine el día 2 con claves de API con límite |
| F. Facilitadores | Tu propio A + B otra vez, más los ensayos |

**Reglas:**

- Enseña con el modelo más potente al que tengas acceso. Un modelo más débil para
  ahorrar enseña límites equivocados. Si el presupuesto obliga a ceder, dilo en
  la sala.
- Pon límite a cada clave, nunca pongas claves en diapositivas ni en el chat, y
  revoca todas las claves del workshop al terminar.
- Pide a los participantes que apunten su uso al final de cada día. Son sus datos
  para el laboratorio 8.
- Los proveedores publican cifras de uso típicas, por ejemplo la
  [página de costes de Claude Code](https://code.claude.com/docs/en/costs) de
  Anthropic. Un día de workshop con sesiones en paralelo queda muy por encima de un
  día típico, así que toma esas cifras como un mínimo.

## Después del workshop

### Encuesta al final del día 2

Que dure menos de cinco minutos y sea anónima.

1. ¿Qué utilidad han tenido los dos días para tu trabajo? (1–5)
2. Ritmo del día 1 y del día 2: demasiado lento / adecuado / demasiado rápido.
3. ¿Qué módulo te ayudó más? ¿Cuál menos?
4. ¿Funcionó tu entorno? Si no, ¿qué falló?
5. El máximo de sesiones que mantuviste trabajando a la vez durante el sprint.
6. Confianza ahora, de 1 a 5, en las cinco habilidades del formulario de
   inscripción: diseñar tareas que un agente pueda verificar; mantener el
   contexto entre sesiones; ejecutar tres o más sesiones en paralelo; revisar
   pull requests de agentes con agentes; estimar el coste por PR mergeado.
7. La única cosa que harás distinto la semana que viene.
8. ¿Qué te sonó a exageración, o a error? ¿Qué deberíamos cambiar?
9. ¿Podemos usar agregados anónimos de tus respuestas para mejorar la guía?
   (sí / no)

### Encuesta al final de la semana 4

1. Tu tabla de antes y después de las seis métricas (del laboratorio 10).
2. ¿Qué práctica se ha quedado? ¿Cuál abandonaste, y por qué?
3. ¿Se resintió la calidad? PR revertidos, bugs, incidencias, retrabajo.
4. Confianza ahora, de 1 a 5, en las mismas cinco habilidades.
5. ¿Ha adoptado algo tu equipo? ¿Qué lo ha frenado?
6. ¿Recomendarías el workshop a un compañero? ¿Por qué sí o por qué no?
7. ¿Podemos usar agregados anónimos? (sí / no)

### Plantillas de mensajes

**El mismo día, después del día 2:**

```text
Asunto: Agentic Engineering 101: tus próximas cuatro semanas

Hola, <nombre>:

Gracias por estos dos días. Tres cosas antes de mañana:

1. Encuesta (5 minutos, anónima): <enlace a la encuesta>
2. Limpieza: haz commit y push de tu repositorio de práctica, elimina los
   worktrees que creaste (git worktree list) y asegúrate de que no queda ninguna
   clave de API del workshop en tu equipo. Esta noche las revocamos.
3. La semana 1 del seguimiento empieza ya. Foco: contexto. En tu repositorio
   real, crea AGENTS.md y una carpeta kb/ con ACTIVE.md. Guía: <enlace a la
   lección 04> y <enlace a la lección 10>.

Sesiones semanales: <día y hora>, cada semana durante cuatro semanas:
<enlace de vídeo>. Trae un número: el máximo de sesiones que mantuviste
trabajando a la vez.

<nombre del facilitador>
```

**Antes de cada sesión semanal:**

```text
Asunto: Sesión <n> de 4: <foco de la semana>

Hola a todos:

Foco de esta semana: <contexto | verificación y barreras de seguridad | pistas
en paralelo | revisión con agentes y economía>.

Lo único que hay que probar antes del <día>: <un objetivo concreto>.
Trae: <qué traer, según la página de workshops>.

¿Atascado? Escribe en <canal de chat> qué le pediste al agente y qué te
respondió.

Sesión: <día y hora>, <enlace de vídeo>.
```

**Después de la sesión final:**

```text
Asunto: Agentic Engineering 101: resultados y próximos pasos

Hola a todos:

Gracias por cuatro semanas de práctica. El antes y después anónimo de la
cohorte: <tabla agregada>. Recuerda que estos números son indicativos, no un
benchmark.

Dos peticiones:
1. Encuesta final (5 minutos): <enlace a la encuesta>
2. Comparte con la comunidad de la guía una práctica que hayas descubierto, en
   una issue de "share your practice":
   https://github.com/theam/agentic-engineering-101/issues/new?template=share-your-practice.yml

La guía sigue cambiando al ritmo de la práctica. No la pierdas de vista y
avísanos cuando algo esté mal o se haya quedado desactualizado.

<nombre del facilitador>
```
