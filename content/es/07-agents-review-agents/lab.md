---
title: "Laboratorio 7 — Dos revisores, un registro, una decisión"
module: 7
kind: lab
minutes: 75
level: advanced
last_reviewed: 2026-09-17
---

# Laboratorio 7 — Dos revisores, un registro, una decisión

## Objetivo

Lleva un pull request real por todo el bucle de revisión de [la lección](README.md): una declaración de intención, un revisor con contexto limpio, un revisor de otro proveedor, un registro de triaje, un lote de correcciones y una decisión de cierre que tomas tú.

Vas a seguir dos números por ronda, **hallazgos de prioridad alta** y **tamaño del diff**, para ver si el bucle converge.

## Antes de empezar

- **Un PR sin mergear que revisar.** Usa un PR del [laboratorio 6](../06-run-sessions-in-parallel/lab.md) en tu copia del [proyecto de práctica](../../../practice/shelf/). Los PR de C1 (etiquetas) o C2 (versión del formato del archivo) son los que más dan que hablar a los revisores. El PR de la S5 ("Eliminar un libro, con confirmación") también es buen material de revisión: su issue deja fuera del alcance la reutilización de ids tras eliminar el libro más reciente, así que fíjate en si tus revisores lo respetan. Si te saltaste el laboratorio 6, pide a un agente en un worktree nuevo que implemente la S5 del [catálogo de issues](../../../practice/issues/es.md), con tests, y que abra un PR con `gh pr create`. Si ya mergeaste todos los PR del laboratorio 6, haz lo mismo con una issue que siga abierta, por ejemplo una que haya salido de conversar sobre S7.
- **En tu propio repositorio:** elige un PR escrito por un agente, de entre 200 y 1.000 líneas cambiadas, que aún no tenga merge.
- **Dos agentes de programación de proveedores distintos**, por ejemplo Claude Code y Codex. Si solo tienes uno, haz la segunda revisión en otra sesión limpia con un foco distinto (tests y manejo de errores) y anota en tu reflexión que este montaje es más débil.
- `gh` con la sesión iniciada. Compruébalo con `gh auth status`.
- Un archivo de registro **fuera del repositorio**, por ejemplo `~/review-log.md`, con esta tabla:

```markdown
| Ronda | Hallazgos de prioridad alta (P0+P1) | Adiciones + eliminaciones | Notas |
| --- | --- | --- | --- |
```

## Pasos

1. **Mide el punto de partida.**

   ```bash
   gh pr view <n> --json additions,deletions,changedFiles
   ```

   **Punto de control:** tu registro tiene una fila de la ronda 0 con adiciones + eliminaciones.

2. **Escribe la declaración de intención.** Localiza el worktree del PR con `git worktree list`, abre allí una sesión nueva y escribe:

   ```text
   Redacta una declaración de intención para el PR #<n> con estos campos:
   Objetivo, Issue, Dentro del alcance, Fuera del alcance (a propósito), Contexto
   que fija el listón, Decisiones ya tomadas, Verificado con, Dónde mirar con más
   cuidado. Lee la issue, el diff (gh pr diff <n>) y los tests. Si no tienes claro
   el Objetivo o el Contexto, déjalos como preguntas para mí. Enséñame el
   borrador; todavía no cambies el PR.
   ```

   Reescribe tú el **Objetivo** y el **Contexto que fija el listón**. Son las líneas que hacen el trabajo. En el proyecto de práctica, el contexto es "CLI local de un solo usuario; el archivo de datos es de quien lo ejecuta; sin red". Copia también en la declaración la lista "Fuera del alcance" de la issue, porque los revisores no pueden respetar un límite que no ven. Después:

   ```text
   Pon esta declaración de intención al principio de la descripción del PR y
   conserva el resto. Después vuelve a consultar el PR con gh pr view <n> y
   confirma que el texto está ahí.
   ```

   **Punto de control:** `gh pr view <n>` muestra la sección de intención, y el agente volvió a consultar el PR en lugar de fiarse del comando de edición.

