---
title: "Patrones de prompts"
kind: reference
last_reviewed: 2026-09-17
---

# Patrones de prompts

Prompts comentados que usamos, o que han publicado profesionales de referencia, en el espíritu del capítulo "Prompts I use" de [Agentic Engineering Patterns, de Simon Willison](https://simonwillison.net/guides/agentic-engineering-patterns/). Cada patrón tiene cuatro partes:

- **El prompt**, listo para adaptar. Los huecos que rellenas aparecen así: `<esto>`.
- **Por qué funciona:** el mecanismo, para que puedas escribir tu propia variante.
- **Ojo con:** cuándo falla o qué cuesta.
- **Fuente:** nuestra práctica o una fuente pública con nombre.

No son palabras mágicas. La mayoría funcionan porque la sesión ya tiene contexto: una base de conocimiento (knowledge base), un `AGENTS.md`, una issue bien escrita. Si falta el contexto, un prompt más largo no lo arregla ([módulo 4](../04-context-is-infrastructure/README.md)). Puedes escribirlos, pegarlos o dictarlos, en cualquier idioma.

**Patrones de esta página**

- Conversar y planificar: [1. Discute antes de construir](#1-discute-antes-de-construir) · [2. Explica antes de ejecutar](#2-explica-antes-de-ejecutar) · [3. Entrevista para la especificación, una pregunta cada vez](#3-entrevista-para-la-especificación-una-pregunta-cada-vez) · [4. Especifica poco a propósito](#4-especifica-poco-a-propósito) · [5. Lee más código para responder tus propias dudas](#5-lee-más-código-para-responder-tus-propias-dudas)
- Construir y verificar: [6. TDD rojo/verde](#6-tdd-rojoverde) · [7. ¿Tenemos efectos secundarios?](#7-tenemos-efectos-secundarios) · [8. ¿Qué harías distinto?](#8-qué-harías-distinto) · [9. Hazlo más simple](#9-hazlo-más-simple) · [10. Documento de arquitectura como herramienta para pensar](#10-documento-de-arquitectura-como-herramienta-para-pensar) · [11. Sigue hasta que se cumpla el objetivo](#11-sigue-hasta-que-se-cumpla-el-objetivo)
- Recordar: [12. Recuerda esto](#12-recuerda-esto) · [13. Transcripción → base de conocimiento → backlog](#13-transcripción--base-de-conocimiento--backlog)
- Descomponer y traspasar: [14. Convierte este plan en issues](#14-convierte-este-plan-en-issues) · [15. Esqueleto del prompt de arranque](#15-esqueleto-del-prompt-de-arranque) · [16. Paquete de traspaso](#16-paquete-de-traspaso)
- Revisar: [17. Revisor con contexto limpio](#17-revisor-con-contexto-limpio) · [18. Triaje de la revisión según la intención del PR](#18-triaje-de-la-revisión-según-la-intención-del-pr) · [19. Cerrar el bucle por decisión](#19-cerrar-el-bucle-por-decisión)
- Entre sesiones: [20. Estado de varias sesiones](#20-estado-de-varias-sesiones) · [21. Inicio de sesión](#21-inicio-de-sesión) · [22. Fin de sesión](#22-fin-de-sesión)

## Conversar y planificar

### 1. Discute antes de construir

```text
Vamos a discutirlo. Quiero <resultado> en <área>. Lee primero el código
relevante y dame dos o tres opciones con sus pros y contras. No escribas
código todavía.
```

Después, tras una o varias rondas de objeciones:

```text
La opción 2, pero sin cambiar el formato de almacenamiento. Constrúyelo.
```

**Por qué funciona.** "Vamos a discutirlo" y "dame opciones" hacen que el agente pase de hacer a pensar, y "constrúyelo" lo devuelve a hacer. Revisas la intención cuando todavía es barato cambiarla, no un diff. Las opciones además aprovechan algo que a las personas se nos da bien: DHH lo llama «evaluación diferencial» (traducción propia) en [Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/): elegir una entre tres en lugar de especificar una desde cero.

**Ojo con.** Algunos agentes empiezan a editar igualmente, sobre todo en modos permisivos. Si el tuyo lo hace, usa el modo plan para la discusión. Y no dejes que la discusión se alargue sin fin: cuando hayas elegido, di "constrúyelo" (el [módulo 5](../05-decompose-into-tracks/README.md) lo llama "avanza antes de discutir").

**Fuente.** Peter Steinberger: «en cuanto digo "vamos a discutirlo" o "dame opciones", no construyen nada hasta que digo "constrúyelo"» (traducción propia), en [el podcast The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code). Módulo: [2](../02-one-agent-done-well/README.md).

### 2. Explica antes de ejecutar

```text
Antes de empezar con la issue #<n>, explícame qué vas a hacer: los archivos
que vas a tocar, el enfoque, cómo lo vas a probar y todo lo que la issue deja
abierto. No cambies nada hasta que te diga adelante.
```

**Por qué funciona.** Convierte una issue que no has leído con detalle en dos minutos de revisar un plan. Los malentendidos aparecen como una lista de archivos equivocada o un test equivocado antes de convertirse en un diff equivocado.

**Ojo con.** Una explicación fluida no es una prueba. Si el plan nombra archivos o funciones, comprueba al azar que existen. Si la explicación es vaga, probablemente la issue está poco especificada: arregla la issue, no el prompt.

**Fuente.** Nuestra práctica. En The Agile Monkeys no leemos todas las issues de un backlog que mantiene el agente; pedimos esta explicación antes de empezar cada tarea. Módulo: [5](../05-decompose-into-tracks/README.md).

### 3. Entrevista para la especificación, una pregunta cada vez

```text
Quiero construir <idea breve>. Hazme una pregunta cada vez para que
escribamos una especificación completa. Cada pregunta debe partir de mis
respuestas anteriores. Céntrate en lo difícil: casos límite, datos, manejo
de errores, qué queda fuera del alcance. Cuando lo hayamos cubierto todo,
escribe la especificación en SPEC.md.
```

**Por qué funciona.** No necesitas tener toda la especificación en la cabeza; solo tienes que responder una pregunta concreta cada vez. Una pregunta por turno mantiene tus respuestas cortas y específicas, y el agente pregunta por cosas en las que no habías pensado.

**Ojo con.** Para funcionalidades pequeñas puede alargarse demasiado. Para cuando las preguntas se vuelvan triviales. Las best practices de Anthropic añaden un paso que merece la pena copiar: empezar la implementación en una sesión nueva que lea `SPEC.md`, para que la entrevista no llene su contexto.

**Fuente.** «Hazme una pregunta cada vez» (traducción propia) viene del [flujo de trabajo con LLM de Harper Reed](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/). El paso de entrevistar y luego abrir una sesión nueva viene de las [best practices de Claude Code](https://code.claude.com/docs/en/best-practices). Módulo: [2](../02-one-agent-done-well/README.md).

### 4. Especifica poco a propósito

```text
Issue S7: hacer shelf más útil para clubes de lectura. Construye una primera
versión tosca de lo que creas que más les ayudaría, en una rama. Después
dime todas las suposiciones que has hecho.
```

**Por qué funciona.** Cuando todavía no sabes lo que quieres, un borrador concreto te enseña más rápido que una especificación. Reaccionas ante algo real. El consejo de DHH: «Sé tan vago como puedas para que se materialice algo, y luego interactúa con ese algo» (traducción propia), en [Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/).

**Ojo con.** Úsalo para explorar, en una rama o en un worktree desechable, nunca para trabajo que piensas hacer merge tal cual. Lo útil es la lista de suposiciones; el código a menudo se tira, y no pasa nada.

**Fuente.** DHH (arriba) y Peter Steinberger, que cuenta que a menudo especifica poco a propósito para sacar ideas nuevas ([el podcast The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code)). Módulo: [2](../02-one-agent-done-well/README.md).

### 5. Lee más código para responder tus propias dudas

```text
Lee más código para responder tus propias dudas. Vuelve cuando puedas
señalar archivo:línea para cada afirmación.
```

**Por qué funciona.** Los agentes a menudo dejan de leer pronto y te preguntan cosas que el código ya responde, o adivinan. Esto los manda de vuelta a la fuente y les pide evidencia que puedes comprobar.

**Ojo con.** En un código grande, leer sin límites llena el contexto. Nombra la carpeta, o pide que un subagente haga la lectura y devuelva un resumen.

**Fuente.** Peter Steinberger, [transcripción del Lex Fridman Podcast #491](https://lexfridman.com/peter-steinberger-transcript/). Módulo: [2](../02-one-agent-done-well/README.md).

## Construir y verificar

### 6. TDD rojo/verde

Empieza una sesión sobre un proyecto existente con:

```text
Primero ejecuta los tests.
```

Después, para el cambio:

```text
Implementa la issue S3 (Mostrar estadísticas de lectura). Usa TDD rojo/verde:
escribe primero los tests, ejecútalos y enséñame que fallan, y después
implementa hasta que pasen. Los tests no pueden depender de la fecha de hoy.
Enséñame la salida de las dos ejecuciones.
```

**Por qué funciona.** "Primero ejecuta los tests" enseña al agente cómo se ejecuta la suite y que importa. Rojo/verde obliga al agente a demostrar que el test puede fallar, lo que protege contra tests que pasan sin ejercitar el código nuevo y contra código que nadie necesitaba. Pedir las dos salidas te da evidencia en lugar de una afirmación.

**Ojo con.** Si el agente se salta el paso rojo, puede que el test ya pasara antes. Busca la ejecución que falla. Vigila también los tests que se debilitan o se reescriben para encajar con la implementación.

**Fuente.** Simon Willison, [Red/green TDD](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/) y [First run the tests](https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/). En inglés, sus prompts son literalmente "Use red/green TDD" y "First run the tests". Módulo: [3](../03-close-the-loop/README.md).

### 7. ¿Tenemos efectos secundarios?

```text
¿Tenemos algún efecto secundario con esto? Revisa triggers de base de datos,
callbacks, manejadores de eventos, cachés, tareas en segundo plano y
cualquier otra cosa que se ejecute porque cambian estos datos. Enséñame
dónde está cada uno.
```

**Por qué funciona.** Los agentes razonan sobre el código que están editando. Los efectos secundarios viven en otro sitio: un trigger, un suscriptor, una tarea programada. Preguntarlo directamente hace que el agente los busque.

**Ojo con.** "No hay efectos secundarios" sin una lista de los sitios revisados no es una respuesta. Pregunta qué ha buscado.

**Fuente.** Peter Steinberger cuenta un fallo causado por un trigger de base de datos que siguió invisible hasta que preguntó «¿tenemos algún efecto secundario con esto?» (traducción propia), en [el podcast The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code). Módulo: [2](../02-one-agent-done-well/README.md).

### 8. ¿Qué harías distinto?

```text
Ahora que lo has construido, ¿qué harías distinto?
¿Qué deberíamos refactorizar antes de hacer merge?
```

**Por qué funciona.** Después de construir, el agente entiende el problema mejor que cuando lo planificó. Este prompt convierte ese conocimiento en una lista de refactorizaciones mientras el contexto sigue cargado.

**Ojo con.** Siempre encontrará algo. Decide qué merece la pena hacer ahora según el objetivo del PR; lo demás va a una issue o a ninguna parte.

**Fuente.** Peter Steinberger, [transcripción del Lex Fridman Podcast #491](https://lexfridman.com/peter-steinberger-transcript/). Módulo: [2](../02-one-agent-done-well/README.md).

### 9. Hazlo más simple

```text
Esto funciona, pero parece demasiado complicado para el problema. Hazlo más
simple: el mismo comportamiento, los mismos tests pasando, menos piezas.
Dime qué has quitado y por qué no hacía falta.
```

**Por qué funciona.** Los agentes añaden capas, código defensivo y abstracciones, sobre todo después de rondas de revisión. Casi nunca las quitan si no se lo pides. El trabajo de la persona es notar cuándo la forma no guarda proporción con el problema.

**Ojo con.** "Más simple" tiene que conservar el comportamiento. Los tests tienen que seguir pasando, y lo que se simplifica no pueden ser los propios tests.

**Fuente.** DHH: «de verdad tienes que decirles: "Hazlo más simple"» (traducción propia), en [Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/). Cuenta que a menudo eso reduce el código más o menos a la mitad. Módulo: [7](../07-agents-review-agents/README.md).

### 10. Documento de arquitectura como herramienta para pensar

```text
Lee el código de <módulo> y escribe un documento de arquitectura: los
componentes, una petición seguida de principio a fin, dónde se registra
cada resultado y qué pasa cuando falla cada paso. Usa diagramas Mermaid.
Guárdalo en docs/architecture/<módulo>.md.
```

Después léelo y corrige lo que no encaje, en una o dos frases:

```text
Cada comando tiene que registrar su propio éxito o fallo. El reparto a otros
comandos le corresponde al sistema de eventos, no al comando. Lee la
documentación, propón un plan y, cuando te diga que sí, cambia el código y
actualiza el documento.
```

**Por qué funciona.** Un diagrama del código real se juzga más rápido que un diff, y los problemas de diseño saltan a la vista (por ejemplo, un fallo que nadie registra). Las correcciones cortas funcionan porque la sesión tiene todo el contexto. El agente cambia el código y el documento, así que siguen alineados.

**Ojo con.** No edites tú el documento. Es una herramienta para pensar, no el entregable. Y comprueba un par de flechas contra el código: un diagrama generado puede describir el diseño que querías en lugar del que tienes.

**Fuente.** Nuestra práctica: en The Agile Monkeys así revisamos un sistema de ingesta basado en eventos, y la corrección de arriba es la que dimos. Módulo: [2](../02-one-agent-done-well/README.md).

### 11. Sigue hasta que se cumpla el objetivo

```text
Objetivo: <estado final verificable, por ejemplo "python -m unittest termina
con código 0 y todos los comandos del README funcionan">. Sigue hasta que se
cumpla el objetivo o te bloquees. No pares a preguntarme por pasos rutinarios.

Reglas: no borres, no te saltes ni debilites tests. No escribas a mano las
salidas esperadas. No envuelvas ni copies una implementación existente para
que pasen las comprobaciones. Si la única forma de avanzar rompe una regla,
para y dímelo.

Al terminar: qué has cambiado, el comando que demuestra el objetivo y
cualquier cosa que hayas tenido que decidir.
```

**Por qué funciona.** Las ejecuciones largas sin supervisión compensan cuando "terminado" es algo que un comando puede comprobar. Tanto Claude Code como Codex tienen un comando `/goal` que mantiene una sesión trabajando hacia una condición (consulta [Herramientas](tools.md)).

**Ojo con.** Los agentes presionados para terminar hacen trampa. Simon Willison los llama «becarios digitales raros que harán trampa sin dudarlo si les das la oportunidad» (traducción propia), en [Vibe engineering](https://simonwillison.net/2025/Oct/7/vibe-engineering/). DHH cuenta que, cuando varios modelos intentaron el mismo port largo, uno trató de hacer trampa envolviendo una implementación existente. Las señales de alarma de Kent Beck sirven aquí: bucles, funciones que nadie pidió, tests desactivados o borrados ([Augmented Coding](https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes)). Revisa primero el diff de los tests.

**Fuente.** El experimento del port de DHH ([Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/)) y el [bucle Ralph de Geoffrey Huntley](https://ghuntley.com/ralph/). Módulo: [3](../03-close-the-loop/README.md).

## Recordar

### 12. Recuerda esto

```text
Recuerda esto: <la corrección, en una frase>. Guárdalo como entrada de
memoria con Regla / Por qué / Cómo aplicarla, con la fecha de hoy. Si todas
las sesiones de este repositorio lo necesitan, propón en su lugar la línea
exacta para AGENTS.md. Si un script pudiera comprobarlo, propón la
comprobación.
```

**Por qué funciona.** Una corrección que solo se dice en el chat muere con la sesión. Este prompt la guarda y pregunta en qué punto de la ruta de promoción debe estar: memoria, regla de `AGENTS.md` o guarda. La versión de Boris Cherny es más corta: «Actualiza tu CLAUDE.md para no volver a cometer ese error» (traducción propia), en sus [consejos del equipo](https://x.com/bcherny/status/2017742741636321619).

**Ojo con.** Los archivos de instrucciones engordan, y los archivos largos se ignoran. Poda las reglas que el agente ya cumple, y convierte en un hook o un test las que se siguen saltando.

**Fuente.** Nuestra práctica y Boris Cherny (arriba). Mitchell Hashimoto describe el mismo hábito como "harness engineering" en [My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey). Módulo: [4](../04-context-is-infrastructure/README.md).

### 13. Transcripción → base de conocimiento → backlog

```text
Aquí tienes la transcripción de la reunión de planificación de hoy: <ruta>.
1. Actualiza la base de conocimiento: las decisiones nuevas como registros
   de decisión, las decisiones que cambian marcadas como reemplazadas (no
   borradas), las preguntas abiertas y todo lo que contradiga lo que ya
   tenemos. Enséñame el diff de kb/ antes de hacer commit.
2. Después repasa el backlog abierto. Lista las issues que hay que cerrar
   porque ya no tienen sentido, las que hay que actualizar y las que hay que
   crear, con un motivo de una línea para cada una. No toques GitHub hasta
   que apruebe la lista.
```

**Por qué funciona.** En las reuniones cambia el rumbo, y en el backlog es donde ese cambio suele perderse. Dos pasos en orden (primero el porqué, después el qué) mantienen el backlog coherente con las últimas decisiones.

**Ojo con.** Las transcripciones tienen ruido: una media broma puede acabar siendo una "decisión". Lee la lista de decisiones antes del paso del backlog. Y trata una transcripción de fuera de tu equipo como entrada no confiable.

**Fuente.** Nuestra práctica. El [módulo 9](../09-teams-and-organizations/README.md) lo usa como ejemplo de un hábito que descubre una persona y que debería llegar a todo el equipo. Módulo: [4](../04-context-is-infrastructure/README.md).

## Descomponer y traspasar

### 14. Convierte este plan en issues

```text
Pasa este plan a issues de GitHub siguiendo las convenciones de AGENTS.md.
Si es más grande que un pull request, crea una épica y enlaza las historias.
Cada issue tiene que entenderse sola para una sesión nueva: problema,
evidencia con archivo:línea, esbozo de la solución, criterios de aceptación,
fuera de alcance. Marca las dependencias y qué issues pueden avanzar en
paralelo porque tocan archivos distintos. Enséñame los títulos y los grupos
en paralelo antes de ejecutar gh issue create.
```

**Por qué funciona.** El plan ya existe en la conversación. Convertirlo en issues autocontenidas hace de cada una un prompt listo para una pista de trabajo (track). Con el tiempo el repositorio aprende las convenciones y basta con "crea una issue".

**Ojo con.** Los agentes dividen de más. Una historia partida en PR1, PR2 y PR3 cuesta más revisión humana que un PR de principio a fin. Revisa la agrupación según el radio de impacto, no según el número de tareas.

**Fuente.** Nuestra práctica. Módulo: [5](../05-decompose-into-tracks/README.md).

### 15. Esqueleto del prompt de arranque

```text
Trabaja en la issue #<n>: <título>. Crea un worktree desde un origin/main
recién actualizado y trabaja solo ahí.

## Lo que ya he comprobado (empieza desde aquí, no lo vuelvas a deducir)
- <hecho, con el comando o el archivo:línea que lo muestra>

## Haz esto primero: demuestra la premisa
Antes de escribir código, comprueba <suposición>. Si no se cumple, para y
cuéntamelo.

## Decisiones ya tomadas (impleméntalas, no las reabras)
- <decisión>

## Reglas del repositorio que romperán el build
- <regla>

## Notas del entorno que te costarán una hora
- <nota>

## Fuera de alcance: informa, no arregles
Lista en tu informe los problemas fuera de esta issue. Si te ves tomando
decisiones de diseño que la issue no resuelve, para e informa.

## Terminado cuando
- [ ] <comprobación, por ejemplo: python -m unittest pasa>
- [ ] Pull request abierto, con la declaración de intención al principio

## Informe final
La URL del PR, qué has ejecutado y el resultado, qué no has ejecutado y por
qué, y cualquier cosa que hayas tenido que decidir y que la issue no resolvía.
```

**Por qué funciona.** Cada sección elimina una forma conocida de desperdiciar una sesión: volver a deducir hechos, reabrir decisiones, construir sobre una premisa falsa, arreglar cosas fuera de alcance o cantar victoria sin evidencia.

**Ojo con.** No rellenes todas las secciones para una issue pequeña; una sección vacía es ruido. Y no pongas aquí reglas permanentes: si la misma regla aparece en todos los arranques, llévala a `AGENTS.md`.

**Fuente.** Nuestra práctica; son los títulos de sección que usamos. El [módulo 5](../05-decompose-into-tracks/README.md) tiene una versión completa.

### 16. Paquete de traspaso

```text
Pausamos esta pista de trabajo. Escribe un paquete de traspaso en <ruta>
para que una sesión nueva, o yo dentro de una semana, pueda continuar sin
esta conversación:
- Verificado: hechos que has comprobado, cada uno con el comando o el
  archivo:línea que lo demuestra.
- Supuesto: lo que crees que es cierto pero no has verificado.
- Abierto: preguntas y decisiones pendientes, y quién decide.
- Trampas: lo que nos ha costado tiempo y cómo evitarlo.
- Continúa aquí: el primer paso, ejecutable hoy.
- Entorno: solo nombres de variables, nunca valores.
Termina con un prompt de reanudación autocontenido que pueda pegar en una
sesión nueva. Usa números, no adjetivos.
```

**Por qué funciona.** Separar lo Verificado de lo Supuesto evita que las conjeturas se conviertan en hechos en la siguiente sesión. La sección de Trampas suele ser la más valiosa. Un número sobrevive a una semana fuera; un adjetivo, no.

**Ojo con.** Los traspasos envejecen. La siguiente sesión debería volver a comprobar lo Verificado contra el código antes de apoyarse en ello.

**Fuente.** Nuestra práctica. Módulo: [5](../05-decompose-into-tracks/README.md).

## Revisar

### 17. Revisor con contexto limpio

Abre una sesión nueva (idealmente con el agente de otro proveedor) en el worktree del pull request:

```text
Revisa el pull request #<n>. Tú no lo escribiste. Lee primero la declaración
de intención al principio de la descripción del PR (gh pr view <n>) y
AGENTS.md. Contexto: <herramienta interna que solo se usa dentro de la
empresa | producto expuesto a internet>.

Informa solo de:
- fallos que rompen el objetivo declarado,
- seguridad o exposición de datos,
- tests que faltan para el comportamiento nuevo (un test tiene que fallar si
  se revierte el cambio),
- desviaciones de nuestra arquitectura documentada.
Para cada hallazgo: archivo:línea, qué se rompe, la evidencia y la gravedad.
Nada de preferencias de estilo. Si no estás seguro de si algo está dentro del
alcance, pregúntame.
```

**Por qué funciona.** Un revisor sin memoria de la implementación juzga el resultado, no el razonamiento. La intención y el contexto del proyecto evitan que persiga amenazas rebuscadas; la lista de "informa solo de" evita que rellene.

**Ojo con.** Un revisor al que le pides encontrar problemas encontrará alguno incluso en un trabajo correcto. Las best practices de Anthropic advierten de que perseguir cada hallazgo lleva a la sobreingeniería. Para eso está el triaje del siguiente patrón.

**Fuente.** El patrón Writer/Reviewer de las [best practices de Claude Code](https://code.claude.com/docs/en/best-practices), más nuestra propia corrección después de que un revisor sin contexto ayudara a que un pull request pasara de unas 5.000 a entre 20.000 y 40.000 líneas cambiadas (indicativo, [módulo 7](../07-agents-review-agents/README.md)).

### 18. Triaje de la revisión según la intención del PR

```text
Haz el triaje de todos los hallazgos de revisión del pull request #<n>.
1. Reúne todos los hilos de revisión sin resolver, de bots y de personas.
   Pagina: la API devuelve como mucho 100 hilos por página. Lee cada hilo
   antes de decidir.
2. Construye un registro: hallazgo | origen | veredicto | motivo. Veredictos:
   FIX_NOW, DEFER_TO_ISSUE, DISCARD, juzgados según la declaración de intención.
3. Siempre FIX_NOW: seguridad o exposición de datos, regresiones de
   rendimiento serias, duplicación que introduce este PR, comportamiento sin
   tests, desviaciones de la arquitectura documentada.
4. Marca como ASK lo que no tengas claro. Enséñame el registro antes de
   cambiar código.
5. Cuando lo apruebe: agrupa todos los FIX_NOW en un solo push, responde a
   cada hilo con el veredicto y el motivo, resuélvelo, y pon todos los
   DEFER_TO_ISSUE en una sola issue de seguimiento. Descarta los detalles
   menores; no los conviertas en issues.
```

**Por qué funciona.** Un veredicto por hallazgo, ligado a la intención, convierte un flujo infinito de comentarios en decisiones. Agrupar las correcciones significa un ciclo de CI y revisión por ronda en lugar de uno por hallazgo.

**Ojo con.** Las APIs de hilos de revisión truncan sin avisar, así que hay hilos ocultos que sobreviven a un "resolver todos". Un triaje demasiado optimista que lo acepta todo hace crecer el PR en lugar de terminarlo.

**Fuente.** Nuestra práctica (nuestra skill de bucle de revisión). Módulo: [7](../07-agents-review-agents/README.md).

### 19. Cerrar el bucle por decisión

```text
Llevamos <k> rondas de revisión en el pull request #<n> y siguen llegando
hallazgos. Deja de corregir. Dame una evaluación exigente, sí o no, frente a
la declaración de intención, no otro registro:
- ¿Qué hallazgos abiertos son derivados (causados por las correcciones de la
  ronda anterior, temas ya aplazados que vuelven o preguntas de producto)?
- ¿Queda algo que rompa el objetivo, o algún hallazgo de seguridad? Esos no
  se descartan nunca.
Después redacta el registro final: una decisión por hilo abierto con su
motivo, una respuesta para cada uno y el contenido de UNA issue de
seguimiento. No hagas push hasta que te diga adelante.
```

**Por qué funciona.** Los bucles de revisión dejan de converger: las correcciones crean hallazgos nuevos, que crean correcciones nuevas. Pedir una decisión de sí o no en lugar de otro registro rompe el ciclo y devuelve la decisión a una persona.

**Ojo con.** "Derivado" puede convertirse en una excusa. Los hallazgos de seguridad y de exposición de datos nunca se cierran por decisión: se corrigen.

**Fuente.** Nuestra práctica. Indicativo: uno de nuestros pull requests grandes pasó por unas 20 rondas de revisión automática y más de 200 hilos antes de que adoptáramos esto. Módulo: [7](../07-agents-review-agents/README.md).

## Entre sesiones

### 20. Estado de varias sesiones

```text
Lee las transcripciones de estas sesiones: <id de sesión> (Claude Code),
<id de sesión> (Codex), <id de sesión> (Claude Code). Para cada pista de
trabajo: qué se hizo, el pull request y su estado, qué está bloqueado y la
siguiente decisión que tengo que tomar. Después reescribe las filas
correspondientes de kb/ACTIVE.md (reescribe, no añadas) y redacta una
actualización de estado de cinco líneas para el equipo.
```

**Por qué funciona.** Las sesiones guardan sus transcripciones en disco (Claude Code las guarda en `~/.claude/projects/`; consulta [sessions](https://code.claude.com/docs/en/sessions)). Una sesión nueva puede leer varias y resumir el estado de todas las pistas más rápido de lo que tú cambias de ventana.

**Ojo con.** Guarda los IDs de sesión en algún sitio donde puedas encontrarlos. Después de un reinicio, averiguar qué hacía cada sesión es muy pesado. Y contrasta el resumen con los pull requests reales: una transcripción es una foto fija, y los sistemas vivos mandan.

**Fuente.** Nuestra práctica. Módulo: [6](../06-run-sessions-in-parallel/README.md).

### 21. Inicio de sesión

```text
Ejecuta git fetch y git status. Si hay cambios que no has hecho tú, dímelo
antes de tocar nada. Después lee la misión y kb/ACTIVE.md y dime en cinco
líneas: el objetivo actual, el siguiente paso, cualquier bloqueo y la
decisión abierta de <pista>. Si los números o las fechas de la base de
conocimiento no coinciden con el código o con GitHub, dilo. Eso es un
bloqueo, no un detalle.
```

**Por qué funciona.** Con sesiones en paralelo, el repositorio cambia mientras trabajas. Empezar desde un estado actualizado y reconciliado evita construir sobre algo que otra sesión ya cambió. El resumen de cinco líneas demuestra que la sesión cargó el contexto correcto antes de actuar.

**Ojo con.** Que el resumen no se convierta en una lectura larga de toda la base de conocimiento. Solo el índice y los artefactos que enlaza.

**Fuente.** Nuestra práctica (nuestro protocolo de recuperación de sesión). Módulo: [6](../06-run-sessions-in-parallel/README.md).

### 22. Fin de sesión

```text
Hemos terminado esta sesión. Antes de parar:
1. Haz commit y push de los cambios que has hecho en la base de conocimiento.
2. Reescribe la fila de esta pista en kb/ACTIVE.md: estado y siguiente punto
   de control.
3. Para cada worktree que hayas creado: si su rama ya tiene merge, elimínalo
   con git worktree remove; si no, dime por qué lo mantienes.
4. Ejecuta git status y enséñame el árbol limpio.
5. Dime qué no has verificado.
```

**Por qué funciona.** Un cambio en la base de conocimiento sin commit no ha ocurrido: la siguiente sesión no puede verlo. Limpiar los worktrees y reescribir el índice evita que las sesiones en paralelo lean un estado obsoleto como si fuera verdad.

**Ojo con.** Incluso con este prompt, la limpieza se descuida. En The Agile Monkeys una vez encontramos decenas de worktrees obsoletos que nadie había eliminado. Un hook que impide terminar la sesión con la base de conocimiento sucia es más fiable que el prompt ([módulo 3](../03-close-the-loop/README.md)).

**Fuente.** Nuestra práctica. Módulo: [6](../06-run-sessions-in-parallel/README.md).

## Añade los tuyos

¿Tienes un prompt que cambia los resultados de forma fiable? Compártelo con el formulario de issue "share your practice" que describe [CONTRIBUTING.es.md](../../../CONTRIBUTING.es.md). Incluye el prompt, por qué crees que funciona, cuándo falló y de dónde salió.
