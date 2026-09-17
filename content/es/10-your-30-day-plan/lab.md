---
title: "Laboratorio 10 — Proyecto final: cuatro semanas con tu propio código"
module: 10
kind: lab
minutes: 90
level: intermediate
last_reviewed: 2026-09-17
---

# Laboratorio 10 — Proyecto final: cuatro semanas con tu propio código

## Objetivo

Planificar, ejecutar y cerrar el plan de 30 días del [módulo 10](README.md). Al terminar tendrás un archivo de plan, cuatro check-ins semanales, una lista de comprobación final respaldada por evidencias, una retrospectiva que compara tu práctica con tu punto de partida del módulo 01 y una práctica compartida.

Los 90 minutos del front matter son el tiempo del propio laboratorio: unos 30 minutos para prepararlo y unos 60 para la medición final y la retrospectiva. Cada check-in semanal lleva 15 minutos. La práctica en sí ocurre durante tu trabajo normal.

## Antes de empezar

- **Tu punto de partida** del [laboratorio 1](../01-from-chatbot-to-system/lab.md). Si no lo tienes, mide primero una semana laborable, antes de la semana 1.
- **Un repositorio:**
  - **En tu propio repositorio** (recomendado): uno en el que vayas a trabajar todos los días durante el mes. Para las primeras semanas, elige uno en el que un PR malo sea una molestia, no un incidente.
  - **Proyecto de prácticas:** si todavía no puedes usar código real, condensa el plan en cuatro sesiones de 1–2 horas sobre tu copia de [`practice/shelf`](../../../practice/shelf/). La sesión 1 es el laboratorio 4, la sesión 2 es el laboratorio 3, la sesión 3 es el laboratorio 6 (tres pistas: S4 con S5, C1 y C2, incluido el conflicto entre C1 y C2) y la sesión 4 son los laboratorios 7 y 8. Los números serán diminutos. Lo que buscas es el hábito y las plantillas.
- La CLI de GitHub (`gh`) autenticada, y un sitio para tu base de conocimiento (`kb/`) que tu agente pueda leer y al que hagas commit.
- Opcional: acceso a un segundo modelo o proveedor para la semana 4, y alguien que siga el mismo plan.

## Pasos

1. **Redacta el archivo de plan.** Abre una sesión donde viva tu base de conocimiento y pega este esqueleto:

   ```markdown
   # Plan de 30 días — <repositorio>, <fecha de inicio> a <fecha de fin>

   ## Punto de partida (del laboratorio 1)
   | Métrica | Valor | Cómo lo medí |
   | --- | --- | --- |

   ## Semana 1 — Contexto
   Objetivo:
   Entregables (cada uno con cómo verificarlo):
   Métrica:
   Riesgos en este repositorio:

   ## Semana 2 — Verificación y guardas
   Objetivo:
   Entregables (cada uno con cómo verificarlo):
   Métrica:
   Riesgos en este repositorio:

   ## Semana 3 — Pistas en paralelo
   Objetivo:
   Entregables (cada uno con cómo verificarlo):
   Métrica:
   Riesgos en este repositorio:

   ## Semana 4 — Revisión y economía
   Objetivo:
   Entregables (cada uno con cómo verificarlo):
   Métrica:
   Riesgos en este repositorio:

   ## Check-ins
   Día y hora:
   Compañero de plan:
   ```

   Y escribe:

   ```text
   Lee mis notas del punto de partida en <ruta>. Después lee este repositorio y
   redacta kb/30-day-plan.md a partir del esqueleto de arriba. Las cuatro
   semanas son: contexto, verificación y guardas, pistas en paralelo, revisión
   y economía. Para cada semana, enumera entregables que se puedan verificar
   con un comando o un archivo, y los riesgos propios de este repositorio
   (tests lentos o inestables, documentación que falta, bases de datos
   compartidas, puertos). Pregúntame lo que no puedas averiguar a partir del
   código. No te inventes números del punto de partida.
   ```

   **Punto de control:** cada entregable dice cómo verificarlo, y cada fila del punto de partida dice cómo se midió. Si alguna fila no tiene método, arréglalo ya. Vas a necesitar el mismo método en la semana 4.

