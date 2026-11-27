---
title: "Del chatbot al sistema · Lectura"
kind: reading
last_reviewed: 2026-11-27
---

# Módulo 01 · Del chatbot al sistema

<!-- Versión escrita del módulo para Agentic Engineer Academy. Una parte por vídeo, en el mismo orden. Formato: docs/reading-format.md. -->

## Parte 1 · Qué es el agentic engineering

<!-- minutes: 4 -->

> Lo que importa no es cuánto código escribe el agente. Es si alguien diseñó una forma de fiarse del resultado.

### Tres formas de trabajar con un agente de código

La mayoría de los ingenieros pasa por tres formas de trabajar. Se diferencian en quién escribe el código, quién lo comprueba y dónde vive la memoria del proyecto.

| | Autocompletado | Chatbot | Sistema |
|---|---|---|---|
| | Escribes y aceptas. | Pides, esperas y lees. | Diseñas, decides y revisas. |
| Quién escribe | Tú | El agente | Agentes, en paralelo |
| Quién comprueba | Tú | Normalmente tú | El agente, y después tú |
| Memoria | Tu cabeza | El chat | El repositorio |

La forma chatbot es donde se queda la mayoría. Funciona, pero **te conviertes en el cuello de botella y en la memoria**: cada resultado espera a que lo compruebes, y cada chat nuevo olvida el proyecto. La forma sistema saca esos dos trabajos de tu cabeza.

### Qué significa agentic engineering

La forma sistema tiene nombre: **agentic engineering (ingeniería agéntica)**. Los agentes escriben la mayor parte del código y tú diseñas el sistema que los rodea. Ese sistema tiene cuatro partes:

- **Contexto:** lo que el agente sabe del proyecto cuando empieza.
- **Descomposición:** cómo se reparte el trabajo en tareas.
- **Verificación y revisión:** cómo se comprueban los resultados, y quién lo hace.
- **Decisiones:** cuáles se quedan contigo.

Dos cosas que la definición deja fuera a propósito:

- **Cuántos agentes usas.** Un agente bien llevado ya cuenta.
- **Que dejes de leer código.** Tú decides, según el riesgo, qué merece tu lectura.

### Lo que no es: vibe coding

DHH, el creador de Ruby on Rails, da la definición más clara de vibe coding: "No miras la implementación. Eso, para mí, es lo que separa el vibe coding de programar" (traducción propia).

No todo el mundo usa el término así. Gene Kim y Steve Yegge, por ejemplo, lo usan para trabajo disciplinado con IA. Así que comprueba qué quiere decir cada uno. **En este curso, vibe coding es que nadie mira el código.**

> Puedes delegar lo que piensas, pero no lo que entiendes (traducción propia).
>
> Una frase que Andrej Karpathy, el investigador de IA que acuñó "vibe coding", cita y repite.

### En la práctica

La diferencia se ve incluso en un solo prompt. Shelf es el pequeño proyecto de práctica que usas en los laboratorios.

```prompt-weak
add csv export to shelf
```

```prompt-strong
Implement issue #4 (read it with gh issue view 4). Write the tests first and show me they fail, then implement. Run python -m unittest and paste the output. If something can't run, tell me exactly what didn't run and why. Open a pull request that closes #4.
```

El prompt mejor es corto porque se apoya en un sistema:

- **Una issue** que ya contiene la especificación.
- **Pruebas** que el agente puede ejecutar para comprobar su propio trabajo.
- **Un pull request** donde se revisa el resultado.

### Ideas clave

- El agentic engineering es un sistema que diseñas, no un prompt mejor.
- Un agente bien llevado ya cuenta.
- Vibe coding es que nadie mira el código.

## Parte 2 · El techo del chatbot

<!-- minutes: 4 -->

> Muchos ingenieros se quedan en la fase del chatbot. Un prompt mejor no los saca de ahí. Los cambios fuera del prompt, sí.

### La historia

Alguien empezó a usar un agente de código hace seis meses. Las primeras semanas fueron emocionantes. Después, el avance se estancó.

