---
title: "Un agente, bien usado · Lectura"
kind: reading
last_reviewed: 2026-11-27
---

# Módulo 02 · Un agente, bien usado

<!-- Versión escrita del módulo para Agentic Engineer Academy. Una parte por vídeo, en el mismo orden. Formato: docs/reading-format.md. -->

## Parte 1 · Háblale como a un compañero

<!-- minutes: 4 -->

> Las preguntas que importan muchas veces se resuelven en una conversación de dos minutos, antes de que exista código. Háblale al agente como a un compañero que comparte tu contexto.

### El sitio más caro para encontrar un problema

Así es como se tuerce una tarea pequeña. Shelf es el pequeño proyecto de práctica que usas en los labs.

Le pides al agente que "añada un comando de estadísticas a shelf". Escribe 150 líneas, incluido un flag --json que no has pedido. Abres el diff, la lista de líneas cambiadas, y empiezas a leer.

A las veinte líneas encuentras el problema de verdad. "Libros terminados este año" cuenta cada libro con estado done cuya fecha cae en el año en curso. Pero ¿qué pasa con un libro que añadiste ayer como ya leído y que terminaste hace años? ¿Y "este año" en qué zona horaria? Las marcas de tiempo se guardan en UTC, y tú vives en Madrid o en Bogotá.

Lo corriges. El agente lo parchea. Se rompe un test en otro archivo. Vuelves a corregir. Cuarenta minutos después, la sesión es un montón de arreglos a medias y ya no sabes cuáles siguen haciendo falta.

**Nada de eso fue un fallo del modelo.** Las dos preguntas que importaban se podían haber hecho en una conversación de dos minutos, antes de que existiera código. En cambio, las encontraste dentro de un diff, que es el sitio más caro para encontrar cualquier cosa.

Este módulo trata de un agente haciendo bien una tarea, lo que el curso llama el ciclo interno. El ciclo interno consiste en **adelantar las correcciones**: del diff al plan, y del plan a la conversación.

### Un compañero, no un buscador

Lo largos que deben ser tus mensajes depende de cuánto sabe el otro lado. A un buscador le das una consulta larga y autocontenida, porque no sabe nada de ti. A un compañero le mandas mensajes cortos, porque compartes contexto con él: el código, las decisiones de la semana pasada, lo que intentas conseguir.

Un agente de programación puede ser cualquiera de los dos, y tú decides cuál. Una sesión es una conversación con un agente. Los archivos de instrucciones son archivos del repositorio que el agente lee al empezar cada sesión. En una sesión abierta en tu repositorio, con archivos de instrucciones y unas cuantas vueltas de conversación, los mensajes cortos funcionan: "¿y los libros añadidos como done?", "no, deja la salida en texto plano".

**Si sigues escribiendo largos "prompts perfectos" que vuelven a explicar el proyecto, tómalo como una señal de alarma:** estás tecleando el contexto que le falta a la sesión. Arregla el contexto, no el prompt. El módulo 04 enseña cómo.

Cuéntale al agente el problema que tienes, no los pasos que hay que dar.

> No le digo adónde vamos. Le digo el problema que tengo (traducción propia).
>
> David Heinemeier Hansson (DHH), el creador de Ruby on Rails, sobre cómo trabaja hoy con agentes.

Corto no es impreciso en lo que importa. Cuando pasas una tarea a una sesión sin historia, la estructura ayuda: las buenas prácticas de Codex, la guía de OpenAI para su agente de programación, proponen objetivo, contexto, restricciones y "cuándo está terminado". El módulo 05 trata esos prompts de traspaso. Dentro de una conversación en marcha casi nunca hacen falta.

### En la práctica

En The Agile Monkeys, la empresa que está detrás de este curso, quienes trabajan con muchos agentes dicen que ya no "escriben prompts". Planifican conversando, dentro de una sesión abierta en un repositorio que ya contiene el contexto del proyecto y las decisiones pasadas:

- "Quiero hacer X, ¿cómo lo harías?"
- "Hazlo así."
- "No, prefiero esta otra forma."