2. **Prepara los check-ins.** Crea `kb/checkins/`, reserva un bloque recurrente de 15 minutos en tu calendario y guarda la plantilla de check-in de la [lección del módulo 10](README.md#el-check-in-semanal) como `kb/checkins/week-1.md`.

   **Punto de control:** `ls kb/checkins/` muestra `week-1.md`, y el evento está en tu calendario.

3. **Recorre las cuatro semanas y verifica cada una con la lista de comprobación.** Avanza en el plan durante tu trabajo normal. Al final de cada semana, antes del check-in, escribe:

   ```text
   Verifica los elementos de la semana N de la lista de comprobación final que
   te pego debajo. Para cada elemento, ejecuta el comando o abre el archivo y
   enséñame la evidencia. Marca un elemento como hecho solo si la evidencia lo
   respalda. Enumera lo que falta, sin arreglarlo.
   ```

   Pega junto al prompt la lista de esa semana.

   **Punto de control:** cada archivo de check-in enlaza la evidencia de los elementos que marcaste como hechos.

   ### La lista de comprobación final

   **Semana 1 — Contexto**

   - [ ] `AGENTS.md` existe. Si usas Claude Code, `grep -n "@AGENTS.md" CLAUDE.md` encuentra el import.
   - [ ] `wc -l kb/ACTIVE.md` imprime 100 o menos, con una fila por pista viva.
   - [ ] Hay al menos tres registros de decisión de decisiones tomadas esta semana.
   - [ ] Una sesión nueva respondió bien a "¿en qué estamos trabajando y por qué?", y su respuesta está guardada en el check-in.
   - [ ] `git status` en la base de conocimiento está limpio al final de cada sesión.

   **Semana 2 — Verificación y guardas**

   - [ ] Hay un comando de verificación documentado en `AGENTS.md` que pasa en la rama principal.
   - [ ] Una guarda bloqueó una sesión: rompiste un test a propósito, la sesión no pudo terminar y guardaste la salida.
   - [ ] Los niveles de permisos están configurados, y la lectura de secretos y el force-push están denegados.
   - [ ] Al menos un fixture de test varía como varían los datos de producción.

   **Semana 3 — Pistas en paralelo**

   - [ ] Hubo 5 o más sesiones en paralelo al menos dos días, con los IDs de sesión apuntados en el check-in. O te quedaste en un nivel más bajo porque no se mantenían las señales del módulo 06, y el check-in dice qué señal fue y qué arreglaste.
   - [ ] Cada pista viva tiene una fila en `ACTIVE.md` con su estado y su siguiente punto de control, y las pistas entregadas se han quitado.
   - [ ] `git worktree list` al final de la semana solo muestra pistas vivas.
   - [ ] Hay una plantilla de prompt de arranque guardada donde la próxima sesión pueda encontrarla.
   - [ ] Se cumple la base de seguridad del módulo 09: ningún modo que se salte los permisos fuera de un sandbox, y ninguna automatización del equipo con un token personal.

   **Semana 4 — Revisión y economía**

   - [ ] Al menos tres PR tienen declaración de intención, revisión con contexto limpio y registro de triaje. `gh pr view <número> --comments` muestra una respuesta en cada hilo de revisión.
   - [ ] El coste por PR mergeado está calculado, con la fórmula y las fuentes de datos por escrito.
   - [ ] Cada uno de tus tres mayores sumideros de tokens tiene un cambio aplicado.

4. **Toma la medición final.** Usa las mismas métricas, el mismo método y la misma duración de ventana que en el punto de partida: PR mergeados, tiempo de ciclo, minutos humanos por PR, coste por PR mergeado y retrabajo, junto a los números de sesiones y de uso. El retrabajo cuenta los PR mergeados que necesitaron un arreglo posterior o una reversión en 7 días, así que rellena esa fila una semana después de que termine la semana 4. Escribe:

   ```text
   Crea kb/retrospective.md con una tabla de antes y después:
   Métrica | Punto de partida | Semana 4 | Cambio | Fuente | Factores de confusión.
   Usa el mismo método que el punto de partida de kb/30-day-plan.md. Para los PR
   mergeados ejecuta
   gh pr list --state merged --author "@me" --search "merged:>=AAAA-MM-DD"
   y enséñame la salida. Saca cada número de una fuente que me puedas enseñar.
   Deja la celda vacía si no hay fuente. No estimes.
   ```

   Rellena a mano lo que el agente no alcanza, como el uso del plan desde la página de tu cuenta y tu recuento de tiempo de espera.

   **Punto de control:** cada celda rellena tiene una fuente, y la columna de factores de confusión no está vacía.

5. **Escribe la retrospectiva.** Reorganiza `kb/retrospective.md` con esta plantilla y mueve la tabla del paso 4 a su sitio:

   ```markdown
   # Retrospectiva de 30 días — <repositorio>, <inicio> a <fin>

   ## Contexto
   - Repositorio (tipo, tamaño, lenguaje) y tamaño del equipo:
   - Agentes y planes usados:
   - Qué más pasó este mes que afecte a los números:

   ## Antes y después
   (la tabla del paso 4)

   ## Qué cambiaron los PR
   Una línea por PR importante: qué cambió para los usuarios o para el equipo.

   ## Entregables
   Enlaza cada entregable semanal. Marca los que abandonaste, y por qué.

   ## Mantener

   ## Cambiar

   ## Abandonar

   ## Sorpresas

   ## Promociones
   Correcciones que se convirtieron en una entrada de memoria, una regla, una skill o una guarda.

   ## Costes
   Dinero, atención, sueño.

   ## Próximos 30 días
   Tres compromisos, cada uno con una métrica.
   1.
   2.
   3.

   ## Una práctica para compartir
   ```

   Deja que el agente rellene **Contexto**, **Entregables** y **Promociones** a partir de tus check-ins. **Mantener**, **Cambiar**, **Abandonar**, **Sorpresas**, **Costes** y **Próximos 30 días** escríbelos tú. Ahí está el criterio.

   **Punto de control:** Mantener, Cambiar y Abandonar tienen al menos un elemento cada uno, escrito con tus palabras.

6. **Pon a prueba tus conclusiones en una sesión nueva.** Abre una sesión sin memoria del mes y escribe:

   ```text
   Lee kb/retrospective.md y kb/30-day-plan.md como un revisor escéptico.
   ¿Qué conclusiones no se desprenden de los números? ¿Qué cambios podrían
   explicarse por los factores de confusión que aparecen, o por una mezcla
   distinta de tareas? No reescribas nada. Enumera como mucho cinco puntos.
   ```

   **Punto de control:** has matizado o cambiado al menos una conclusión, o has escrito por qué cada punto no aplica.

7. **Comparte una práctica.** Escribe:

   ```text
   Redacta una aportación de "Share your practice" a partir de kb/retrospective.md
   con: contexto, qué hice (el prompt, la regla o la guarda, literal), evidencia
   marcada como orientativa y qué no funcionó. Quita nombres de clientes, URLs
   internas, secretos y nombres de personas. Dame el texto; no envíes nada.
   ```

   Revisa el borrador buscando cualquier dato confidencial y envíalo tú mediante el formulario de issue descrito en [CONTRIBUTING](../../../CONTRIBUTING.es.md).

   **Punto de control:** la retrospectiva enlaza la issue que abriste.

## Cómo saber que has terminado

- [ ] `kb/30-day-plan.md` existe, con una tabla del punto de partida que indica el método de cada métrica y cuatro semanas de objetivos.
- [ ] `ls kb/checkins/` muestra cuatro archivos de check-in.
- [ ] Cada elemento de la lista de comprobación final está marcado con evidencia, o marcado como abandonado con un motivo.
- [ ] `kb/retrospective.md` tiene la tabla de antes y después, con una fuente para cada celda rellena.
- [ ] Mantener, Cambiar y Abandonar los has escrito tú.
- [ ] La prueba en una sesión nueva está hecha, y al menos una conclusión se ha revisado.
- [ ] Has compartido una práctica, y la retrospectiva la enlaza.
- [ ] `git status` en la base de conocimiento está limpio: todo tiene commit y push.

## Reflexiona

- ¿Qué capa marcó más diferencia y cuál menos? ¿Es lo que esperabas el día 1?
- ¿Dónde tocó techo tu capacidad de revisión, y qué la limitó?
- ¿Qué número te sorprendió? ¿Qué factor de confusión podría explicarlo?
- ¿Qué le dirías a alguien de tu equipo que empieza este plan el lunes que viene?
- ¿Cuál de tus prácticas debería convertirse en regla del equipo (consulta el [laboratorio 9](../09-teams-and-organizations/lab.md))?

## Para ir más allá

- Vuelve a medir dentro de 30 días sin seguir el plan. ¿Se mantuvieron los números?
- Sigue el plan a la vez que alguien de tu equipo sobre un repositorio compartido y compara tu retrospectiva con la suya.
- Propón tu práctica más útil como cambio al acuerdo de trabajo de tu equipo del laboratorio 9.