3. **Ejecuta el revisor con contexto limpio.** Abre una sesión **nueva** en el mismo worktree. No reutilices la sesión del autor ni la del paso 2. Aquí sirve el mismo proveedor que escribió el código.

   ```text
   Estás revisando el PR #<n> en una sesión nueva. Tú no escribiste este código.
   Lee la declaración de intención al principio de la descripción del PR
   (gh pr view <n>) y juzga cada hallazgo contra su objetivo, su alcance y su
   contexto. Lee el diff (gh pr diff <n>) y el código que lo rodea; lee más código
   para responder tus propias dudas.
   Informa solo de: fallos de corrección frente al objetivo, seguridad o exposición
   de datos, regresiones de rendimiento serias, duplicación que introduce este PR,
   comportamiento que ningún test detectaría si se revierte, desviaciones de
   AGENTS.md. Nada de estilo ni de renombrados.
   Para cada hallazgo: prioridad (P0 bloquea el merge, P1 se arregla en este PR,
   P2 seguimiento), archivo:línea, un escenario que falla, una idea de arreglo en
   una línea.
   Si no estás seguro de si es real o está dentro del alcance, ponlo en "Preguntas
   para la persona". Como mucho cinco hallazgos P2. No edites archivos. Una
   revisión vacía es un resultado válido.
   Publica la revisión como un único comentario del PR que empiece por
   "Revisión 1 (contexto limpio, <nombre del agente>)".
   ```

   **Punto de control:** `gh pr view <n> --comments` muestra la revisión. Cada hallazgo tiene archivo:línea y un escenario concreto. Trata como débiles los hallazgos sin escenario.

4. **Ejecuta el revisor de otro proveedor.** Abre una sesión nueva con el agente del otro proveedor en el mismo worktree. Pega el mismo prompt, pero etiqueta el comentario como `Revisión 2 (otro proveedor, <nombre del agente>)`.

   **Punto de control:** existe un segundo comentario de revisión. En la columna de notas de tu registro, apunta cuántos hallazgos aparecen en las dos revisiones y cuántos solo en una.

5. **Construye el registro de triaje.** Abre una sesión nueva (una sesión de triaje) y escribe:

   ```text
   Actúa como responsable del triaje del PR #<n>. Todavía no cambies código.
   1. Recoge todos los hallazgos: los dos comentarios de revisión y todos los hilos
      de revisión sin resolver, de bots o de personas. Obtén los hilos con la API
      GraphQL de GitHub y pagina hasta que hasNextPage sea false. Dime el total.
   2. Lee cada hallazgo entero antes de decidir.
   3. Construye una tabla: ID, Origen, Hallazgo, Veredicto (FIX_NOW /
      DEFER_TO_ISSUE / DISCARD), Motivo ligado a la declaración de intención.
      Siempre se corrigen: seguridad o exposición de datos, regresiones de
      rendimiento serias, duplicación introducida por este PR, falta de cobertura
      de comportamiento, desviaciones de la arquitectura documentada. Nunca
      marques como DISCARD un hallazgo de seguridad.
   4. Marca como ASK lo que no tengas claro y cualquier arreglo que añada una
      funcionalidad o una dependencia, o que haga crecer el diff de forma notable.
   Enséñame el registro y la lista de ASK, y para.
   ```

   Decide tú cada ASK y dile al agente tu veredicto y tu motivo.

   **Punto de control:** cada hallazgo tiene exactamente un veredicto. Ningún hallazgo de seguridad es DISCARD. Tu registro tiene el número de hallazgos de prioridad alta de la ronda 1 (P0 + P1 sumando las dos revisiones).

6. **Corrige la ronda 1 en un solo lote.**

   ```text
   Aplica todos los FIX_NOW en un único cambio. Ejecuta los tests. Haz un solo push.
   Crea UNA issue de seguimiento (gh issue create) con todos los DEFER_TO_ISSUE,
   cada uno con su motivo y un enlace a este PR. Publica el registro como
   comentario del PR, con el enlace a la issue. Para cada hilo de revisión: léelo,
   responde con su veredicto y su motivo, y después resuélvelo.
   ```

   **Punto de control:** `python -m unittest` pasa en la carpeta del proyecto de práctica (o pasa el comando de tests de tu repositorio). `gh issue list` muestra la issue de seguimiento. `gh pr view <n> --json additions,deletions` te da el tamaño del diff de la ronda 1 para tu registro.

7. **Haz la ronda 2.** Repite los pasos 3, 4 y 5 añadiendo estas líneas a los dos prompts de revisión:

   ```text
   En este PR hay publicado un registro de la ronda 1. No vuelvas a plantear temas
   ya decididos ahí salvo que tengas evidencia nueva. Si la tienes, di qué es nuevo.
   ```

   Etiqueta cada hallazgo de la ronda 2: *problema nuevo en el cambio original* o *derivado* (consecuencia de una corrección de la ronda 1, tema aparcado que vuelve, pregunta de producto, hipótesis más allá del contexto o contradicción entre revisores).

   **Punto de control:** tu registro tiene el número de hallazgos de prioridad alta de la ronda 2, y cada hallazgo tiene su etiqueta.

