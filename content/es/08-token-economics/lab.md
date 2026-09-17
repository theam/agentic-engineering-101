---
title: "Laboratorio 8 — Tu coste por PR mergeado y tus principales sumideros de tokens"
module: 8
kind: lab
minutes: 60
level: advanced
last_reviewed: 2026-09-17
---

# Laboratorio 8 — Tu coste por PR mergeado y tus principales sumideros de tokens

## Objetivo

Mide una semana real de trabajo con agentes en las unidades de [la lección](README.md): **coste por PR mergeado**, **tasa de retrabajo** y **minutos humanos por PR**. Después encuentra tus **tres principales sumideros de tokens**, cada uno respaldado por un número, y elige para cada uno un cambio que puedas medir la semana que viene.

## Antes de empezar

- **Una semana de trabajo real con agentes.** Tu propio repositorio es el que da los números más útiles. En el [proyecto de práctica](../../../practice/shelf/), usa la semana en la que hiciste los laboratorios 5 a 7. Los números serán pequeños, pero el método es el mismo.
- **Tu punto de partida** del [laboratorio 1](../01-from-chatbot-to-system/lab.md).
- **Acceso a lo que pagas**: pantallas de uso de los planes, facturas, la consola de la API si tienes claves y las facturas de los servicios de revisión.
- `gh` con la sesión iniciada (`gh auth status`).
- **Un sitio donde apuntar los resultados** en la base de conocimiento (knowledge base) del [laboratorio 4](../04-context-is-infrastructure/lab.md), por ejemplo `kb/metrics/economics-<AAAA-MM-DD>.md`.

> [!WARNING]
> Las cifras de gasto son privadas. Si tu base de conocimiento vive en un repositorio público, guarda este archivo en otro sitio.

## Pasos

1. **Fija la ventana.** Elige siete días que terminaran hace al menos una semana, para que cada PR mergeado en ellos haya tenido sus 7 días para necesitar retrabajo. Crea el archivo de resultados y escribe arriba las fechas de inicio y fin (`START` y `END`, con formato `AAAA-MM-DD`). En un workshop, o si no puedes esperar, usa los siete días que terminan hoy y marca la tasa de retrabajo como provisional.

   **Punto de control:** el archivo existe con el rango de fechas.

2. **Cuenta los PR mergeados (N).**

   ```bash
   gh pr list --state merged --author @me --search "merged:START..END" --limit 200 \
     --json number,title,additions,deletions,mergedAt
   ```

   `gh pr list` devuelve solo 30 resultados por defecto, así que `--limit` importa. Es la misma trampa de truncado que viste en el módulo 7. Si tus agentes abren los PR con otra cuenta, cambia `--author`. Guarda el JSON y añade `--jq length` para obtener el total.

   **Punto de control:** N está apuntado y la lista, guardada.

3. **Clasifica el retrabajo (R).** Pasa la lista guardada a una sesión nueva:

   ```text
   Estos son los PR que mergeé entre START y END (JSON abajo). Un PR tiene
   retrabajo si un PR posterior lo arregló o lo revirtió en los 7 días siguientes
   a su merge. Para cada PR, busca ese seguimiento entre los PR mergeados desde
   START (gh pr list --state merged --search "merged:>=START"), y lee la
   descripción de los PR y las issues enlazadas con gh pr view cuando un título
   sea ambiguo. Marca cada PR con o sin retrabajo, da como evidencia el PR de
   seguimiento de cada uno con retrabajo, y devuelve una tabla y el total.
   ```

   Contrasta las reversiones con una búsqueda:

   ```bash
   gh pr list --state merged --search "revert in:title merged:>=START" --limit 200 --json number,title
   ```

   **Punto de control:** R = PR de la ventana que necesitaron un arreglo posterior o una reversión en 7 días, con el PR de seguimiento como evidencia en cada uno. Has comprobado tú al menos dos clasificaciones.