Hoy pega el mismo contexto del proyecto en cada ventana nueva. Pasa las pruebas por su cuenta, porque una vez el agente dijo "todas las pruebas pasan" sin haberlas ejecutado. Tiene la sensación de ir más rápido. No sabe si es así.

Ese estancamiento es el **techo del chatbot**: una ventana, un prompt, una tarea cada vez.

### Por qué la gente se queda ahí

No es pereza. La fase del chatbot compensa rápido, así que nada duele lo suficiente como para ir más allá.

Cada paso siguiente está fuera del prompt: pruebas que el agente puede ejecutar, una base de conocimiento (knowledge base, archivos que guardan lo que sabe el proyecto entre sesiones), el trabajo repartido en tareas, una rutina de revisión. **Cada uno parece trabajo de más la semana que lo añades, y solo compensa semanas después.**

### Por qué la distancia crece, y cómo se cierra

Quien hace estos cambios ve cómo se suman sus avances. Las correcciones se convierten en reglas que el agente lee al empezar cada sesión. Las comprobaciones repetidas se convierten en scripts. Su forma de trabajar mejora cada semana, mientras que una sesión de chatbot empieza de cero. Así que la distancia con quien se queda en el techo no deja de crecer.

**La buena noticia:** cada cambio es pequeño y se aprende. Bastan unas pocas semanas centradas en ello. El resto del curso te da el orden.

### Encuentra tu propio techo

Mira tus propios hábitos. Cada uno señala lo que falta, y el módulo que lo enseña.

| Si notas que | Lo que falta | Módulo |
|---|---|---|
| Pegas el mismo contexto en cada sesión nueva | Archivos de instrucciones y una base de conocimiento | 04 |
| Pasas tú las pruebas cuando el agente dice "hecho" | Comprobaciones que el agente ejecuta solo | 03 |
| Escribes "prompts perfectos" muy largos | Contexto y una conversación, no un prompt largo | 02 |
| Miras al agente trabajar porque no hay otra cosa que hacer | Trabajo repartido en tareas independientes | 05 y 06 |
| Lees cada cambio línea a línea | Revisión según el riesgo, con agentes que revisan primero | 07 |
| Llegas al límite de tu plan sin saber qué has conseguido con él | Coste por resultado | 08 |

### Ideas clave

- La fase del chatbot parece suficiente. Por eso la gente se queda.
- Lo que te mueve está fuera del prompt: comprobaciones, memoria, tareas y revisión.
- La distancia crece sola. Se cierra en pocas semanas en cuanto empiezas.

## Parte 3 · Tu trabajo cambia de sitio

<!-- minutes: 3 -->

> Cuando los agentes escriben la mayor parte del código, tu trabajo no desaparece. Pasa de escribir líneas a diseñar y juzgar el sistema.

### De escritor a arquitecto

Peter Steinberger, un ingeniero que lleva de cinco a diez agentes en un proyecto que construye casi en solitario, lo dice así: "No entiendo el código línea a línea. Eso, eso lo hace Codex por mí, pero yo soy el arquitecto" (traducción propia). Codex es el agente de código de OpenAI.

DHH lo compara con un maestro cuyos alumnos tallan mientras él dice cuándo fallan las proporciones. Eso incluye pedir a los agentes "hazlo más simple", algo que rara vez hacen por su cuenta.

### Lo que sigue siendo humano

Los agentes pueden encargarse de teclear. En todos los relatos en los que confía el curso, cuatro cosas se quedan contigo:

#### 1 · Criterio de producto

Decidir qué merece la pena construir.

#### 2 · Coherencia

Muchos cambios razonables pueden desgastar igualmente una arquitectura. Alguien cuida la forma del conjunto.

#### 3 · Verificación y aprobaciones

Qué significa "correcto", y quién aprueba los planes y mergea los cambios.

#### 4 · Comprensión

La suficiente para darte cuenta de cuándo se equivoca el agente.

### En la práctica

En The Agile Monkeys, la empresa detrás de este curso, quienes trabajan así describen su día como conversaciones, no como prompts. Planifican con un agente que ya conoce el proyecto, le piden que convierta el plan en issues y dedican su tiempo a aceptar planes, decidir y revisar.