Cuando el plan está listo: "convierte este plan en issues de GitHub; si es grande, divídelo en una épica". Una issue es una tarea escrita en GitHub, y una épica es una issue grande hecha de otras más pequeñas. Al cabo de unas semanas, el repositorio ha aprendido las convenciones y basta con "crea una issue".

### Habla en tu idioma, escribe en uno

Planificar conversando encaja con la voz. Hablar es más rápido que teclear cuando piensas en voz alta, y los agentes le sacan un sentido sorprendente a pensamientos dichos sin pulir.

**Piensa en voz alta con el agente en lugar de dictarle.** No necesitas frases terminadas. Divaga, cambia de idea a mitad ("no, olvida eso, prueba de la otra forma") y deja que el agente lo convierta en una estructura que puedas corregir. Recupera tu intención incluso de una mala transcripción: un "¿ese commit fue directo a main?" dicho con cansancio puede salir como "exit en commit directo a main", y el agente aun así pregunta si el commit fue directo a main. Quien no lo ha probado suele suponer que hacen falta frases limpias y ordenadas. Pruébalo una semana antes de decidir.

El dictado es un modo. Algunas herramientas ofrecen además una conversación por voz en tiempo real, que algunos preferimos para repasar una tarea o un trozo de código. En Claude Code, el agente de programación de Anthropic, el comando /voice activa el dictado: mantén pulsada la barra espaciadora y habla.

En The Agile Monkeys muchos hablamos con los agentes en español, a menudo por voz. Tenemos una regla fija en nuestros repositorios: todo lo que se guarda se escribe en inglés, es decir, código, comentarios, commits, pull requests, issues y documentación. Un pull request es un cambio propuesto, que se revisa antes de entrar en el código principal. No hemos visto problemas por mezclar los dos idiomas.

Pon la misma regla en tu archivo de instrucciones, para que cada sesión la siga sin que se lo digas. La escribimos en inglés, como el resto de lo que se guarda: "Talk to the user in the language they use. Write every persisted artifact (code, comments, commit messages, pull request and issue text, documentation) in English."

**Ten cuidado con los identificadores, los números y los nombres de archivo.** Cuando importen, pégalos en lugar de decirlos, y lee la transcripción antes de enviarla.

### Ideas clave

- Los problemas salen más baratos si los encuentras conversando, antes de que exista código.
- Los "prompts perfectos" largos delatan contexto que falta. Arregla el contexto.
- Piensa en voz alta en cualquier idioma. Escribe lo que se guarda en uno.

## Parte 2 · El ciclo

<!-- minutes: 5 -->

> Explorar, conversar, planificar, construir, verificar y hacer commit. Separa el hablar del construir: el agente solo construye cuando tú lo dices.

### Seis pasos

Cada tarea que le das a un agente pasa por seis pasos: explorar, conversar, planificar, construir, verificar y hacer commit. Abajo va cada uno, y después cuándo saltarse un paso y cuándo volver atrás.

### Explorar

El agente lee antes de escribir. Hazle preguntas cuya respuesta está en el código, y dile que no cambie nada. En shelf, el modelo es el código que define un libro y el store es el código que lo guarda: "Lee el modelo, el store y el comando list. ¿Cómo cambia el estado de un libro y qué se guarda cuando eso ocurre? No cambies nada."

Cuando el agente te pregunte cosas que el código podría responder, devuélvelo a la fuente. Peter Steinberger, un ingeniero que lleva muchos agentes en un proyecto que construye casi en solitario, usa una sola frase para eso: "Lee más código para responder tus propias preguntas" (traducción propia). En el lab 2, cada vez que tengas que devolvérselo cuenta como una corrección.

### Conversar

Pide opciones con sus pros y contras, y elige. DHH lo llama "Evaluación diferencial. Me das tres opciones y elijo una" (traducción propia). Elegir entre tres diseños concretos funciona mejor que describir el correcto desde cero.

Los agentes tienen ganas de construir, así que deja claro cuándo no deben hacerlo. Steinberger usa unas frases disparadoras:

> En cuanto digo "hablemos" o "dame opciones", no construyen nada hasta que digo "construye" (traducción propia).
>
> Peter Steinberger, sobre cómo evita que los agentes construyan demasiado pronto.