8. **Cierra por decisión.** Si los hallazgos de prioridad alta no bajaron, o la mayoría de los de la ronda 2 son derivados, para aquí aunque queden hallazgos:

   ```text
   Para el bucle de correcciones. Dame una evaluación exigente, sí o no, del PR #<n>
   frente a su declaración de intención: ¿qué se le rompería a un usuario si
   hiciéramos merge ahora? Después clasifica todos los hallazgos abiertos en un
   registro final, responde y resuelve cada hilo con su motivo, añade lo aplazado a
   la issue de seguimiento que ya existe y confirma que no se descartó ningún
   hallazgo de seguridad. No hagas push de código.
   ```

   Si los hallazgos de prioridad alta sí bajaron y quedan FIX_NOW reales, haz primero un lote más (paso 6) y después cierra de la misma manera.

   Después decides **tú**. Haz merge del PR o publica un comentario que explique por qué no.

   **Punto de control:** existe un comentario con el registro final, no queda ningún hilo sin resolver (ver el comando de abajo) y tu decisión consta en el PR.

## Cómo saber que has terminado

- [ ] La descripción del PR empieza con una declaración de intención: `gh pr view <n>`.
- [ ] Hay dos comentarios de revisión de dos revisores distintos: `gh pr view <n> --comments`.
- [ ] Cada ronda tiene un registro en el que cada hallazgo tiene un veredicto y un motivo.
- [ ] Ningún hallazgo de seguridad tiene el veredicto DISCARD.
- [ ] Todo lo aplazado vive en una única issue de seguimiento: `gh issue list`.
- [ ] Los tests pasan: `python -m unittest` en la carpeta del proyecto de práctica, o el comando de tests de tu repositorio.
- [ ] No queda ningún hilo de revisión sin resolver. Este comando no imprime nada:

  ```bash
  gh api graphql --paginate -f owner=<owner> -f repo=<repo> -F number=<n> -f query='
  query($owner: String!, $repo: String!, $number: Int!, $endCursor: String) {
    repository(owner: $owner, name: $repo) {
      pullRequest(number: $number) {
        reviewThreads(first: 100, after: $endCursor) {
          pageInfo { hasNextPage endCursor }
          nodes { isResolved path }
        }
      }
    }
  }' --jq '.data.repository.pullRequest.reviewThreads.nodes[] | select(.isResolved == false) | .path'
  ```

- [ ] Tu registro muestra los hallazgos de prioridad alta y el tamaño del diff de cada ronda.
- [ ] Hiciste tú el merge del PR, no un agente, o dejaste por escrito por qué no.

## Reflexiona

- ¿Qué hallazgo menos querrías ver llegar a producción? ¿Lo habría detectado el otro revisor?
- ¿Cuánto creció el diff entre la ronda 0 y tu última ronda? ¿Qué parte de ese crecimiento servía al objetivo y qué parte vino de los revisores?
- ¿Qué ASK te costó más decidir? ¿Qué línea que faltaba en la declaración de intención lo habría decidido por ti?
- ¿Dónde paraste y qué señal te dijo que parases?
- ¿Qué partes del diff leíste línea a línea y por qué esas?

## Para ir más allá

- **Revisor especialista.** Añade un subagente con una sola pregunta. Para C2, por ejemplo: "¿Se puede perder o reescribir en silencio un archivo v1 durante la migración?". Haz que se ejecute solo cuando cambie `shelf/store.py` y que informe con el formato del registro.
- **Reglas en el repositorio.** Deja escritas tus reglas de revisión para que un bot las aplique en cada PR: una sección `## Code Review Rules` en `AGENTS.md` para el revisor de Codex en GitHub, o un `REVIEW.md` para la revisión gestionada de Claude Code. Consulta la [referencia de herramientas](../reference/tools.md).
- **Prompt request.** Escribe la S7 ("Hacer shelf más útil para clubes de lectura") como una prompt request: la intención, los prompts que usarías y cómo verificarías el resultado. Pásasela a una sesión limpia y compara el PR que produce con uno construido a partir de la issue de una línea.
