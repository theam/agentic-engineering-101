# Guía de autoría

[Read in English](authoring.md)

Cómo escribir para *Agentic Engineering 101*, tanto si eres una persona como un
agente que trabaja para una. La versión corta está en [AGENTS.md](../AGENTS.md).

## Para quién escribimos

Para un ingeniero que conoce git y al menos un lenguaje, que puede usar hoy un
agente de programación o no, y que tiene poco tiempo. Se saltará todo lo que no
cambie lo que hace el lunes.

## Voz

- **Primero lo concreto.** Empieza por una situación real, un prompt real o un
  fallo real, y después generaliza. Explica *por qué* importa algo antes de
  explicar *cómo*.
- **Frases cortas, palabras sencillas.** Sin palabras grandilocuentes
  ("revolucionario", "cambia las reglas del juego", "10x" sin contexto). Sin
  relleno.
- **Segunda persona del singular:** "you" en inglés, "tú" en español.
- **Señala con claridad los enfoques equivocados.** Mostrar un prompt débil al
  lado de uno mejor enseña más que describir solo el bueno. Seguimos los
  [consejos de Julia Evans sobre explicaciones](https://jvns.ca/blog/confusing-explanations/).
- **Honestidad.** Mantén los costes, los modos de fallo y la evidencia en
  contra. Cuando dos expertos respetados no coinciden, presenta ambas posturas y
  di qué hacemos nosotros y por qué.

### La práctica de la empresa y las personas

- Nuestra práctica se escribe con la voz de la empresa: "En The Agile Monkeys…",
  "uno de nuestros ingenieros…". Nunca nombramos a empleados ni a clientes. La
  práctica es del equipo, no de una persona.
- Quien contribuya desde fuera puede describir su propia práctica con su
  nombre, si quiere, o de forma anónima.
- Los números de nuestra propia práctica se marcan como *orientativos, no como
  benchmarks*.

### Cómo citar voces públicas

- Cita a personas y documentos por su nombre, con enlace, la primera vez que
  aparezcan en cada archivo.
- Citas: literales, de 25 palabras como máximo y enlazadas a la fuente (con
  marca de tiempo en audio y vídeo cuando la tengas).
- En español, traduce la cita y añade "(traducción propia)":
  `> «…» — DHH en [Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/) (traducción propia)`
- Añade cada fuente externa nueva a `content/*/reference/sources.md`.

### Herramientas

- **Principios en las lecciones, herramientas como ejemplo.** Una lección tiene
  que seguir teniendo sentido aunque la herramienta que menciona desaparezca el
  mes que viene.
- **Nunca te inventes un flag, un comando o una clave de configuración.**
  Compruébalo en la documentación oficial y enlázala.
- `content/*/reference/tools.md` es el sitio, con fecha, para el detalle de
  herramientas que cambia a menudo. Actualiza su fecha `last_reviewed` cuando
  lo toques. Las lecciones usan ejemplos concretos de herramientas (un hook, un
  flag, un archivo de configuración) cuando enseñan un principio, comprobados
  en la documentación oficial y enlazados.
- No nombres versiones concretas de modelos en las lecciones. Escribe "el
  modelo más potente al que tengas acceso".

### Confidencialidad

Nada que no pudiera publicarse en un blog público: ni nombres de clientes, ni
URLs internas, ni identificadores de infraestructura, ni credenciales, ni
información comercial, ni datos personales.

## Plantillas

`scripts/check_content.py` valida el front matter y los encabezados obligatorios
de abajo. Todo lo demás queda a tu criterio.

### Lección: `content/<lang>/NN-slug/README.md`

```markdown
---
title: "Cierra el ciclo"
module: 3
kind: lesson
minutes: 40
level: foundation        # foundation | intermediate | advanced
last_reviewed: 2026-09-17
---

# 3. Cierra el ciclo

> **En una frase:** …

## Lo que serás capaz de hacer
## Por qué importa
## <tus secciones de conceptos>
## Otras formas de verlo          (opcional, muy recomendable)
## Ojo con
## Comprueba lo que has aprendido (respuestas dentro de <details>)
## Ideas clave
## Para profundizar               (termina con "Siguiente: …")
```

### Laboratorio: `content/<lang>/NN-slug/lab.md`

```markdown
---
title: "Laboratorio 3 — Dale al agente una forma de comprobarse"
module: 3
kind: lab
minutes: 45
level: foundation
last_reviewed: 2026-09-17
---

## Objetivo
## Antes de empezar
## Pasos                           (numerados, cada uno con un punto de control observable)
## Cómo saber que has terminado    (una lista, idealmente verificable con un comando)
## Reflexiona
## Para ir más allá                (opcional)
```

Cada laboratorio funciona con el [proyecto de prácticas](../practice/shelf/) *y*
con el repositorio propio de quien lo hace.

### Páginas de referencia y apéndice

Front matter con `title`, `kind` (`reference` o `appendix`) y `last_reviewed`.
Estructura libre.

### Encabezados obligatorios por idioma

| Inglés | Español |
|---|---|
| What you'll be able to do | Lo que serás capaz de hacer |
| Why this matters | Por qué importa |
| Other ways to see it | Otras formas de verlo |
| Watch out | Ojo con |
| Check your understanding | Comprueba lo que has aprendido |
| Key points | Ideas clave |
| Go further | Para profundizar |
| Goal | Objetivo |
| Before you start | Antes de empezar |
| Steps | Pasos |
| Done when | Cómo saber que has terminado |
| Reflect | Reflexiona |
| Stretch | Para ir más allá |

## Convenciones

### Avisos

Usamos las [alertas de GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts):

```markdown
> [!NOTE]
> **En The Agile Monkeys** mantenemos el índice que siempre se carga por debajo de 100 líneas.

> [!TIP]
> Un atajo práctico.

> [!WARNING]
> Un riesgo que no se puede pasar por alto.

> [!IMPORTANT]
> Una regla que no nos saltamos.
```

### Parejas de prompts

````markdown
❌ **Prompt débil**

```text
arregla el bug
```

✅ **Prompt mejor**

```text
El comando export falla con libros sin autor. Reprodúcelo primero con un test
que falle y después arréglalo. No cambies el formato del CSV.
```
````

### Diagramas y enlaces

- Los diagramas
  [Mermaid](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams)
  son bienvenidos. Mantenlos pequeños. Nada de imágenes binarias.
- Usa textos de enlace descriptivos, nunca "aquí". Dentro del repositorio, usa
  enlaces relativos.

## Convenciones del español

- Español neutro y "tú". Evita regionalismos, y "vosotros" y "ustedes" siempre
  que puedas.
- Estos términos se quedan en inglés: prompt, commit, merge, pull request (PR),
  issue, backlog, worktree, hook, skill, token, pipeline, CI, checkout, workshop.
- Estos se traducen: branch → *rama*, subagent → *subagente*, session →
  *sesión*, context window → *ventana de contexto*, plan mode → *modo plan*,
  blast radius → *radio de impacto*, lab → *laboratorio*, file → *archivo*
  (no "fichero"), cost → *coste*, merged → *mergeado*, lethal trifecta →
  *trifecta letal*.
- *Loop* tiene dos traducciones. Los tres ciclos de la guía y "close the loop"
  son *ciclo*: *ciclo interno*, *ciclo de contexto*, *ciclo externo*, *cerrar
  el ciclo*. El bucle propio de un agente, los bucles de revisión, el bucle
  Ralph y otros bucles que siguen hasta que algo los para son *bucle*: *bucle
  agéntico*, *bucle de revisión*, *cerrar el bucle de revisión con una
  decisión*. *Cycle time* es *tiempo de ciclo*.
- Estos se explican la primera vez que aparecen: *base de conocimiento
  (knowledge base)*, *revisión de código (code review)*, *pista de trabajo
  (track)*, *barrera de seguridad (guardrail)*, *modo headless (no
  interactivo)*, *agentic engineering (ingeniería agéntica)*, *validación local
  completa (full gate)*.
- El [glosario](../content/es/reference/glossary.md) es la referencia. Si
  añades un término, añádelo en los dos idiomas.

## Traducción

- **El inglés es la fuente de verdad.** El español vive en la misma ruta dentro
  de `content/es/` (los archivos de la raíz usan un hermano `.es.md`).
- **Mismo pull request.** Cada cambio de contenido actualiza los dos idiomas.
  El español es una adaptación natural, no una traducción literal: misma
  estructura, mismos ejemplos, mismos enlaces.
- **Los agentes pueden hacer el borrador; las personas revisan.** Una traducción
  hecha por un agente necesita la revisión de alguien con dominio del idioma.
  Añade la etiqueta `translation-review` si no puedes hacer tú esa revisión
  (consulta la [política de IA](../AI_POLICY.es.md)).
- **El desfase se detecta con el historial de git.** El validador avisa cuando
  un archivo en inglés tiene un commit posterior al de su versión en español.
  Trata el aviso como una tarea pendiente.
- Más adelante serán bienvenidos otros idiomas. Abre antes una issue. Añadiríamos
  un nuevo árbol `content/<lang>/` siguiendo
  [el modelo de localización de Kubernetes](https://kubernetes.io/docs/contribute/localization/).

## Antes de abrir un pull request

- [ ] Los dos idiomas actualizados, con la misma estructura.
- [ ] `python3 scripts/check_content.py` pasa.
- [ ] Los comandos y flags nuevos están comprobados en la documentación oficial y enlazados.
- [ ] Las citas son literales, de ≤ 25 palabras y enlazadas. Las fuentes nuevas están en `sources.md`.
- [ ] Ni nombres de empleados, ni de clientes, ni detalles confidenciales.
- [ ] La asistencia de IA declarada en el pull request y en los trailers de los commits.