Di "no escribas código hasta que te diga que construyas". Si dudas de que te haya hecho caso, ejecuta git status, que lista los archivos que han cambiado.

Si el agente no ve un caso que tú sí ves, no le des la respuesta todavía. Pregunta "¿Qué datos harían que estas cuentas salieran mal?". Si sigue sin verlo, díselo.

```prompt-weak
añade un comando de estadísticas
```

```prompt-strong
Hablemos de la issue #3 (shelf stats) antes de construir. Lee primero la
issue, el modelo y el store. Después dime qué casos no resuelve la issue,
dame opciones para cada uno con sus pros y contras, y recomienda una.
No escribas código hasta que te diga que construyas.
```

El prompt mejor abre una conversación, no una construcción:

- **Lee primero:** la issue, el modelo y el store.
- **Pide los casos abiertos,** con opciones y una recomendación.
- **Frena la construcción** hasta que tú lo digas.

La issue #3 es la tarea de estadísticas del proyecto de práctica. En tu repositorio puede tener otro número. El lab 2 explica cómo crearla.

### Planificar

Antes de que ejecute, pide al agente que explique qué va a hacer. Un plan que puedes revisar en un minuto incluye:

- los archivos que va a cambiar,
- cualquier cambio en los datos o en el almacenamiento,
- el comportamiento en los casos límite,
- los tests que lo demostrarán, y que fallarían sin el cambio,
- lo que no va a hacer.

La parte 4 explica cómo pedir el plan y cómo corregirlo.

### Construir y verificar

**Construir.** Di "construye" de forma explícita. Pide al agente que escriba primero los tests y los ejecute para enseñarte que fallan: un test que nunca falló no demuestra el cambio. Después implementa, y tú no miras. Si ejecuta el comando a mano, que use un archivo temporal, para no tocar nunca tus datos reales. En el lab 2, para eso está la variable de entorno SHELF_PATH.

**Verificar.** El agente te enseña la salida de los tests que ejecutó. Las buenas prácticas de Claude Code, la guía de Anthropic para su agente de programación, lo formulan así: "Haz que Claude muestre pruebas en lugar de afirmar que ha terminado bien" (traducción propia). No aceptes un "terminado" sin pruebas: pide el comando que ejecutó y su salida. Después:

- **Comprueba tú el alcance.** git status y git diff --stat enseñan qué archivos han cambiado.
- **Mira la salida real** del comando, no un resumen.
- **Calcula tú la salida esperada** antes de leer la del agente. Si no coinciden, pregunta por qué antes de aceptar ninguna explicación.

El módulo 03 trata entero sobre este paso.

### Hacer commit

Pequeño, con un mensaje que recoja las decisiones y no solo el cambio. En el lab 2, la descripción del pull request también explica cada decisión y lo que se gana y se pierde con ella.

Kent Beck, conocido por el desarrollo guiado por tests, separa en commits distintos los cambios estructurales y los de comportamiento: los que reorganizan el código, aparte de los que cambian lo que hace. Ese hábito hace mucho más fácil revisar el trabajo de un agente.

### Cuándo saltarse un paso y cuándo volver atrás

No todo cambio necesita un plan. La regla práctica de Anthropic: "Si pudieras describir el diff en una frase, sáltate el plan" (traducción propia). Renombrar un flag, corregir una errata en un mensaje de error o añadir una línea de log pueden ir directamente a construir y verificar. Un comando de estadísticas con una decisión de fechas dentro no se describe en una frase, así que necesita un plan.

El ciclo también vuelve atrás:

- **Falla la verificación:** vuelta a construir.
- **El plan parte de una suposición equivocada:** vuelta a conversar.
- **Lo construido está mal de raíz:** vuelta a conversar.

### El ciclo por defecto

En The Agile Monkeys seguimos este ciclo en nuestros portátiles con claude-dev-kit, un plugin open source que mantenemos. Un plugin es un complemento que le da al agente comandos ya hechos. Funciona en Claude Code y en Codex. En Claude Code, su comando /work-story lee la issue, propone un plan y no escribe código hasta que alguien lo aprueba. Después construye, comprueba los tests del proyecto y la cobertura mínima de tests que pide, hace una revisión de seguridad y una autorrevisión, y abre el pull request con las pruebas.

