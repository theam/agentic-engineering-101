---
title: "Laboratorio 9 — Escribe el acuerdo de trabajo de tu equipo"
module: 9
kind: lab
minutes: 60
level: advanced
last_reviewed: 2026-09-17
---

# Laboratorio 9 — Escribe el acuerdo de trabajo de tu equipo

## Objetivo

Escribir, con un agente, un acuerdo de trabajo de una página sobre cómo usa un equipo los agentes de programación: columnas del tablero y puntos de control, política de revisión, reglas de seguridad y declaración del uso de IA. Después, convertir una de sus reglas en una comprobación determinista, hacer que una sesión nueva ataque el documento y abrir un pull request con él.

El acuerdo es la palanca de "construir herramientas" del [módulo 9](README.md) en su forma más sencilla: un archivo compartido y revisado que leen tanto los agentes como las personas.

## Antes de empezar

- Has hecho los laboratorios 5–7, o te manejas con issues, worktrees y bucles de revisión.
- Tienes un repositorio en el que trabajar:
  - **Proyecto de prácticas:** tu copia de [`practice/shelf`](../../../practice/shelf/). Casi todas las respuestas del inventario serán "todavía nada". No pasa nada: el acuerdo es lo que las define.
  - **En tu propio repositorio:** uno que tu equipo use de verdad. Descubrirás cosas que no sabías (un bot con un token personal es un clásico). Háblalo con tu tech lead antes de abrir el PR.
- La CLI de GitHub (`gh`) está autenticada, si tu repositorio está en GitHub.
- Opcional pero valioso: alguien del equipo que te dé 10 minutos al final.

## Pasos

1. **Haz inventario de cómo funcionan hoy las cosas.** Abre una sesión en la raíz del repositorio y escribe:

   ```text
   Hablemos antes de escribir nada. Quiero un acuerdo de trabajo de una página
   sobre cómo usa nuestro equipo los agentes de programación en este repositorio.
   Primero, haz inventario de cómo funcionan hoy las cosas, como hechos con
   evidencia (rutas de archivos, configuración, salida de comandos). Incluye:
   quién puede mergear y si la rama principal está protegida, qué bots o
   automatizaciones existen y qué credenciales usan, dónde se ejecutan los
   agentes, qué archivos de instrucciones hay y cómo se revisan los PR.
   Marca como "desconocido" todo lo que no hayas podido verificar.
   No propongas cambios todavía.
   ```

   **Punto de control:** cada elemento tiene una fuente (una ruta, un comando y su salida) o dice "desconocido". Si el agente afirma algo sin evidencia, responde "Enséñame dónde lo has encontrado" antes de seguir. En tu propio repositorio, confirma los "desconocido" con alguien del equipo.

2. **Mapea la trifecta letal.** En la misma sesión:

   ```text
   Para cada agente o automatización del inventario, más dos que queremos añadir
   (un revisor de PR y un agente de triaje de issues), construye una tabla:
   agente | ¿datos privados? | ¿contenido no confiable? | ¿comunicación hacia fuera? | identidad y permisos
   En cualquier fila con tres "sí", propón el cambio más pequeño que quite una pata.
   ```

   **Punto de control:** ninguna fila tiene tres "sí" sin una mitigación al lado. El agente de triaje de issues debería salir con contenido no confiable en "sí". Si no, pregúntale al agente quién puede escribir texto en las issues de tu repositorio.

3. **Elige el tablero y los puntos de control.** Pide opciones, no un documento:

   ```text
   Dame dos o tres opciones para las columnas y los puntos de control de nuestro
   tablero. Restricciones: los agentes solo actúan en una columna de
   planificación y en una de implementación; las personas mueven las tarjetas,
   aceptan los planes y mergean. Para cada opción, enumera las columnas, quién
   actúa en cada una, la condición de salida y cómo distinguimos "PR todavía en
   CI" de "PR listo para una persona". Recomienda una. No escribas el acuerdo todavía.
   ```

   **Punto de control:** has elegido una opción y puedes explicar por qué en una frase. Si ninguna encaja, di qué falla ("no tenemos columna Listo; los planes se aceptan en el hilo de la issue") y vuelve a pedir.

4. **Redacta el acuerdo.** Pega este esqueleto en la sesión:

   ```markdown
   # Acuerdo de trabajo: agentic engineering
   Última revisión: AAAA-MM-DD

   ## 1. Tablero y puntos de control
   | Columna | Quién actúa | Sale cuando |
   - Los agentes solo actúan en:
   - Hay una persona asignada antes de que empiece un agente.
   - "Listo para una persona" significa:

   ## 2. Política de revisión
   - Cada PR recibe: (revisor con contexto limpio, segundo modelo o proveedor)
   - Categorías que siempre se corrigen:
   - Los bucles de revisión se cierran por decisión cuando:
   - Las personas leen línea a línea:

   ## 3. Reglas de seguridad
   - Entradas no confiables:
   - Identidades y permisos de los agentes: (tabla del paso 2, o un enlace a ella)
   - Secretos:
   - Comandos con privilegios de producción:

   ## 4. Declaración y firmas
   - Commits:
   - Publicaciones de agentes:
   - Todo lo que sale del equipo:

   ## 5. Pedir decisiones

   ## 6. Aprendizaje y arquitectura

   ## 7. Cómo cambia este acuerdo
   ```

   Y escribe:

   ```text
   Escribe docs/agentic-working-agreement.md con este esqueleto y las decisiones
   de esta conversación. Una página: como mucho 100 líneas. Donde no hayamos
   decidido algo, escribe "ABIERTO:" seguido de la pregunta. No inventes reglas
   que no hayamos hablado.
   ```

   **Punto de control:** lee el archivo entero. Son tres minutos. Cada regla debería ser algo que decidiste de verdad. Todo lo demás debería ser una línea `ABIERTO:`. Corrige con frases cortas ("los agentes nunca mergean, no 'rara vez'"). No edites el archivo a mano.

