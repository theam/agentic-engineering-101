---
title: "Workshops"
kind: workshop
last_reviewed: 2026-09-17
---

# Workshops de Agentic Engineering 101

[Read in English](../en/README.md) ·
[Guía para facilitadores](facilitator-guide.md) ·
[Índice de la guía](../../content/es/README.md)

Esta página es para dos grupos de personas: quienes organizan un workshop y
quienes asisten a uno. Describe tres formatos, qué debería conseguir cada uno,
qué hay que preparar y cómo averiguamos después si algo ha cambiado.

No hay diapositivas aparte ni un guion aparte. El workshop es la guía: cada
bloque de las agendas de abajo apunta a una lección y a un laboratorio de
[`content/es/`](../../content/es/). En la sala enseñamos una versión corta de
cada lección y dedicamos la mayor parte del tiempo a los laboratorios. Las
lecciones completas son para leer antes o después.

> [!NOTE]
> **En The Agile Monkeys** usamos este material para incorporar a nuestros
> propios ingenieros y para impartir workshops. Esta es su primera edición. Los
> tiempos salen de hacer todos los laboratorios nosotros mismos, no de la media
> de muchas cohortes. Cuando impartas una sesión, cuéntanos qué se alargó y qué
> falló en una
> [issue de "share your practice"](https://github.com/theam/agentic-engineering-101/issues/new?template=share-your-practice.yml).

## Los tres formatos

| Formato | Duración | Módulos | Ideal para | Tamaño del grupo | Te llevas |
|---|---|---|---|---|---|
| **Sesión de introducción** | 90 minutos | 00, con vistazos a 01, 03, 06 y 07 | Equipos que deciden si invertir en el intensivo | Hasta 20 con práctica, hasta 40 solo con demo | Una imagen del juego completo y un cambio que probar la semana siguiente |
| **Intensivo** | 2 días | Día 1 "El sistema, no el prompt": 00–05 · Día 2 "Orquestación": 06–08 + un sprint en paralelo | Ingenieros que van a trabajar así con código real | 8–20 | Un repositorio de práctica con contexto, barreras de seguridad, PR mergeados y un registro de revisión, además de tus números de partida |
| **Seguimiento** | 4 semanas, una sesión por semana | 09–10, aplicados a tu propio código | Quienes terminaron el intensivo | La misma cohorte | Números de antes y después sobre tu trabajo real y un acuerdo de trabajo para tu equipo |

Los formatos se apoyan unos en otros. La sesión de introducción es un adelanto
de la primera mañana del intensivo. El seguimiento solo tiene sentido después
del intensivo, o después de trabajar por tu cuenta los módulos 00–08.

La guía se apoya en tres ciclos y un cuello de botella, y las agendas los
siguen: el **ciclo interno** (un agente, una tarea, bien hecha: módulos 02–03),
el **ciclo de contexto** (el sistema recuerda: módulo 04), el **ciclo externo**
(muchas pistas de trabajo (tracks) en paralelo: módulos 05–07) y la **atención
humana**, el cuello de botella que todo lo demás existe para proteger (módulos
06–08).

## Para quién es

### Público

El intensivo funciona mejor con ingenieros de software que escriben código cada
semana y que al menos han probado un agente de programación. En una sala típica
encontrarás los tres itinerarios de aprendizaje descritos en el
[módulo 00](../../content/es/00-start-here/README.md):

- **Recién llegados a los agentes.** Han usado un agente unas pocas veces, o
  solo como asistente de chat. Pueden hacer el intensivo si preparan bien el
  trabajo previo. Cuenta con que terminen los pasos básicos de cada laboratorio
  y se salten los apartados "Para ir más allá".
- **Usuarios diarios de un solo agente.** Usan un agente cada día, una tarea
  cada vez. Son el público principal: los dos días están pensados justo para el
  salto de una sesión a varias.
- **Líderes técnicos (tech leads)**, y cualquiera que ya trabaje con varias
  sesiones en paralelo. Sacan más partido de los apartados "Para ir más allá",
  de los módulos 07–09 y de ayudar a su mesa. Además, son quienes llevan la
  práctica de vuelta a sus equipos.

La sesión de introducción sirve para cualquier ingeniero y para responsables de
ingeniería que quieran ver la práctica antes de decidir. Los responsables pueden
seguir la versión solo con demo sin instalar nada.

No encaja con personas que no escriben código, ni con equipos que no pueden usar
agentes de programación en ningún código. Esos equipos pueden hacer el
intensivo con el proyecto de práctica, pero el seguimiento necesita un
repositorio real.

### Requisitos previos

Habilidades:

- **git:** crear una rama, hacer commit, hacer merge, resolver un conflicto
  sencillo.
- **Pull requests en GitHub:** abrirlos, comentarlos, hacer merge.
- **Un terminal:** moverte entre carpetas, ejecutar comandos, leer mensajes de
  error.
- **Leer Python, a grandes rasgos.** El proyecto de práctica es una pequeña
  herramienta de línea de comandos escrita en Python, solo con la biblioteca
  estándar. No hace falta que programes en Python. El código lo escribe el
  agente, pero tienes que poder juzgar si un cambio tiene sentido.

Las herramientas y las cuentas están en la lista de trabajo previo, justo debajo.

## Lista de trabajo previo

Si participas, termínala al menos tres días laborables antes del día 1. Si
organizas, recoge una confirmación (basta con un formulario corto) para que los
facilitadores puedan ayudar a quien se atasque antes de que se llene la sala.
Un problema de instalación resuelto en casa cuesta cinco minutos. En la sala
cuesta la primera hora.

### Cuentas y planes

- [ ] **Un plan de pago de al menos un agente de programación capaz**, por
  ejemplo [Claude Code](https://code.claude.com/docs/en/overview) o
  [Codex](https://learn.chatgpt.com/guides/best-practices), con la sesión
  iniciada en el equipo que vas a traer. El día 2 vas a ejecutar varias sesiones
  a la vez, y los planes de entrada pueden agotarse. Consulta los límites de uso
  de tu plan en la documentación del proveedor antes de venir. Si ya tienes un
  segundo plan, tráelo.
- [ ] **Opcional: un segundo agente de otro proveedor.** El módulo 07 lo usa
  como revisor. Si no lo tienes, harás pareja con alguien que sí.
- [ ] **Una cuenta de GitHub** en la que puedas crear un repositorio privado.
  `gh auth status` dice que tienes la sesión iniciada.
- [ ] **Permiso para usar tu plan en una formación**, si es un plan o una cuenta
  de empresa.

### Herramientas instaladas

Cada uno de estos comandos tiene que funcionar:

```bash
git --version          # cualquier git reciente; los worktrees vienen incluidos
gh --version
gh auth status
python3 --version      # 3.10 o superior
```

- [ ] Tu agente de programación arranca en un terminal (por ejemplo `claude` o
  `codex`) y responde a una pregunta trivial.
- [ ] Opcional: un terminal o una aplicación que muestre varias sesiones de
  agente a la vez, y una entrada de voz con la que te sientas cómodo (el dictado
  del sistema operativo basta). La
  [referencia de herramientas](../../content/es/reference/tools.md) recoge
  opciones.

### El repositorio de práctica

Los laboratorios usan [`shelf`](../../practice/shelf/), un pequeño gestor de
lista de lecturas. Cópialo en un repositorio tuyo, para que los agentes puedan
abrir issues y pull requests en él. La sección
["Use it for the labs"](../../practice/shelf/README.md#use-it-for-the-labs) del
README del proyecto de práctica explica cada flag. Desde la raíz de tu copia
local de esta guía:

```bash
mkdir -p ~/code
cp -r practice/shelf ~/code/shelf
cd ~/code/shelf
git init -b main
git add .
git commit -m "Start from the Agentic Engineering 101 practice project"
gh repo create shelf --private --source=. --remote=origin --push
python3 -m unittest
```

Después crea las issues S1 y S2 como describe la sección "Antes de empezar" del
[laboratorio 0](../../content/es/00-start-here/lab.md), con sus títulos y su
texto del [catálogo de issues](../../practice/issues/es.md). El laboratorio 5
crea el resto.

- [ ] `python3 -m unittest` en tu copia termina con `OK` (tarda menos de un
  segundo).
- [ ] `gh repo view` muestra tu copia en GitHub.
- [ ] `gh issue list` muestra S1 y S2.
- [ ] Conservas la copia de esta guía en tu equipo: varios laboratorios leen de
  ella el catálogo de issues.

### Un repositorio real para el seguimiento

- [ ] Elige un repositorio en el que vayas a trabajar durante las cuatro semanas
  posteriores al intensivo. Tiene que cumplir todo esto:
  - **Puedes usar agentes de programación en él.** Lee la política de tu empresa
    o de tu cliente; no lo des por hecho.
  - Sus **tests se ejecutan en local**, en minutos, sin credenciales de
    producción.
  - **Hay trabajo real en marcha:** issues que de verdad vas a hacer el mes
    siguiente.
  - Puedes conseguir que tus pull requests se **revisen y se mergeen en uno o
    dos días**.
  - Importa, pero **no es el sistema donde un error sale más caro**. Un merge
    malo tiene que tener arreglo.
- [ ] No lo uses durante el intensivo, salvo en los apartados "Para ir más
  allá", y nunca muestres su código en una pantalla compartida sin permiso.

### Seguridad

- [ ] **Ninguna credencial de producción en el equipo del workshop.** Nada de
  credenciales de la nube con acceso a producción en tus variables de entorno o
  archivos de configuración, nada de archivos `.env` con secretos reales, nada
  de claves SSH ni URL de bases de datos que lleguen a producción. Si tu portátil
  de siempre las tiene, usa para el workshop otro usuario del sistema operativo,
  una máquina virtual, un contenedor de desarrollo o un entorno de desarrollo en
  la nube.
- [ ] **Ningún modo que se salte los permisos en un equipo con credenciales.**
  Aprende antes del workshop qué hace la configuración de permisos de tu agente
  (para Claude Code, consulta los
  [modos de permisos](https://code.claude.com/docs/en/permission-modes)).
- [ ] **Una sesión de GitHub que solo llegue a lo que necesitas.** El
  repositorio de práctica y, más adelante, tu repositorio del seguimiento.

> [!WARNING]
> Durante los laboratorios, los agentes ejecutan comandos que no has escrito tú,
> leen archivos y procesan texto de issues y pull requests que podría haber
> escrito cualquiera. En agosto de 2025, un paquete de npm comprometido
> [invocó los CLI de programación con IA instalados, con flags para saltarse los permisos, para buscar secretos](https://nx.dev/blog/s1ngularity-postmortem).
> La ["trifecta letal"](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
> de Simon Willison explica el riesgo general: datos privados, contenido no
> confiable y una vía para sacar datos, todo en el mismo sitio. Un equipo de
> workshop no debería tener nada que merezca la pena robar.

### Punto de partida y lectura

- [ ] **Empieza el [laboratorio 1, tu punto de partida](../../content/es/01-from-chatbot-to-system/lab.md),
  una semana antes del día 1.** Registra una semana normal de trabajo: sesiones
  en paralelo, PR mergeados, tiempo esperando al agente, uso del plan. El día 1
  solo lo terminas y fijas un objetivo. El seguimiento compara contra este punto
  de partida.
- [ ] Lee el [módulo 00](../../content/es/00-start-here/README.md). Si tienes
  tiempo, lee las "Ideas clave" de los módulos 01–05.

## Formato 1: Sesión de introducción (90 minutos)

### Resultados de aprendizaje

Después de la sesión de introducción, cada participante puede:

- Explicar la diferencia entre usar un agente como un chatbot y construir un
  sistema a su alrededor: contexto, verificación, descomposición y revisión.
- Describir cómo un cambio pasa de issue a pull request revisado mientras un
  segundo cambio avanza en paralelo.
- Nombrar una práctica que probará en su propio trabajo la semana siguiente.

### Preparación

Dos variantes comparten la misma agenda. **Con práctica:** los participantes han
hecho las partes "Herramientas instaladas" y "El repositorio de práctica" del
trabajo previo y trabajan en parejas durante el bloque de 25 minutos. **Solo
demo:** nadie instala nada y, durante ese bloque, la sala decide en conjunto
cómo debería abordar el agente S2 y después critica el plan que produce.

### Agenda

| Hora | Min | Qué pasa | Material |
|---|---|---|---|
| 0:00 | 5 | Bienvenida. Encuesta rápida: "La semana pasada, ¿cuántas sesiones de agente llegaste a tener trabajando a la vez?" (0 / 1 / 2–4 / 5+) | — |
| 0:05 | 10 | La distancia entre usar un chatbot y tener un sistema; tres ciclos y un cuello de botella | [Lección 00](../../content/es/00-start-here/README.md) · [Lección 01](../../content/es/01-from-chatbot-to-system/README.md) |
| 0:15 | 15 | Demo en directo, parte 1: el agente explica `shelf`; discutir, planificar y construir la issue S1 con tests | [Laboratorio 0](../../content/es/00-start-here/lab.md) · [Lección 02](../../content/es/02-one-agent-done-well/README.md) |
| 0:30 | 5 | Demo en directo, parte 2: mientras S1 avanza, crear un worktree y arrancar una segunda sesión con S2 | [Lección 06](../../content/es/06-run-sessions-in-parallel/README.md) |
| 0:35 | 25 | Práctica en parejas: laboratorio 0 hasta el primer pull request. Solo demo: la sala dirige S2 | [Laboratorio 0](../../content/es/00-start-here/lab.md) · [Catálogo de issues](../../practice/issues/es.md) |
| 1:00 | 10 | Demo en directo, parte 3: una sesión nueva revisa el pull request de S1; triaje de un hallazgo | [Lección 07](../../content/es/07-agents-review-agents/README.md) |
| 1:10 | 8 | El momento del fallo: un agente dice "terminado" sin ejecutar los tests, y una barrera de seguridad (guardrail) le obliga a demostrarlo | [Lección 03](../../content/es/03-close-the-loop/README.md) |
| 1:18 | 7 | Puesta en común con notas adhesivas: qué te sorprendió y dónde está hoy tu techo | — |
| 1:25 | 5 | Siguientes pasos: el itinerario por tu cuenta, el intensivo, tarjetas de un minuto | [Índice de la guía](../../content/es/README.md) |

## Formato 2: Intensivo (2 días)

### Resultados de aprendizaje

Después del **día 1, "El sistema, no el prompt"** (módulos 00–05), cada
participante puede:

- Describir con números su propio punto de partida y fijar un objetivo (01).
- Llevar una issue por el ciclo discutir → planificar → construir → verificar
  con un agente, y enumerar las correcciones que tuvo que hacer (02).
- Conseguir que un agente compruebe su propio trabajo con una barrera de
  seguridad determinista en lugar de con un recordatorio en un prompt (03).
- Dar contexto completo a una sesión nueva mediante `AGENTS.md`, una base de
  conocimiento (knowledge base) y un índice `ACTIVE.md` (04).
- Convertir una lista de peticiones en pistas independientes, encontrar la
  pareja que entra en conflicto y escribir prompts de arranque (05).

Después del **día 2, "Orquestación"** (módulos 06–08 y el sprint), cada
participante puede:

- Llevar tres pistas a la vez en worktrees separados y hacer merge en un orden
  planificado, conflicto incluido (06).
- Revisar pull requests de agentes con un revisor de contexto limpio y un
  revisor de otro proveedor, dar un veredicto a cada hallazgo y cerrar el bucle
  por decisión (07).
- Calcular su coste por PR mergeado y nombrar sus principales sumideros de
  tokens (08).
- Convertir una petición vaga en issues concretas y después mantener
  productivas varias sesiones con ellas durante un sprint de 90 minutos sin
  romper los tests de `main`.

### Cómo se reparte el tiempo

Los bloques de abajo son más cortos que los `minutes` que figuran al principio
de cada lección y cada laboratorio. Esos son para quien aprende por su cuenta.
En la sala enseñamos una versión condensada de cada lección, el trabajo previo
cubre la instalación y los facilitadores señalan qué pasos pueden quedar como
tarea cuando un laboratorio se alarga. La
[guía para facilitadores](facilitator-guide.md) dice cuáles.

### Día 1 — "El sistema, no el prompt" (módulos 00–05)

| Hora | Min | Qué pasa | Material |
|---|---|---|---|
| 09:00 | 20 | Bienvenida, objetivos, cómo funcionan las notas adhesivas. Comprobación: nota "OK" a la vista cuando `python3 -m unittest` pasa en tu copia y tu agente responde | Lista de trabajo previo (arriba) |
| 09:20 | 15 | El juego completo: tres ciclos, un cuello de botella y cómo encajan en ellos los dos días | [Lección 00](../../content/es/00-start-here/README.md) |
| 09:35 | 45 | **Laboratorio 0:** planificar y construir S1 y abrir un PR; arrancar S2 en un worktree mientras S1 avanza; revisar el primer PR en una sesión nueva | [Laboratorio 0](../../content/es/00-start-here/lab.md) |
| 10:20 | 15 | Puesta en común: qué hizo el agente sin que se lo pidieras, qué salió mal, qué módulo explica cada paso | — |
| 10:35 | 15 | Descanso | — |
| 10:50 | 20 | Del chatbot al sistema: definición, el techo de adopción, qué dice la evidencia | [Lección 01](../../content/es/01-from-chatbot-to-system/README.md) |
| 11:10 | 20 | **Laboratorio 1 (final):** consolidar el punto de partida que empezaste hace una semana y fijar un objetivo a 30 días | [Laboratorio 1](../../content/es/01-from-chatbot-to-system/lab.md) |
| 11:30 | 20 | Un agente, bien usado: demo en directo de discutir → planificar → construir → verificar | [Lección 02](../../content/es/02-one-agent-done-well/README.md) |
| 11:50 | 55 | **Laboratorio 2:** la issue S3 por el ciclo completo, con un registro de cada corrección | [Laboratorio 2](../../content/es/02-one-agent-done-well/lab.md) |
| 12:45 | 60 | Comida | — |
| 13:45 | 20 | Cerrar el ciclo: demo en directo de un agente que dice "terminado", y después una barrera que le obliga a demostrarlo | [Lección 03](../../content/es/03-close-the-loop/README.md) |
| 14:05 | 45 | **Laboratorio 3:** añadir una barrera de seguridad determinista que impida al agente terminar mientras fallen los tests | [Laboratorio 3](../../content/es/03-close-the-loop/lab.md) |
| 14:50 | 15 | Descanso | — |
| 15:05 | 20 | El contexto es infraestructura: archivos de instrucciones, base de conocimiento, el índice `ACTIVE.md` | [Lección 04](../../content/es/04-context-is-infrastructure/README.md) |
| 15:25 | 45 | **Laboratorio 4:** `AGENTS.md`, `kb/ACTIVE.md` y un registro de decisión; comparar una sesión nueva con y sin ellos | [Laboratorio 4](../../content/es/04-context-is-infrastructure/lab.md) |
| 16:10 | 15 | Descomponer en pistas: issues como prompts, radio de impacto, orden de merge | [Lección 05](../../content/es/05-decompose-into-tracks/README.md) |
| 16:25 | 45 | **Laboratorio 5:** issues a partir del catálogo, pistas independientes, la pareja en conflicto, tres prompts de arranque. El día 2 empieza desde aquí | [Laboratorio 5](../../content/es/05-decompose-into-tracks/lab.md) · [Catálogo de issues](../../practice/issues/es.md) |
| 17:10 | 20 | Cierre: commit y push de todo, tarjetas de un minuto, qué esperar mañana | — |
| 17:30 | — | Fin | — |

**Entre los dos días (15 minutos como mucho):** comprueba que tu árbol de
trabajo está limpio y con push, que tus tres prompts de arranque están guardados
en el repositorio, y apunta el uso de tu plan durante el día 1. El laboratorio 8
lo usa.

### Día 2 — "Orquestación" (módulos 06–08 y el sprint en paralelo)

| Hora | Min | Qué pasa | Material |
|---|---|---|---|
| 09:00 | 15 | Apertura: temas principales de las tarjetas de un minuto. Comprobación: árbol limpio, las issues existen (`gh issue list`), prompts de arranque listos | — |
| 09:15 | 25 | Ejecutar sesiones en paralelo: demo en directo con tres worktrees, sesiones con nombre y notificaciones atendidas por turnos (round-robin) | [Lección 06](../../content/es/06-run-sessions-in-parallel/README.md) |
| 09:40 | 80 | **Laboratorio 6:** tres pistas a la vez en tres worktrees; merge en el orden planificado; resolver el conflicto entre C1 y C2 | [Laboratorio 6](../../content/es/06-run-sessions-in-parallel/lab.md) |
| 11:00 | 15 | Descanso | — |
| 11:15 | 20 | Agentes que revisan agentes: intención del PR, contexto limpio, un segundo proveedor, el registro de triaje, cerrar por decisión | [Lección 07](../../content/es/07-agents-review-agents/README.md) |
| 11:35 | 55 | **Laboratorio 7:** dos revisores sobre un PR del laboratorio 6; un veredicto por hallazgo; cerrar el bucle por decisión | [Laboratorio 7](../../content/es/07-agents-review-agents/lab.md) |
| 12:30 | 60 | Comida | — |
| 13:30 | 20 | Economía de tokens: coste por PR mergeado, adónde van los tokens, elección de modelo | [Lección 08](../../content/es/08-token-economics/README.md) |
| 13:50 | 30 | **Laboratorio 8:** coste por PR mergeado de tu semana de partida y del workshop hasta ahora; tus tres principales sumideros de tokens | [Laboratorio 8](../../content/es/08-token-economics/lab.md) |
| 14:20 | 10 | Presentación del sprint: reglas, tablero, objetivos por itinerario | [Reglas del sprint](#el-sprint-en-paralelo) |
| 14:30 | 90 | **Sprint en paralelo** con el proyecto de práctica: conversar sobre S7, dividirla en issues y ejecutarlas en paralelo. Tómate el descanso mientras tus sesiones trabajan | [Catálogo de issues](../../practice/issues/es.md) · [Proyecto de práctica](../../practice/shelf/) |
| 16:00 | 30 | Revisión del sprint: totales de la sala, un registro de triaje en pantalla, el mejor fallo del día | — |
| 16:30 | 20 | Arranque del seguimiento: confirmar tu repositorio real y planificar la semana 1 | [Lección 10](../../content/es/10-your-30-day-plan/README.md) · [Laboratorio 10](../../content/es/10-your-30-day-plan/lab.md) |
| 16:50 | 10 | Encuesta y tarjetas de un minuto | [Plantilla de encuesta](facilitator-guide.md) |
| 17:00 | — | Fin | — |

### El sprint en paralelo

Noventa minutos para poner a trabajar el sistema completo sobre la única issue
que ningún laboratorio ha construido: S7, «Hacer shelf más útil para clubes de
lectura», la petición vaga a propósito. Después del laboratorio 6 suele ser la
única issue que queda abierta.

1. **Conversa sobre ella** con tu agente, en unos 20 minutos: las preguntas que
   necesitan respuesta y dos o tres opciones, como describen los criterios de
   aceptación de S7. Elige una y escribe la conclusión en la issue.
2. **Divide la opción en issues nuevas** escritas como S1–S6, compáralas entre
   sí en busca de solapamientos textuales y conflictos semánticos, y planifica
   un orden de merge. Casi todas las ideas para clubes de lectura cambian el
   formato del archivo de `shelf` que C2 versionó, lo que da trabajo de sobra a
   quien tiene más experiencia.
3. **Ejecuta las issues nuevas en paralelo,** cada una en su worktree, y haz
   merge en el orden que planificaste.

Lo que haya sobrado de laboratorios anteriores también puede entrar en el
sprint.

Reglas, leídas en voz alta en la presentación:

1. **Cada pull request pasa tu barrera en local**, recibe una revisión con
   contexto limpio y tiene un registro con un veredicto por hallazgo.
2. **El merge lo hacen las personas. Los agentes nunca hacen merge.**
3. **S7 necesita una conclusión escrita de la discusión antes de escribir
   código.** Es vaga a propósito.
4. **Ningún modo que se salte los permisos** en tu equipo.
5. **A las 16:00, deja de empezar cosas.** Termina o aparca lo que esté en
   marcha y deja tus worktrees limpios (`git worktree list`).

Los objetivos dependen del itinerario. Recién llegados: dos sesiones a la vez.
Usuarios diarios de un solo agente: tres o cuatro. Líderes técnicos y quienes ya
trabajan en paralelo: cinco o más. La sala mantiene un único tablero con
totales y sin nombres. La [guía para facilitadores](facilitator-guide.md) tiene
una variante para tríos que comparten repositorio.

> [!IMPORTANT]
> El sprint no es una carrera. Un pull request mergeado con los tests
> debilitados cuenta como fallo, y un fallo que detectas y arreglas cuenta como
> acierto. Celebramos el mejor fallo recuperado, no el número más alto.

## Formato 3: Seguimiento (4 semanas con tu propio código)

### Resultados de aprendizaje

Después del seguimiento, cada participante puede:

- Aplicar contexto, barreras de seguridad, pistas en paralelo y revisión con
  agentes a su propio repositorio, una práctica por semana (10).
- Comparar con honestidad sus números con su punto de partida, incluido lo que
  no mejoró (10).
- Proponer un acuerdo de trabajo para su equipo: columnas del tablero, puertas
  de control, política de revisión, reglas de seguridad y transparencia sobre el
  uso de IA (09).
- Compartir una práctica con la comunidad.

### Cómo funciona

Cada semana tiene un foco y una sesión en remoto de 60 minutos con la cohorte.
La cuarta sesión dura 90 minutos. Entre sesiones, cada participante trabaja
como siempre en su repositorio real aplicando la práctica de la semana, y
rellena la revisión semanal personal de la
[lección 10](../../content/es/10-your-30-day-plan/README.md). Calcula unos 30
minutos al día de práctica deliberada, además del trabajo normal, no en lugar
de él.

| Semana | Foco | Lee | Haz en tu repositorio real | Trae a la sesión |
|---|---|---|---|---|
| 1 | **Contexto** | [Lección 04](../../content/es/04-context-is-infrastructure/README.md) · [Lección 10](../../content/es/10-your-30-day-plan/README.md) | `AGENTS.md` (más un `CLAUDE.md` que lo importe, si usas Claude Code), una carpeta `kb/` con `ACTIVE.md` y tus primeros registros de decisión; haz commit de todo | La respuesta de una sesión nueva a "¿qué estamos haciendo y por qué?" |
| 2 | **Verificación y barreras de seguridad** | [Lección 03](../../content/es/03-close-the-loop/README.md) · la parte de seguridad de la [lección 09](../../content/es/09-teams-and-organizations/README.md) | Un único comando local de "puerta"; una barrera determinista para una regla que el agente se saltó de verdad; niveles de permisos. Aplica la base de seguridad antes de la semana 3 | Un fallo que la barrera detectó y una cosa que todavía no puedes comprobar |
| 3 | **Pistas en paralelo** | [Lección 05](../../content/es/05-decompose-into-tracks/README.md) · [Lección 06](../../content/es/06-run-sessions-in-parallel/README.md) | Cinco o más sesiones en worktrees durante al menos dos días; empieza el borrador del [laboratorio 9](../../content/es/09-teams-and-organizations/lab.md), el acuerdo de trabajo del equipo | El máximo de sesiones que sostuviste y qué se rompió primero |
| 4 | **Revisión con agentes y economía** | [Lección 07](../../content/es/07-agents-review-agents/README.md) · [Lección 08](../../content/es/08-token-economics/README.md) | Dos revisores agentes y un registro de triaje en cada PR; coste por PR mergeado; la retrospectiva del [laboratorio 10](../../content/es/10-your-30-day-plan/lab.md) | Tu tabla de antes y después y una práctica para compartir |

### Sesión semanal (semanas 1–3, 60 minutos)

| Hora | Min | Qué pasa |
|---|---|---|
| 0:00 | 5 | Ronda: un número por persona, el máximo de sesiones que mantuviste trabajando a la vez esta semana (de tu nota de revisión semanal) |
| 0:05 | 20 | Tríos en salas de grupos: tus números frente a tu punto de partida, una cosa que funcionó, una cosa que se rompió |
| 0:25 | 20 | Clínica sobre el foco de la semana: una demo breve del facilitador con el proyecto de práctica y preguntas de los tríos |
| 0:45 | 10 | Compromisos: cada persona escribe, en un documento compartido, la única cosa que hará la semana siguiente |
| 0:55 | 5 | Tarjetas de un minuto (un formulario anónimo de dos preguntas) |

### Sesión final (semana 4, 90 minutos)

| Hora | Min | Qué pasa |
|---|---|---|
| 0:00 | 10 | Ronda: tu antes y después en una frase |
| 0:10 | 25 | Tríos: cada persona recorre con las otras dos la retrospectiva de su laboratorio 10 |
| 0:35 | 20 | El antes y después agregado y anónimo de la sala, y lo que esos números muestran y no muestran |
| 0:55 | 20 | Dos o tres voluntarios presentan su acuerdo de trabajo de equipo (laboratorio 9) |
| 1:15 | 10 | Cada persona redacta una [issue de "share your practice"](https://github.com/theam/agentic-engineering-101/issues/new?template=share-your-practice.yml) |
| 1:25 | 5 | Encuesta final |

> [!WARNING]
> Quienes participan trabajan con código que puede ser confidencial. En las
> sesiones se habla de números y de patrones, no de código. Comparte pantalla
> con código real solo si tienes permiso, y los facilitadores hacen las demos
> con el proyecto de práctica, nunca con el repositorio de un participante.

## Qué medimos, antes y después

La promesa de esta guía es más trabajo en paralelo sin perder calidad.
Comprobamos esa promesa con seis números. Cada participante los mide sobre su
propio trabajo. El [laboratorio 1](../../content/es/01-from-chatbot-to-system/lab.md)
ya registra sesiones, PR mergeados, tiempo de ciclo, minutos humanos por PR,
coste por PR mergeado, retrabajo, tiempo de espera y uso del plan. Las cohortes
del workshop añaden una columna a esa semana de partida, la espera de revisión,
porque muestra adónde va la atención humana.

| Métrica | Qué significa | Cómo recogerla | Ojo con |
|---|---|---|---|
| **Sesiones en paralelo sostenidas** | Sesiones de agente que mantuviste haciendo trabajo útil a la vez en un día típico: la mediana, no tu mejor momento. Apunta también el máximo | La columna `parallel` del registro del laboratorio 1, que rellenas cada vez que arrancas una sesión | Una sesión que lleva una hora esperando tu respuesta no está "trabajando" |
| **PR mergeados por semana** | Pull requests que impulsaste y que llegaron a la rama principal | `gh pr list --author "@me" --state merged --search "merged:>=YYYY-MM-DD"` | Contar no es valor. Partir un PR en tres infla la cifra |
| **Tiempo de ciclo** | Desde que abres el pull request hasta el merge, mediana de la semana | Los campos `createdAt` y `mergedAt` que el laboratorio 1 guarda con `gh pr list --json`, resumidos por su script | Elige un único evento de inicio y úsalo en las dos mediciones |
| **Espera de revisión** | Cuánto tiempo pasó un PR listo para una decisión humana (checks en verde, revisión automática cerrada) hasta que una persona decidió | Apunta cuándo lo marcas como listo y cuándo alguien decide; la línea temporal del PR ayuda | Suele ser el número más grande. Muestra dónde la atención humana es el cuello de botella |
| **Coste por PR mergeado** | Gasto en agentes de la semana dividido entre PR mergeados | Cuotas de los planes prorrateadas a la semana, más el gasto en API (revisores automáticos incluidos), entre los PR mergeados | Más bajo no es automáticamente mejor: puede significar PR más pequeños y de menos valor |
| **Uso del plan** | Lo cerca que trabajas de los límites de tus planes, y cuántas veces los alcanzas | La vista de uso de tu agente al final de cada día (consulta la [referencia de herramientas](../../content/es/reference/tools.md)) | Llegar al límite no es un fracaso. Te dice dónde mirar en el módulo 08 |

Cuatro señales más mantienen honestos los números: el **retrabajo** (PR
mergeados que necesitaron un arreglo posterior o una reversión en 7 días), los
**minutos humanos por PR mergeado** (una muestra de cinco), el **tiempo
esperando a un agente**, los tres del laboratorio 1, y una **autoevaluación de
confianza** en las encuestas. No medimos líneas de código. Como dice DHH en el
[Lex Fridman Podcast](https://lexfridman.com/dhh-2/), «las líneas de código son
una métrica estúpida en general» (traducción propia).

### Cómo las recogemos

1. **Antes:** el [laboratorio 1](../../content/es/01-from-chatbot-to-system/lab.md),
   durante una semana normal antes del día 1, sin hábitos del workshop.
2. **Durante:** el [laboratorio 8](../../content/es/08-token-economics/lab.md), el
   día 2, ensaya el cálculo con números del workshop. Tienen ruido y salen de un
   proyecto de juguete. No pasa nada, porque lo que importa es el método.
3. **Después:** la semana 4 del seguimiento, con las mismas definiciones y las
   mismas herramientas, en la retrospectiva del
   [laboratorio 10](../../content/es/10-your-30-day-plan/lab.md).
4. **Confianza:** el formulario de inscripción pide una autoevaluación, y las
   encuestas del día 2 y de la semana 4 la vuelven a pedir (consulta la
   [guía para facilitadores](facilitator-guide.md)).

> [!IMPORTANT]
> Los números pertenecen a cada participante. Existen para aprender, nunca para
> evaluar el desempeño. Quien organiza solo ve agregados anónimos, y solo con
> consentimiento. Cuando se clasifica a las personas por un número, optimizan el
> número y la práctica se degrada.

Sé honesto sobre lo que pueden mostrar una semana antes y una semana después.
Las semanas no son iguales: vacaciones, incidencias, una migración difícil.
Apunta qué tuvo de especial cada semana. La investigación también es mixta. En
el [estudio de METR de 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/),
desarrolladores experimentados de código abierto fueron más lentos con IA
mientras creían que iban más rápido, y el
[seguimiento de METR de 2026](https://metr.org/blog/2026-02-24-uplift-update/)
apunta a una mejora de velocidad, pero califica su propia evidencia de muy
débil. [Faros AI](https://www.faros.ai/blog/ai-software-engineering) (un
proveedor, con datos correlacionales) vio subir los PR mergeados y, con ellos,
el tiempo de revisión de PR. Un
[estudio a gran escala sobre un despliegue en Microsoft](https://arxiv.org/abs/2607.01418)
encontró más PR mergeados entre quienes adoptaron las herramientas y señala que
el número de PR no equivale a valor. Trata tu antes y después como indicativo,
no como un benchmark, y trata con la misma cautela lo que cada cual declara en
las encuestas.

## Logística

### En la sala

- **Distribución:** mesas para parejas, con enchufe en cada puesto. Los
  portátiles con agentes todo el día agotan la batería.
- **Red:** los agentes necesitan una conexión estable todo el día. Prueba antes
  la red del lugar con varios portátiles ejecutando sesiones de agente, no solo
  con un test de velocidad. Las redes de invitados que piden iniciar sesión cada
  hora, cortan las conexiones largas o bloquean SSH rompen las sesiones y git.
  Ten un plan B, al menos un punto de acceso desde el teléfono para el facilitador.
- **Proyector:** comprueba desde la última fila que la fuente del terminal se
  lee.
- **Equipo del facilitador:** dos pantallas (demo y notas), notificaciones de
  chat y correo desactivadas, un usuario del sistema operativo limpio. La
  [guía para facilitadores](facilitator-guide.md) tiene la lista de comprobación
  previa completa.
- **Materiales:** notas adhesivas de dos colores para cada participante, fichas
  para las tarjetas de un minuto, una pizarra o una pared para el tablero del
  sprint, un temporizador visible.
- **Personas:** un facilitador principal más un ayudante por cada 8–10
  participantes. Los ayudantes tienen que haber hecho todos los laboratorios.
- **Descansos:** los agentes siguen trabajando mientras la gente come. Anuncia
  los descansos y respétalos: la sostenibilidad forma parte de la lección.

### En remoto

- **Divide el intensivo en cuatro medias jornadas** de unas tres horas y media,
  en días consecutivos o dos por semana: módulos 00–02, 03–05, 06–07, y 08 más el
  sprint. Dos días completos en remoto son demasiadas horas de pantalla.
- **Plataforma:** vídeo con salas de grupos, un canal de chat para errores y
  enlaces, y un tablero de estado compartido como equivalente de las notas
  adhesivas (consulta la [guía para facilitadores](facilitator-guide.md)).
- **Participantes:** una pantalla grande o dos (terminal y vídeo), auriculares.
  Con la cámara encendida durante los laboratorios, los ayudantes ven quién se
  ha atascado.
- **Facilitadores:** al menos dos, uno que enseña y otro que atiende el chat y
  las salas de grupos.
- **Compartir pantalla:** antes de compartir un terminal para pedir ayuda,
  comprueba que no se ven secretos ni código confidencial.
- **Descansos** cada 60–75 minutos.

### Idioma

El material existe en inglés y en español, y el workshop puede impartirse en
cualquiera de los dos. Cada participante puede hablar con sus agentes en el
idioma en el que mejor piense. Decide al principio en qué idioma se escriben los
artefactos persistentes de los repositorios de práctica (código, issues,
commits, base de conocimiento) y déjalo escrito en `AGENTS.md`.

> [!NOTE]
> **En The Agile Monkeys** solemos hablar con los agentes en español, a menudo
> por voz, y tenemos una regla fija: todo artefacto del repositorio se escribe
> en inglés. No hemos visto problemas por mezclar idiomas.

### Calendario para quien organiza

| Cuándo | Qué |
|---|---|
| 4 semanas antes | Fecha, lugar o plataforma, facilitadores y ayudantes. Formulario de inscripción con las preguntas de itinerario y el consentimiento para métricas anónimas |
| 2 semanas antes | Enviar la lista de trabajo previo de esta página. Cada participante confirma su plan y los permisos de su política |
| 1 semana antes | Cada participante empieza el punto de partida del laboratorio 1. Los facilitadores repasan la lista de comprobación previa |
| 3 días antes | Revisar las confirmaciones del trabajo previo; contactar con quien esté atascado |
| El día anterior | Probar la red en la sala; preparar los materiales |
| Después del día 2 | Enviar el mensaje de seguimiento, programar las cuatro sesiones, compartir la encuesta |

## Adaptar el material

El contenido de la guía tiene licencia [CC BY 4.0](../../LICENSE) y su código,
licencia [MIT](../../LICENSE-CODE). Puedes impartir estos workshops, cambiarlos y
traducirlos, en tu empresa, en tu comunidad o como formación de pago, siempre
que cites la autoría e indiques qué has cambiado. Por ejemplo:

```text
Basado en "Agentic Engineering 101", de The Agile Monkeys y sus colaboradores
(https://github.com/theam/agentic-engineering-101), con licencia CC BY 4.0.
Cambios: <qué has cambiado>.
```

Adaptaciones habituales:

- **Otro agente.** Los principios no dependen de una herramienta. Cambia los
  comandos con ayuda de la [referencia de herramientas](../../content/es/reference/tools.md)
  y ensaya cada laboratorio con la herramienta que vas a enseñar.
- **Otro stack.** Sustituye `shelf` por un proyecto en tu lenguaje, pero
  conserva sus propiedades: se ejecuta y se prueba en segundos sin servicios;
  tiene unas seis issues pequeñas e independientes, una pareja de issues que
  cambian el mismo modelo de datos y una petición vaga.
- **Un solo día.** Quédate con los módulos 00, 02, 03, 05 y 06 y un sprint de
  60 minutos, y deja 01, 04, 07 y 08 como lectura. Sé claro con el coste:
  pierdes la base de conocimiento y la revisión con agentes, que son lo que
  mantiene viva la práctica después del workshop.
- **Repartido en semanas.** Un módulo por semana en un bloque de dos horas: 30
  minutos de lección, 60 de laboratorio y 30 de puesta en común.
- **Dentro de un equipo, con su propio código.** Desde el día 2, haz los
  laboratorios en el repositorio del equipo, después de revisar la seguridad de
  los equipos y los permisos, y sustituye la pareja C1/C2 por dos issues reales
  que choquen.

Si lo adaptas, cuéntanos cómo fue en una
[issue de "share your practice"](https://github.com/theam/agentic-engineering-101/issues/new?template=share-your-practice.yml).
Las mejoras a estas páginas son bienvenidas como pull requests; consulta
[CONTRIBUTING.es.md](../../CONTRIBUTING.es.md).