No sustituye el criterio de este módulo: sigues conversando, corrigiendo el plan y tirando el trabajo cuando está mal de raíz. Lo que cambia es que los pasos ocurren por defecto, en lugar de depender de un hábito que tienes que recordar. **No necesitas este plugin, ni ningún otro.** El apéndice del curso "Construye tus propias skills" enseña a escribir este mismo ciclo como una skill tuya: un paquete de instrucciones que el agente carga cuando hace falta.

### Ideas clave

- Explorar, conversar, planificar, construir, verificar y hacer commit.
- El agente solo construye cuando dices "construye".
- Pide pruebas, no un "terminado".
- Sáltate el plan solo si el diff cabe en una frase.

## Parte 3 · Cuánto decir

<!-- minutes: 2 -->

> Hay dos consejos opuestos sobre cuánto decirle a un agente, y los dos tienen razón en momentos distintos. Di poco cuando quieras ideas. Sé preciso en lo que el código no le puede contar.

### Di menos para descubrir

Di menos cuando todavía no sabes lo que quieres. Steinberger lo hace a propósito:

> Le doy al agente menos indicaciones a propósito, para que haga algo que me dé ideas nuevas (traducción propia).
>
> Peter Steinberger

Reconoce que casi todo lo que vuelve no sirve, pero un par de ideas suelen merecer la pena. DHH defiende lo mismo desde la tradición ágil: nadie sabe qué debe hacer un software hasta que lo usa. En sus palabras: "Sé todo lo vago que puedas para que se materialice algo, y después interactúa con ese algo" (traducción propia).

### No dictes cada paso

Los expertos pueden empeorar los resultados si lo prescriben todo. DHH cuenta, de segunda mano y sin que se pueda verificar, que un proveedor de agentes recortó mucho su prompt de sistema porque al agente "lo estaban perjudicando humanos demasiado prescriptivos" (traducción propia). El prompt de sistema son las instrucciones fijas que un proveedor le da a su propio agente.

El patrón es conocido: si dictas cada paso, el agente sigue tus pasos incluso donde su propia lectura del código habría encontrado un camino mejor. **Prescribe el resultado y las restricciones que el código no le puede contar, no los pasos.**

### Lo que el código no cuenta

El agente no puede leer esto en el repositorio, así que si no se lo dices, lo adivinará:

- las decisiones ya tomadas,
- los invariantes, lo que siempre tiene que cumplirse, y las reglas sobre los datos,
- las restricciones de seguridad,
- las interfaces de las que dependen otras personas,
- lo que queda fuera de alcance.

### Tres momentos

| | Descubrir | Entregar | Reparar |
|---|---|---|---|
| | No sabes lo que quieres. | Sabes qué, no cómo. | Salió mal de raíz. |
| Cuánto decir | Poco. Pide opciones. | Preciso en el resultado y las restricciones. Nada sobre los pasos. | Dirección explícita, en una sesión nueva. |

Cómo suena cada uno con shelf:

- **Descubrir:** "Shelf debería ser más útil para clubes de lectura. Dame tres direcciones muy distintas entre sí."
- **Entregar:** "Stats muestra una línea por estado más 'finished this year': año natural en UTC, como las marcas de tiempo guardadas. Texto plano, sin flags."
- **Reparar:** "Empieza de nuevo. No toques el almacenamiento; calcula las estadísticas solo con los campos que ya existen."

### Ideas clave

- Di poco cuando quieras ideas.
- Sé preciso con el resultado y con las restricciones que el código no cuenta.
- No dictes los pasos, aunque seas quien sabe.

## Parte 4 · Revisa la intención, no las líneas

<!-- minutes: 5 -->

> En cualquier cambio que no sea trivial, lo primero que revisas es un plan, no un diff. Corrígelo en una frase.

### Un minuto o veinte