5. **Haz determinista una regla.**

   ```text
   Elige la regla del acuerdo que sea más fácil de comprobar mecánicamente y
   más probable que se olvide. Implementa la comprobación determinista más
   pequeña posible: un script, un hook o un paso de CI. Enséñame la comprobación
   fallando con un ejemplo malo y pasando con uno bueno. Después añade al acuerdo
   una línea que diga dónde vive la comprobación.
   ```

   Buenas candidatas: los commits de agentes llevan el trailer `Assisted-by:`; los agentes no pueden leer archivos `.env` (una regla de permisos o un [hook](https://code.claude.com/docs/en/hooks)); la descripción de cada PR tiene una sección de "AI assistance".

   **Punto de control:** has visto con tus propios ojos la salida que falla y la que pasa, no solo al agente diciéndolo.

6. **Atácalo desde una sesión nueva.** Cierra la sesión o abre otra. Quien revisa no debe recordar haber escrito el documento. Escribe:

   ```text
   Lee docs/agentic-working-agreement.md como un ingeniero senior escéptico que
   acaba de entrar en este equipo. No lo reescribas. Informa de:
   1. las tres reglas que más probablemente se ignorarán en la práctica, y por qué;
   2. cualquier contradicción entre reglas;
   3. un hueco que podría usar un atacante, sabiendo que los agentes leen issues y PR.
   Para cada hallazgo da un veredicto, FIX_NOW, DEFER_TO_ISSUE o DISCARD, con
   una línea de razonamiento.
   ```

   **Punto de control:** tienes un pequeño registro con un veredicto por hallazgo. Aplica los `FIX_NOW`. Para cada `DEFER_TO_ISSUE`, añade una línea `ABIERTO:` o crea una issue. Los huecos de seguridad nunca se descartan.

7. **Consigue una lectura humana y abre el pull request.** Enséñale el archivo a alguien del equipo, o reléelo mañana por la mañana si trabajas solo, y haz dos preguntas: "¿Seguirías esto mañana?" y "¿Qué regla romperías primero?". Ajusta. Luego pide al agente que redacte la descripción del PR:

   ```text
   Redacta la descripción de un pull request para este cambio: qué cubre el
   acuerdo, la comprobación determinista y cómo ejecutarla, las preguntas
   ABIERTO y una sección "AI assistance" que diga qué hizo el agente y qué
   decidí yo. No crees el PR; dame el texto.
   ```

   Haz commit, sube la rama y crea tú el PR con `gh pr create`.

   **Punto de control:** `gh pr view` muestra el PR, y su descripción tiene la sección de AI assistance.

## Cómo saber que has terminado

- [ ] `docs/agentic-working-agreement.md` existe y `wc -l docs/agentic-working-agreement.md` imprime 100 o menos.
- [ ] `grep -c "^## " docs/agentic-working-agreement.md` imprime al menos 5 (tablero, revisión, seguridad, declaración y al menos una más).
- [ ] La tabla de la trifecta no tiene ningún agente con las tres patas y sin mitigación.
- [ ] Una regla tiene una comprobación determinista, y la has visto fallar con un ejemplo malo y pasar con uno bueno.
- [ ] La revisión de la sesión nueva está triada, y sus `FIX_NOW` están aplicados.
- [ ] `gh pr view` muestra el PR con una sección "AI assistance".
- [ ] Solo en el proyecto de prácticas: si has tocado código, `python -m unittest` sigue pasando desde el directorio `shelf`.

## Reflexiona

- ¿Qué regla romperás primero con prisas? ¿Qué haría que romperla fuera difícil, y no solo algo desaconsejado?
- ¿Qué reglas siguen siendo prosa y deberían convertirse en guardas?
- ¿Qué te ha descubierto el inventario que no sabías?
- ¿Qué pregunta `ABIERTO:` necesita a alguien con autoridad, y cómo la vas a plantear bien: qué necesitas, por qué ahora y el camino degradado?
- Si un cliente de un sector regulado pidiera este acuerdo, ¿qué echaría en falta?

## Para ir más allá

- Haz una sesión de 30 minutos con tu equipo. Recorre el acuerdo con todos, pide a cada persona una regla con la que no esté de acuerdo y registra cada decisión en el documento o en la base de conocimiento del equipo.
- Enlaza el acuerdo desde `AGENTS.md` con una línea, para que los agentes lo encuentren cuando lo necesiten. Enlázalo en lugar de copiarlo dentro, para que el contexto que se carga siempre siga siendo pequeño.
- Comparte una versión sin datos sensibles, o la regla que te resultó más útil, como práctica para esta guía: consulta [CONTRIBUTING](../../../CONTRIBUTING.es.md).