4. **Reúne el gasto en IA (S) de la ventana.**
   - Suscripciones: cuota mensual × 12 ÷ 52 da la parte semanal de cada una.
   - Uso extra por encima de tus planes, claves de API de bots y CI, y servicios que cobran por revisión: toma los importes de la ventana en cada página de facturación.
   - Margen del plan: apunta qué parte de tus límites usaste, o cuántas veces llegaste a un límite. Una cuota fija lo esconde.

   En Claude Code, `/usage` muestra el uso del plan y un desglose por skills, subagentes, plugins y servidores MCP ([documentación de costes](https://code.claude.com/docs/en/costs)). Para otras herramientas, consulta la [referencia de herramientas](../reference/tools.md) o la página de uso del proveedor.

   **Punto de control:** una tabla con las líneas de gasto, cada una con su fuente, y el total S.

5. **Estima los minutos humanos (M) y el trabajo tirado (U).** Elige cinco PR mergeados, mezclando pequeños y grandes. Para cada uno, estima los minutos que dedicaste a leer, decidir y desbloquear, redondeando de 5 en 5. Usa tu calendario, las notificaciones y la memoria. La media de los cinco es M. Después cuenta los PR que cerraste sin merge:

   ```bash
   gh pr list --state closed --author @me --search "is:unmerged closed:START..END" --limit 200 --json number,title
   ```

   **Punto de control:** M y U están apuntados.

6. **Calcula los números por unidad.** Rellena esta tabla en tu archivo de resultados:

   ```markdown
   | Métrica | Fórmula | Valor |
   | --- | --- | --- |
   | Coste por PR mergeado | S ÷ N | |
   | Tasa de retrabajo | R ÷ N | |
   | Coste por PR mergeado neto | S ÷ (N − R) | |
   | Minutos humanos por PR mergeado | M | |
   | Minutos humanos de la semana | M × N | |
   | PR cerrados sin merge | U | |
   ```

   La lección tiene un [ejemplo resuelto](README.md#un-ejemplo-resuelto) si quieres comprobar tus cuentas.

   **Punto de control:** todos los valores están rellenos. Junto a la tabla, escribe una frase que compare estos números con tu punto de partida del laboratorio 1.

7. **Reúne evidencia de los sumideros de tokens.**
   - **Rondas de revisión.** En tus cinco PR mergeados más grandes, ejecuta `gh pr view <n> --json reviews --jq '.reviews | length'`.
   - **Contexto que se carga siempre.** Ejecuta `wc -l AGENTS.md CLAUDE.md`, o lo equivalente para tus archivos de instrucciones. Después mira cuánto contexto usa una sesión nueva antes de tu primer mensaje (en Claude Code, `/context`).
   - **Hábitos de sesión.** En Claude Code, `/insights` genera un informe sobre los puntos de fricción de tus sesiones recientes ([documentación de costes](https://code.claude.com/docs/en/costs)). Apunta también cualquier sesión que tuvieras abierta todo el día.

   Después pregunta a una sesión nueva:

   ```text
   Ayúdame a encontrar mis 3 principales sumideros de tokens de la semana. Evidencia:
   - PR mergeados: N, PR con retrabajo: R, cerrados sin merge: U
   - rondas de revisión en mis 5 PR más grandes: <números>
   - archivos de instrucciones: <salida de wc -l>; contexto usado antes de mi primer
     mensaje: <valor>
   - desglose de uso y avisos: <pegar>
   - otras observaciones: <por ejemplo "una sesión estuvo abierta todo el martes">
   Ten en cuenta estos sumideros habituales: bucles de revisión que persiguen el
   crecimiento del alcance, contexto siempre cargado e hinchado, demasiadas
   herramientas o skills, volver a deducir lo que ya se sabe, sesiones largas,
   salida de herramientas muy verbosa, un modelo haciendo lo que debería hacer el
   código, uso en segundo plano, trabajo que se tira.
   Ordena los 3 principales por coste probable. Para cada uno da: la evidencia (un
   número), un cambio y la métrica que dirá la semana que viene si el cambio
   funcionó. No propongas cambios que pasen trabajo de los agentes a mí.
   ```

   **Punto de control:** tres sumideros, cada uno con un número, un cambio y una métrica. Rechaza cualquier sumidero cuya única evidencia sea un adjetivo ("las sesiones se hacen largas").

8. **Apunta y haz commit.** Añade al archivo de resultados los tres sumideros y un párrafo breve de "la semana que viene voy a…". Haz commit en tu base de conocimiento.

   **Punto de control:** `git log -1 --stat` muestra el archivo.

## Cómo saber que has terminado

- [ ] N, R, U, S y M están apuntados, cada uno con su fuente (un comando o una página de facturación).
- [ ] El coste por PR mergeado, la tasa de retrabajo, el coste por PR mergeado neto y los minutos humanos están calculados, con las fórmulas a la vista.
- [ ] Hay tres sumideros de tokens, cada uno respaldado por un número.
- [ ] Cada sumidero tiene un cambio y una métrica para comprobar la semana que viene.
- [ ] Los resultados están comparados con tu punto de partida del laboratorio 1.
- [ ] El archivo tiene commit en tu base de conocimiento: `git log -1 --stat`.
- [ ] No hay cifras de gasto en ningún repositorio público.

## Reflexiona

- ¿Qué pesó más en tu semana, el gasto en IA o los minutos humanos? ¿Te sorprendió?
- ¿Dónde gastarías con gusto más tokens para ahorrarte minutos a ti?
- ¿De cuál de tus números te fías menos, y por qué?
- ¿Parte de tu trabajo parecía productivo por líneas de código pero no por PR mergeados sin retrabajo?

## Para ir más allá

- **Comparativa de modelos.** En el proyecto de práctica, implementa la S3 (`shelf stats`) dos veces, en dos worktrees, con el mismo prompt: una con el modelo más potente y otra con uno más barato. Compara si pasan los tests, cuántas correcciones necesitó cada uno, qué encuentra el revisor del laboratorio 7, los tokens usados y el tiempo de reloj. Busca trabajo con trampa, como tests editados o salidas escritas a mano, y comprueba el criterio más delicado de la issue: tests que no dependan de la fecha de hoy.
- **Filtra la salida de los tests.** Añade un hook que recorte la salida de los tests a los fallos (la [documentación de costes](https://code.claude.com/docs/en/costs) tiene un ejemplo). Compara el contexto usado en una tarea con muchos tests antes y después.
- **Visión de equipo.** Aplica las mismas fórmulas a cada persona de tu equipo y después revisa con el equipo los números por unidad, no las facturas.