Un plan se lee en un minuto. Un diff de 400 líneas lleva veinte, y aun así se te puede escapar la suposición equivocada que esconde. El equipo que escribió la guía de HumanLayer sobre ingeniería de contexto para agentes de programación lo resume sin rodeos: "una mala línea de un plan puede acabar en cientos de líneas de código malas" (traducción propia).

Cuánto código lees después depende del riesgo, y el módulo 07 explica cómo. Lo que no cambia: **que el diff no sea nunca el primer sitio donde descubres lo que ha decidido el agente.**

### Dos formas de conseguir un plan

| | Modo plan | Conversación |
|---|---|---|
| | Un modo de solo lectura. El agente explora y propone un plan sin editar archivos. | Lo hablas, y después dices "explica qué vas a hacer" y luego "ok". |
| Dónde está | Uno de los modos de permisos de Claude Code. Codex tiene su propio modo plan. | En cualquier sesión |
| Quién lo defiende | Anthropic, y la guía de Codex para trabajo difícil o ambiguo | Peter Steinberger, desde finales de 2025 |
| Cuándo lo usamos | Con un agente que se pone a editar demasiado pronto, o en cambios de varios archivos sobre código que no conocemos | En una sesión que ya tiene mucho contexto |

Steinberger recomendaba el modo plan. Unos meses después, a finales de 2025, escribió que "El modo plan parece un apaño que hacía falta con generaciones anteriores de modelos" (traducción propia), y ahora consigue lo mismo conversando y con palabras clave. **Su cambio de opinión es la lección de verdad:** el mejor mecanismo depende de los modelos de esta temporada. El objetivo no cambia.

En The Agile Monkeys usamos el mecanismo que nos mantenga revisando la intención y no las líneas. El lab 2 te propone probar los dos en sus tres primeros pasos, y apuntar cuál te mantuvo revisando la intención.

### Pide el plan y corrígelo

Un prompt de revisión de plan que funciona: "Antes de construir, escribe el plan en menos de 25 líneas: archivos que vas a cambiar, cualquier cambio en los datos guardados y cómo se siguen cargando los archivos existentes, la salida exacta (con un ejemplo), los tests que vas a añadir y por qué fallaría cada uno sin el cambio, y lo que no vas a hacer. Después espera."

Responde con correcciones de una frase:

- "No añadas --json, eso es otra issue."
- "Usa el año natural en UTC, como las marcas de tiempo guardadas."
- "Los tests no pueden depender de la fecha de hoy; escribe el archivo de la estantería con marcas de tiempo fijas."

La última es una de las dos decisiones que te pide el lab 2: cómo probar "este año" sea cual sea el año en que se ejecuten los tests. Las marcas de tiempo fijas son una opción. Otra es una función de conteo que recibe la fecha de hoy como parámetro, no como opción de la línea de comandos, porque elegir el año queda fuera de alcance. También puedes usar las dos.

### Deja que el agente dibuje el sistema

Algunos problemas son difíciles de ver en planes o diffs, porque viven en cómo interactúan las piezas. Para esos, pide al agente que genere a partir del código una descripción visual del sistema, léela y corrígela en una o dos frases.

En The Agile Monkeys, uno de nuestros ingenieros llegó a la conclusión de que todo el enfoque de un sistema estaba mal y estaba a punto de rehacerlo. Antes, pidió al agente un documento visual de arquitectura generado a partir del código. El problema de verdad saltó a la vista: cuando un paso fallaba, nada lo registraba. La corrección cupo en una frase. El agente propuso un plan, recibió un "ok", arregló el código y actualizó el documento.

#### 1 · No lo edites tú

Es una herramienta para pensar, no el entregable. Editarlo a mano te cuesta tiempo y no le enseña nada al agente. Dile al agente qué está mal y deja que arregle el código y el documento a la vez.

#### 2 · Dibujos, no párrafos

Los diagramas de flujo, los de secuencia y las tablas se comprueban más rápido que la prosa. Una flecha equivocada se ve de un vistazo.

#### 3 · Ánclalo al código

Un diagrama generado puede mostrar el diseño que el agente espera en lugar del que existe. Pídele que cite archivo y línea para cada flecha.