### Lo que cuesta

No es buena noticia para todo el mundo. DHH: "lo vas a pasar mal adaptándote a la nueva realidad si lo único que te gustaba de programar era la parte mecánica" (traducción propia). Steinberger vivió lo contrario: "Siempre pensé que me gustaba programar, pero lo que de verdad me gusta es construir" (traducción propia).

También cansa más de lo que parece. El desarrollador Simon Willison dice que llevar varios agentes a la vez es "sorprendentemente eficaz, aunque agotador mentalmente" (traducción propia).

### Ideas clave

- Tu papel pasa de escribir líneas a ser el arquitecto.
- El criterio de producto, la coherencia, la verificación y las aprobaciones, y la comprensión siguen siendo humanos.
- Cansa más de lo que parece. Planifica tu ritmo.

## Parte 4 · No te fíes de tu sensación de velocidad

<!-- minutes: 4 -->

> Tu sensación de velocidad no es una prueba. Mide tus resultados antes y después.

### Lo que encontraron los estudios

El entusiasmo es fácil de encontrar. Las pruebas sólidas, no. Cada estudio midió algo distinto, así que lee cada uno con su límite.

#### METR · 2025 · Un 19 % más lentos, y se sintieron un 20 % más rápidos

16 desarrolladores con experiencia, sobre código que conocían bien, con herramientas de principios de 2025. **Límite:** un seguimiento de 2026 apunta a que ahora son más rápidos, pero no es concluyente.

#### DORA · 2025 · La IA amplifica lo que ya hay

Casi 5.000 profesionales. La IA magnifica los puntos fuertes y débiles que ya tiene un equipo. **Límite:** más ritmo de entrega, pero también más inestabilidad.

#### Faros AI · 2025 · El cuello de botella pasa a la revisión

Más de 10.000 desarrolladores. Más pull requests mergeados, revisiones más largas. **Límite:** datos de un proveedor, y solo correlación.

#### Microsoft · 2026 · Alrededor de un 24 % más de pull requests

Sus propios ingenieros, durante cuatro meses. **Límite:** un pull request mergeado no es el valor que aporta. Todavía no está revisado por pares.

### Por qué los resultados no coinciden

Los estudios parecen contradecirse. Cinco cosas explican la mayor parte de la diferencia:

- **El entorno.** METR 2025 probó a expertos sobre código que se saben de memoria, donde las personas son más fuertes.
- **La época.** Andrej Karpathy, el investigador de IA que acuñó "vibe coding", dijo que los agentes de código "básicamente no funcionaban antes de diciembre y básicamente funcionan desde entonces" (traducción propia), refiriéndose a diciembre de 2025.
- **Cómo está montado y la práctica.** Un agente que puede ejecutar las pruebas se comporta de forma muy distinta a uno que no puede. Y alguien en sus primeras semanas no es igual que alguien en su segundo año.
- **Lo que se mide.** El tiempo, los pull requests y el valor son cosas distintas. Lo que cada uno dice de sí mismo es la medida más débil.
- **El resto del sistema.** Las ganancias desaparecen si la revisión no puede absorber más cambios.

### Qué medir en su lugar

No midas líneas de código ni cuántos agentes usas. Mide resultados:

- **Pull requests mergeados.**
- **Tiempo de ciclo:** desde que abres un pull request hasta que se mergea.
- **Retrabajo:** pull requests mergeados que necesitaron un arreglo o una vuelta atrás en 7 días.
- **Tus minutos por pull request mergeado:** el tiempo que dedicas a leer, decidir y desbloquear.
- **Coste por pull request mergeado:** lo que gastaste en IA, dividido entre lo que mergeaste.

El laboratorio 1 te pide registrar una semana normal y apuntar estas cifras. No cambies tu forma de trabajar hasta tener la semana registrada.

### Ideas clave

- La gente se equivoca con su propia velocidad.
- La IA amplifica lo que un equipo ya hace bien y mal.
- No te fíes de la cifra de nadie. Mide la tuya.
