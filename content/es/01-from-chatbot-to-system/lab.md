---
title: "Laboratorio 1 — Mide tu punto de partida"
module: 1
kind: lab
minutes: 60
level: foundation
last_reviewed: 2026-09-17
---

# Laboratorio 1 — Mide tu punto de partida

## Objetivo

Medir una semana normal de cómo trabajas hoy con agentes de programación, anotar tu punto de partida y fijar un objetivo. Necesitarás esta medición en el [módulo 10](../10-your-30-day-plan/README.md), cuando compares tu propio antes y después.

Por qué molestarse: en el [estudio de METR de 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), desarrolladores con experiencia creían que la IA los había hecho un 20 % más rápidos cuando los había hecho un 19 % más lentos. Tu impresión sobre tu propia velocidad no es un dato. Una semana de registro sencillo, sí.

Este laboratorio lleva alrededor de una hora de tiempo activo repartida a lo largo de una semana: 15 minutos para prepararlo, dos minutos unas cuantas veces al día para registrar y unos 40 minutos al final para calcular y escribir. El recuento del retrabajo necesita una comprobación más, de cinco minutos, una semana después.

## Antes de empezar

- **Elige una semana normal.** Ni una semana de vacaciones, ni una de incidencias, ni la semana en que cambias de herramienta. Mide cómo trabajas *ahora*, antes de aplicar nada de los módulos siguientes.
- **Localiza dónde aparece tu consumo.** Cada agente muestra el uso del plan o el gasto a su manera, con una vista de uso en la propia herramienta o en la página de la cuenta del proveedor. La [referencia de herramientas](../reference/tools.md) indica dónde mirar en los agentes más habituales; para Claude Code, consulta [la gestión de costes](https://code.claude.com/docs/en/costs).
- **Comprueba la GitHub CLI** con `gh auth status`. La usarás para contar pull requests.
- **Elige un sitio privado para tus notas**, fuera de cualquier repositorio de trabajo. Tu punto de partida puede incluir gasto, y es tuyo, no un informe de rendimiento.

**Con el proyecto de prácticas:** si en una semana normal no escribes mucho código, usa [shelf](../../../practice/shelf/) como tu "trabajo". Toma las issues S3 a S6 del [catálogo de issues](../../../practice/issues/es.md), una o dos al día, trabajando como lo haces hoy, y registra exactamente como se describe abajo. Hazlo en una segunda copia del proyecto, por ejemplo `~/code/shelf-baseline` publicada como un repositorio aparte, porque los laboratorios 2, 3 y 6 implementan esas issues en tu copia principal. Las cifras serán menos realistas, pero verás igualmente tus hábitos.

**En tu propio repositorio:** es la mejor opción. Registra tu trabajo real en tus repositorios reales.

## Pasos

### 1. Escribe primero tus estimaciones (5 minutos)

Antes de medir nada, crea `baseline.md` y escribe tus estimaciones honestas:

```markdown
## Estimaciones (escritas antes de medir)
- Pull requests que mergeo en una semana típica:
- Sesiones de agente que tengo a la vez durante la mayor parte del día:
- Máximo de sesiones a la vez:
- Minutos al día que paso esperando a un agente o mirando cómo trabaja:
- Veces al día que compruebo algo que el agente podría haber comprobado:
- Veces al día que vuelvo a explicar el contexto del proyecto a un agente:
```

**Punto de control:** seis estimaciones escritas y fechadas.

### 2. Prepara un registro (10 minutos)

Crea `baseline-log.csv` al lado, con esta cabecera:

```text
date,time,repo,task,kind,parallel,waited_min,i_verified,re_explained
```

Añade una fila cada vez que abras una sesión de agente:

| Columna | Qué escribir |
|---|---|
| `kind` | `plan`, `implement`, `review`, `question` u `other` |
| `parallel` | Cuántas otras sesiones de agente estaban activas cuando abriste esta |
| `waited_min` | Minutos que pasaste mirando o esperando a esta sesión en lugar de hacer otra cosa (estímalo al cerrarla) |
| `i_verified` | Cuántas veces ejecutaste tests o comprobaste una salida que el agente podría haber comprobado |
| `re_explained` | Cuántas veces explicaste un contexto del proyecto que el agente ya debería tener |

Fila de ejemplo:

```text
2026-09-21,10:40,billing-api,fix rounding bug,implement,1,12,2,1
```

> [!TIP]
> Ten el registro abierto en un panel lateral, o dicta las filas al cerrar cada sesión. Si se te olvida alguna, muchas herramientas permiten listar las sesiones anteriores (en Claude Code, `/resume` las muestra), lo que te ayuda a rellenar huecos al final del día. Un registro aproximado es mejor que uno perfecto que abandonas el miércoles.

**Punto de control:** al final del primer día, el registro tiene una fila por cada sesión que recuerdas haber abierto.

### 3. Anota el uso y el gasto de tu plan al principio y al final de la semana (5 minutos en total)

El primer día y el último, anota para cada herramienta: el plan y su cuota mensual, el uso o gasto que muestra, cualquier uso extra o gasto de API y si llegaste a algún límite durante la semana (y cuándo).

**Punto de control:** dos lecturas por herramienta, o una nota diciendo que la herramienta no muestra el uso, y una cifra de cuota o de gasto por cada herramienta que pagas.

### 4. Cuenta tus pull requests y tus minutos al final de la semana (15 minutos)

En cada repositorio en el que hayas trabajado, guarda junto a tus notas los pull requests mergeados con sus fechas, y lista los abiertos:

```bash
gh pr list --author "@me" --state merged --search "merged:>=YYYY-MM-DD" --limit 100 \
  --json number,title,createdAt,mergedAt > ~/baseline/merged-prs-REPO.json
gh pr list --author "@me" --state open
```

Sustituye `YYYY-MM-DD` por el primer día de tu semana, `REPO` por el nombre del repositorio y `~/baseline` por la carpeta privada donde guardas `baseline.md`. Si trabajas en muchos repositorios, el buscador web de GitHub acepta el mismo filtro: `is:pr author:@me is:merged merged:>=YYYY-MM-DD`. El script del paso 5 convierte los archivos guardados en un recuento y una mediana del **tiempo de ciclo**, desde que se abre un pull request hasta que se mergea. Mantén ese evento de inicio: el módulo 10 compara con él.

Estima los **minutos humanos por pull request mergeado**. Elige cinco pull requests mergeados, mezclando pequeños y grandes. Para cada uno, estima los minutos que dedicaste a leer, decidir y desbloquear, redondeando a 5, con ayuda de tu calendario, las notificaciones y la memoria. Haz la media de los cinco.

Cuenta también el **retrabajo**: pull requests mergeados esta semana que necesitaron un arreglo posterior o una reversión en los 7 días siguientes al merge. Los que se mergearon al final de la semana aún no han tenido sus 7 días, así que ponte un recordatorio en el calendario y vuelve a comprobar este número una semana después de que termine la semana.

**Punto de control:** cuatro números: mergeados, todavía abiertos, minutos humanos por pull request mergeado y retrabajo, con un recordatorio para volver a comprobar el retrabajo.

### 5. Que el agente escriba la aritmética, no que la haga (10 minutos)

No pegues tu registro en un chat para pedir totales. Un modelo de lenguaje puede copiar mal un número y seguir sonando seguro. Pide un script y ejecútalo tú:

❌ **Prompt débil**

```text
aquí tienes mi registro, dame las medias
```

✅ **Prompt mejor**

```text
Escribe un script de Python, summarize.py, solo con la biblioteca estándar,
que lea baseline-log.csv (columnas: date,time,repo,task,kind,parallel,
waited_min,i_verified,re_explained) y muestre: número de sesiones, sesiones
por día, máximo y mediana de (parallel + 1), total y media diaria de
waited_min, total de i_verified, total de re_explained y un recuento de
sesiones por kind. Que lea también todos los archivos merged-prs-*.json de la
carpeta (una lista JSON de objetos con createdAt y mergedAt) y muestre el
número de pull requests mergeados y la mediana de horas entre createdAt y
mergedAt. Muestra un aviso por cada fila o entrada que no pueda interpretar,
en lugar de saltársela en silencio. No leas ni muestres nada más. Lo ejecutaré yo.
```

Ejecútalo (usa `python3` si así se llama Python 3 en tu máquina):

```bash
python summarize.py baseline-log.csv
```

Comprueba a mano un número, por ejemplo el número de sesiones de un día. Si no coincide, arregla el script, no el número.

**Punto de control:** el script se ejecuta, no muestra avisos sin explicar y un número coincide con tu comprobación manual.

### 6. Escribe tu punto de partida (10 minutos)

Añade esto a `baseline.md` y rellena cada fila o escribe "sin datos":

```markdown
## Medido: semana del YYYY-MM-DD
| Métrica | Estimación | Medido | Fuente |
|---|---|---|---|
| Pull requests mergeados | | | summarize.py |
| Tiempo de ciclo, apertura → merge (mediana en horas) | — | | summarize.py |
| Minutos humanos por pull request mergeado (muestra de cinco) | — | | mi estimación |
| Coste por pull request mergeado (gasto en IA de la semana ÷ mergeados) | — | | cuotas y gasto del paso 3 |
| Retrabajo (PR mergeados que necesitaron un arreglo posterior o una reversión en 7 días) | — | | gh pr list + memoria, revisado una semana después |
| Sesiones por día | — | | summarize.py |
| Sesiones a la vez habitualmente (mediana) | | | summarize.py |
| Máximo de sesiones a la vez | | | summarize.py |
| Minutos al día esperando a un agente o mirándolo | | | summarize.py |
| Veces que verifiqué lo que podía verificar el agente | | | summarize.py |
| Veces que volví a explicar el contexto | | | summarize.py |
| Uso del plan al final de la semana, por herramienta | — | | vista de uso |
| Límites alcanzados (cuándo) | — | | vista de uso |

## Dónde estoy hoy
Un párrafo: ¿autocompletado, chatbot, unas pocas sesiones en paralelo o muchas pistas?
¿Qué síntoma de la tabla de diagnóstico del módulo 01 encaja mejor conmigo?

## Mi objetivo para el plan de 30 días
- Un número de práctica que quiero mover (por ejemplo: "verifico por el agente 15 veces a la semana → 3"):
- Un número de resultado que no puede empeorar (por ejemplo: retrabajo):
```

Para el gasto en IA de la semana, prorratea a una semana la cuota mensual de cada plan (cuota × 12 ÷ 52) y súmale el uso extra o el gasto de API del paso 3. El [módulo 08](../08-token-economics/README.md) explica cómo leer el coste por pull request mergeado sin engañarte.

**Punto de control:** la tabla está completa y cada objetivo tiene un número.

### 7. Elige objetivos que no se puedan maquillar (5 minutos)

Vuelve a mirar tus objetivos. Un objetivo como "tener 5 sesiones a la vez" es fácil de cumplir y no dice nada de los resultados. Empareja cada objetivo de actividad con un resultado que tenga que mantenerse: pull requests mergeados que no necesitaron retrabajo, o tiempo de revisión por pull request.

**Punto de control:** cada objetivo de actividad tiene al lado un número de resultado.

## Cómo saber que has terminado

- [ ] `baseline-log.csv` cubre cinco días laborables, con una fila por sesión.
- [ ] `python summarize.py baseline-log.csv` se ejecuta sin avisos sin explicar.
- [ ] `baseline.md` tiene tus estimaciones, la tabla de mediciones con cada fila rellena o marcada como "sin datos" y un párrafo breve de "Dónde estoy hoy".
- [ ] La tabla incluye los números que compara el módulo 10: pull requests mergeados, tiempo de ciclo, minutos humanos por pull request mergeado, coste por pull request mergeado y retrabajo (revisado una semana después).
- [ ] Has escrito un objetivo de práctica y uno de resultado, cada uno con un número.
- [ ] Los archivos están guardados en un sitio donde los encontrarás en el módulo 10.

## Reflexiona

- **¿Dónde estuvo la mayor diferencia entre tus estimaciones y las mediciones?** Recuérdala la próxima vez que tengas la sensación de ir más rápido.
- **¿En qué se fue tu tiempo?** ¿Esperando, verificando por el agente o volviendo a explicar? Cada cosa apunta a un módulo: el [06](../06-run-sessions-in-parallel/README.md), el [03](../03-close-the-loop/README.md) y el [04](../04-context-is-infrastructure/README.md).
- **¿Cambió la medición tu forma de trabajar esta semana?** Suele pasar. Anótalo, para no contar ese cambio como progreso más adelante.
- **¿Qué síntoma arreglarías primero** si solo pudieras arreglar uno?

## Para ir más allá

- **Un punto de partida de equipo.** Haz el laboratorio con tu equipo y comparte solo datos agregados. Acuerda con tu equipo de antemano que las cifras de nadie se usarán para evaluar su rendimiento, o la gente registrará lo que crea que quieres ver.
- **Compáralo con el laboratorio 0.** Relee tus tres líneas del [laboratorio 0](../00-start-here/lab.md). ¿Las confirmó la semana?