Para shelf, el prompt podría ser: "Lee el código de shelf/ y escribe docs/architecture.md con: un diagrama de flujo en Mermaid de cómo viaja un comando desde la línea de comandos hasta el archivo JSON, un diagrama de secuencia de 'shelf finish 3' y una tabla con cada punto que lee o escribe el archivo. Cita archivo y línea para cada elemento. Marca todo lo que hayas deducido en lugar de leído." Mermaid es un formato de texto que se convierte en diagramas. En el lab 2 es un ejercicio extra.

### Que lo que vuelve sea fácil de leer

La regla del dibujo sirve para todo lo que lees, no solo para la arquitectura. Tu ancho de banda te limita en las dos direcciones. La información entra cuando le hablas al agente, cuando le das objetivos completos y cuando le señalas las fuentes en lugar de resumírselas. El módulo 04 trata ese lado. La información sale en forma de planes, explicaciones, informes y revisiones, y un muro de texto tarda lo mismo en leerse aunque lo haya escrito un agente.

- **Las explicaciones vienen con un dibujo.** Un diagrama de flujo de lo que cambia un pull request, una tabla con los casos que cubre una issue, un diagrama de secuencia de un bug. Si un párrafo necesita un diagrama para entenderse, pide el diagrama.
- **Los informes, como una pequeña página HTML.** Para un informe de estado, una comparación o un panel, pide un único archivo HTML autocontenido con tablas y gráficos. Cuando algo está mal, lo dices y el agente corrige una línea. Una imagen generada con tres palabras mal hay que volver a generarla.
- **Escribe una vez cómo entiendes mejor las cosas,** como una skill personal, y reutilízala con cualquier issue, pull request o pregunta. Por ejemplo: empieza con una frase sobre lo que cambia para el usuario, luego un diagrama que cite archivos y líneas, tablas mejor que párrafos, y termina con lo que el agente no tiene claro.

En The Agile Monkeys muchos hemos dejado de leer informes largos de texto. Pedimos un diagrama o una pequeña página HTML, la revisamos en una fracción del tiempo y respondemos con preguntas sobre el dibujo.

### Ideas clave

- Revisa el plan antes que el diff, y corrígelo con mensajes de una frase.
- Si el problema está en cómo interactúan las piezas, pide al agente que dibuje el sistema y corrige el dibujo a través del agente.
- Pide lo que lees más rápido: un diagrama, una tabla o una pequeña página HTML.

## Parte 5 · Pregunta, y si hace falta, tira el trabajo

<!-- minutes: 3 -->

> Después de construir, unas pocas preguntas cortas encuentran problemas que nadie buscaba. Cuando el trabajo está mal de raíz, tíralo y empieza de nuevo. Sale barato.

### Preguntas que se pagan solas

Unos pocos prompts cortos encuentran problemas que no buscabas ni tú ni el agente.

#### 1 · "¿Tenemos algún efecto secundario?"

Hace que el agente mire más allá de las líneas que ha cambiado. Steinberger encontró un bug oculto en un trigger de base de datos solo cuando lo preguntó.

#### 2 · "Ahora que lo has construido, ¿qué habrías hecho de otra manera?"

Después de construir, el agente conoce el código mejor que cuando planificó. La respuesta suele contener la refactorización que merece la pena.

#### 3 · "Hazlo más simple."

Los agentes añaden capas y código defensivo. DHH cuenta que le dice a un agente que un cambio terminado y revisado "parece un poco demasiado complicado" (traducción propia), y el agente lo reduce a la mitad.

#### 4 · "¿Qué has supuesto sin comprobarlo?"

Convierte las suposiciones ocultas en una lista que puedes revisar.

#### 5 · "¿Qué no has ejecutado, y por qué?"

Separa "los tests pasan" de "pasan los tests que existen y que se han podido ejecutar".

#### 6 · No "¿esto está bien?"

Los agentes tienden a dar la razón a quien pregunta. Pregunta mejor "¿cuál es el mejor argumento de que esto está mal?".

### Lo que harías distinto es una propuesta

Trata las respuestas a "¿qué habrías hecho de otra manera?" como propuestas, no como órdenes. Para cada sugerencia, decide:

- **Hazla ahora,** si es pequeña y cabe en el alcance del cambio.
- **Apúntala para después,** como una issue.
- **Descártala.**

Que lo que se ve a toro pasado no haga crecer el cambio.

### Tirar trabajo es barato

Cuando el código era caro, parchear una implementación equivocada tenía sentido. Ahora muchas veces no lo tiene. Simon Willison, un desarrollador que escribe una guía de patrones de agentic engineering, titula ese capítulo "Writing code is cheap now" (escribir código ahora es barato).

Steinberger cambió una suposición central de la arquitectura de su proyecto, de un agente a muchos, en unas tres horas con un agente. Calcula que a mano le habría llevado dos semanas.

### Cuándo empezar de nuevo

Las buenas prácticas de Claude Code dan un umbral concreto: después de dos correcciones fallidas sobre el mismo problema, para, limpia la sesión y empieza de nuevo con un prompt mejor.

> Una sesión limpia con un prompt mejor casi siempre supera a una sesión larga con correcciones acumuladas (traducción propia).
>
> Buenas prácticas de Claude Code, de Anthropic

Empieza de nuevo en lugar de parchear cuando:

- la implementación está mal de raíz: modelo de datos equivocado, capa equivocada, abstracción equivocada,
- has corregido dos veces el mismo problema y sigue mal,
- el agente está arreglando sus propios arreglos,
- la sesión está llena de enfoques fallidos que se vuelven a colar.

Todo lo de una sesión comparte su ventana de contexto: la memoria de trabajo del modelo para esa sesión. Guarda la conversación, los archivos que leyó el agente y la salida de sus comandos, y los resultados empeoran a medida que se llena. Por eso también perjudica mezclar tareas: una tarea, luego una pregunta sin relación, luego vuelta a la tarea. Una tarea por sesión, y limpia o empieza de nuevo entre tareas que no tienen que ver.

### Cómo empezar de nuevo

Empezar de nuevo bien lleva tres pasos:

- **Pide las lecciones.** En la sesión que falla: "Resume en 10 puntos como máximo lo que hemos aprendido: restricciones descubiertas, enfoques que fallaron y por qué."
- **Descarta la rama.** No hay nada valioso en ella. En el lab 2 quitas el worktree y creas uno limpio, y el lab te da los comandos.
- **Abre una sesión nueva.** Pega los puntos y tus decisiones hasta ahora, y da una dirección explícita: primero el plan, y que espere.

```prompt-weak
sigue mal, la cuenta anual vuelve a fallar. arréglalo
```

```prompt-strong
Empezamos de nuevo con shelf stats. Lecciones del primer intento:
- las marcas de tiempo de fin se guardan en UTC; "este año" es el año natural en UTC
- los tests del cambio de año fallaban según el día en que se ejecutaban; usa marcas de tiempo fijas
- el primer intento cambió el almacenamiento y rompió la carga; el almacenamiento no se toca
Primero el plan: calcula las estadísticas solo con los campos existentes,
enséñame el plan y un ejemplo de la salida, y espera a mi ok.
```

El prompt mejor le da a la sesión nueva lo que aprendió la primera:

- **Las restricciones** que se descubrieron.
- **Lo que no cambia.**
- **Primero el plan,** y esperar a tu ok.

En el lab 2, empezar de nuevo es opcional: lo practicas si fallaron dos correcciones sobre el mismo problema. Cuenta como un éxito. Apúntalo como una corrección.

### Ideas clave

- Después de construir, pregunta por los efectos secundarios y por lo que el agente haría distinto.
- No preguntes "¿esto está bien?". Pide el mejor argumento de que está mal.
- Tras dos correcciones fallidas, recoge las lecciones y empieza una sesión nueva.

## Parte 6 · Tu registro de correcciones

<!-- minutes: 3 -->

> Cada corrección te dice que faltaba algo. En el lab 2, apuntarlas todas es lo que de verdad sale del lab.

### Lo que te pide el lab 2

En el lab 2 implementas S3, una issue del proyecto de práctica shelf, que los prompts del lab llaman #3: un comando de estadísticas que muestra cuatro líneas de cuentas. Un agente y el ciclo completo. La issue fija mucho: las cuatro líneas en orden, ceros en una estantería vacía, UTC, y que solo cambian el comando nuevo y su archivo de tests. También deja cosas fuera de alcance: estadísticas por autor o etiqueta, gráficos y una opción para elegir el año.

S3 parece trivial. No lo es. Aun así, deja abiertas decisiones fáciles de pasar por alto:

- cómo probar "este año" sin depender del día en que se ejecutan los tests,
- qué hacer con datos que la issue no menciona. Un libro se puede añadir directamente como done. Y shelf todavía no comprueba los estados, así que un archivo de la estantería ya puede tener un estado que no sea to-read, reading ni done.

Se trata de encontrarlas en la conversación, no en el diff.

### Antes de empezar

Partes de tu propia copia del proyecto de práctica del lab 0, con sus tests pasando en main. Trabajas en un worktree nuevo: una carpeta más del mismo repositorio, en su propia rama. El lab te da los comandos. Abre ahí una sesión. También puedes hacer el lab en tu propio repositorio: elige una funcionalidad pequeña que esconda una pregunta de definición, como una cuenta, un rango de fechas o una zona horaria.

Usa el modelo más potente al que tengas acceso para planificar, diseñar la arquitectura, depurar y revisar. Los errores de un modelo más flojo cuestan tu atención, el recurso más escaso que tienes. Pasa un trabajo a un modelo más barato solo cuando tengas pruebas: una evaluación con tus propias tareas, o datos de coste que muestren que rinde igual.

Lo barato puede funcionar para volumen bien especificado. DHH describe una migración larga, reescribir código existente para que funcione en otro sitio, que varios modelos más baratos completaron por una fracción del coste. Uno intentó hacer trampa envolviendo una implementación existente y nunca terminó. Se sabe midiendo. El módulo 08 lo trata a fondo.

### El registro de correcciones

Mientras trabajas, lleva un registro de correcciones: una línea cada vez que tengas que corregir al agente. El pull request es el resultado visible, pero el registro es lo que de verdad sale de este lab. El lab 4 convierte algunas de esas líneas en reglas.

Guárdalo en tus notas, no en el repositorio. Cada fila dice:

- **Etapa:** en qué paso del ciclo pasó.
- **Qué corregiste.**
- **Qué faltaba.**
- **Qué lo habría evitado.**

### Qué faltaba

Cada corrección apunta a una de cinco causas:

- **Contexto:** el agente no podía saberlo.
- **Verificación:** podía haberlo comprobado y no lo hizo.
- **Decisión:** una elección de producto que nadie había tomado.
- **Instrucción:** lo sabía y no hizo caso.
- **Modelo:** un error sin más.

### Qué lo habría evitado

Al final del lab, rellena la última columna de cada fila:

- **Una línea en el archivo de instrucciones,** para contexto o instrucción. Módulo 04.
- **Una comprobación que el agente ejecuta solo,** para verificación. Módulo 03.
- **Una pregunta mejor al conversar,** para una decisión. Este módulo.
- **Nada:** era una decisión de criterio de verdad.

### Dónde corriges

Después, mira el registro entero:

- **¿Dónde se concentraron las correcciones?** ¿Al conversar y planificar, o al construir y verificar? Cuanto antes llega una corrección, más barata sale.
- **¿Qué causa domina?** Muchas filas de contexto significan que tu repositorio necesita mejores instrucciones. Muchas de verificación, que el agente necesita mejores comprobaciones. Muchas de decisión, que estás delegando elecciones que son tuyas.
- **¿Cuál fue tu mensaje más largo?** ¿Suplía contexto que la sesión debería haber tenido ya?
- **¿Encontró el agente las preguntas abiertas, o las encontraste tú?** Si fuiste tú, ¿qué le habría hecho falta para encontrarlas solo?

### Ideas clave

- En el lab 2, lo que de verdad sale es el registro de correcciones.
- Cada corrección lleva su etapa, su causa y qué la habría evitado.
- Usa el modelo más potente salvo que tengas pruebas de que uno más barato rinde igual.
