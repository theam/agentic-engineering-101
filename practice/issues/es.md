# Issues de práctica para `shelf`

Este catálogo reúne nueve issues para [`shelf`](../shelf/README.md), el proyecto de práctica de esta guía. Los laboratorios las usan para practicar planificación, pistas de trabajo (tracks) en paralelo, merges y revisión de código (code review) sobre un proyecto tan pequeño que se lee en cinco minutos.

- **S1 a S6** son pequeñas e independientes. Puedes ejecutarlas a la vez.
- **C1 y C2** entran en conflicto entre sí. Las dos cambian el formato del archivo de la estantería.
- **S7** es corta pero deliberadamente vaga. Sirve para practicar la conversación antes de construir.

## Cómo usan los laboratorios este catálogo

| Laboratorio | Issues | Qué haces con ellas |
| --- | --- | --- |
| [Laboratorio 0: el juego completo](../../content/es/00-start-here/lab.md) | S1, S2 | Una sesión implementa S1. Mientras trabaja, una segunda sesión implementa S2 en un worktree. Una tercera sesión, nueva, revisa el pull request de S1. |
| [Laboratorio 2: un agente, bien usado](../../content/es/02-one-agent-done-well/lab.md) | S3 | Llevas una issue por el ciclo conversar → planificar → construir → verificar y apuntas cada corrección que haces. |
| [Laboratorio 3: cierra el ciclo](../../content/es/03-close-the-loop/lab.md) | S6 | Escribes primero los tests de S6, añades un hook Stop que ejecuta los tests y ves cómo devuelve a un agente a arreglar su implementación. |
| [Laboratorio 4: el contexto es infraestructura](../../content/es/04-context-is-infrastructure/lab.md) | C1, C2 | Sin código. Decides cuál de las dos hace merge primero y lo registras como la decisión `D-0001`. |
| [Laboratorio 5: descomponer en pistas](../../content/es/05-decompose-into-tracks/lab.md) | Todas | Creas en GitHub las issues que aún no existen, detectas los solapamientos y la pareja en conflicto, reutilizas `D-0001` para el orden de merge y escribes prompts de arranque para tres pistas: S4 y S5, C1, y C2. |
| [Laboratorio 6: sesiones en paralelo](../../content/es/06-run-sessions-in-parallel/lab.md) | S4, S5, C1, C2 | Ejecutas las tres pistas en tres worktrees, haces merge primero de S4 y S5, después de C1 y C2 en el orden que fija `D-0001`, y resuelves su conflicto. |
| [Laboratorio 7: agentes que revisan agentes](../../content/es/07-agents-review-agents/lab.md) | Un pull request del laboratorio 6, mejor el de C1 o el de C2 | Lo revisas con un revisor de contexto limpio y con un revisor de otro proveedor, y clasificas los hallazgos. |

Si te saltas un laboratorio, sus issues siguen abiertas. Los laboratorios 5 y 6 dicen dónde van.

S7 no tiene laboratorio propio. Úsala cuando quieras practicar cómo convertir una petición vaga en trabajo concreto. En el laboratorio 5, fíjate en si tu agente la planifica sin más o si primero hace preguntas. El [sprint en paralelo](../../workshops/es/README.md#el-sprint-en-paralelo) del día 2 del workshop intensivo se basa en ella: conversar sobre ella, dividirla en issues nuevas y ejecutarlas después en paralelo.

> [!TIP]
> Este catálogo también existe en inglés: [practice/issues/en.md](en.md). Crea las issues de GitHub en el idioma en el que tu equipo escribe sus artefactos. Tu agente entiende tus instrucciones en cualquiera de los dos idiomas.

## Cómo está escrita cada issue

Cada issue está lista para pegarla en GitHub:

- **Título:** empieza por el ID de la issue, para que la encuentres en cualquier herramienta.
- **Problema:** qué falta y por qué le importa a quien usa `shelf`.
- **Criterios de aceptación:** comprobaciones que puede verificar una persona que revisa o un agente. Cuando un test necesita un mensaje o un código de salida exactos, la issue los da.
- **Archivos que probablemente cambian:** los archivos que una buena implementación seguramente toca. Es una pista, no una regla.
- **Fuera de alcance:** lo que no hay que hacer en esta issue.
- **Seguridad en paralelo:** si la issue puede ejecutarse a la vez que las demás.

> [!NOTE]
> **En The Agile Monkeys** escribimos las issues para que una sesión nueva de un agente pueda tomar una sin ningún otro contexto. La issue es el prompt. Si una sesión nueva necesita que le expliques la issue, la issue no está terminada.

Las líneas de seguridad en paralelo usan dos términos a propósito:

- Un **solapamiento textual** significa que dos ramas editan las mismas líneas. Git se detiene y te pide que elijas. Resolverlo lleva un minuto y no exige ninguna decisión de producto.
- Un **conflicto semántico** significa que dos ramas cambian el mismo contrato, aquí el formato del archivo de la estantería. Git puede incluso hacer el merge sin quejarse, y el resultado seguir estando mal. Alguien tiene que tomar una decisión.

El [módulo 5](../../content/es/05-decompose-into-tracks/README.md) explica cómo aprovechar esto al dividir el trabajo en pistas.

## S1: Filtrar `shelf list` por estado

**Título:** `S1: Filtrar shelf list por estado`

### Problema

`shelf list` muestra todos los libros. En cuanto tu estantería tiene más de un puñado, no ves de un vistazo qué estás leyendo ahora ni qué viene después.

### Criterios de aceptación

- [ ] `shelf list --status reading` muestra solo los libros con estado `reading`, uno por línea, con el mismo formato y orden que `shelf list`.
- [ ] `--status` acepta exactamente `to-read`, `reading` y `done`. Cualquier otro valor termina con código 2 y escribe en stderr un error que nombra los valores válidos.
- [ ] Si ningún libro coincide, también con la estantería vacía, el comando escribe `No books with status reading.` (con el estado pedido) y termina con código 0.
- [ ] `shelf list` sin `--status` se comporta exactamente igual que antes.
- [ ] `python -m unittest` pasa, con tests nuevos para el filtro, el mensaje sin coincidencias y un estado no válido.

### Archivos que probablemente cambian

- `shelf/commands/list_books.py` (reutiliza `STATUSES` de `shelf/models.py`; ese archivo no necesita cambios)
- `tests/test_cli.py`, en la clase `ListCommandTest`

### Fuera de alcance

- Filtrar por cualquier otra cosa que no sea el estado.
- Cambiar el formato de salida de `shelf list`.

**Seguridad en paralelo:** Independiente de S2–S6 y de C2. C1 también cambia `shelf list` (añade `--tag`), así que S1 y C1 editan las mismas líneas de `shelf/commands/list_books.py`: un pequeño solapamiento textual. Haz primero el merge de S1.

## S2: Buscar libros por título o autor

**Título:** `S2: Buscar libros por título o autor`

### Problema

Para saber si un libro ya está en tu estantería, tienes que leer toda la salida de `shelf list`.

### Criterios de aceptación

- [ ] `shelf search TEXT` muestra todos los libros cuyo título o autor contiene `TEXT`, uno por línea, con el mismo formato y orden que `shelf list`.
- [ ] La búsqueda no distingue mayúsculas de minúsculas, tampoco en letras con tilde: `shelf search GARCÍA` encuentra `One Hundred Years of Solitude by Gabriel García Márquez`.
- [ ] Si nada coincide, el comando escribe `No books match "TEXT".` (con el texto buscado) y termina con código 0.
- [ ] `shelf search` sin `TEXT` es un error de uso y termina con código 2.
- [ ] El archivo de la estantería no se modifica.
- [ ] `python -m unittest` pasa, con tests nuevos para una coincidencia en el título, otra en el autor, mayúsculas y tildes, y ninguna coincidencia.

### Archivos que probablemente cambian

- `shelf/commands/search.py` (nuevo)
- `tests/test_search.py` (nuevo)

### Fuera de alcance

- Búsqueda aproximada, expresiones regulares o búsqueda por estado o etiqueta.

**Seguridad en paralelo:** Independiente. Solo añade archivos nuevos.

## S3: Mostrar estadísticas de lectura

**Título:** `S3: Mostrar estadísticas de lectura`

### Problema

No hay forma de ver cómo va tu lectura: cuántos libros esperan, cuántos estás leyendo y cuántos has terminado este año.

### Criterios de aceptación

- [ ] `shelf stats` escribe exactamente estas cuatro líneas, en este orden, y termina con código 0:

  ```text
  to-read: 2
  reading: 1
  done: 3
  finished this year: 2
  ```

- [ ] Aparecen todos los estados, aunque su cuenta sea 0. Una estantería vacía muestra las cuatro líneas con ceros.
- [ ] `finished this year` cuenta los libros con estado `done` cuyo `finished_at` cae en el año natural en curso, en UTC (la zona horaria de las marcas de tiempo guardadas).
- [ ] Los tests no dependen de la fecha de hoy: un libro terminado el año pasado no cuenta, sea cual sea el año en que se ejecuten. Por ejemplo, un test puede escribir el archivo de la estantería con marcas de tiempo elegidas, o el comando puede recibir la fecha actual como parámetro.
- [ ] El archivo de la estantería no se modifica.
- [ ] `python -m unittest` pasa, con tests nuevos para las cuentas, la estantería vacía y el cambio de año.

### Archivos que probablemente cambian

- `shelf/commands/stats.py` (nuevo)
- `tests/test_stats.py` (nuevo)

`shelf finish` ya guarda `finished_at`, así que no hace falta cambiar ningún otro archivo.

### Fuera de alcance

- Estadísticas por autor o etiqueta, velocidad de lectura, gráficos, elegir otro año.

**Seguridad en paralelo:** Independiente. Solo añade archivos nuevos.

## S4: Exportar la estantería a CSV o Markdown

**Título:** `S4: Exportar la estantería a CSV o Markdown`

### Problema

Tu lista de lectura está encerrada en un archivo JSON. Quieres pegarla en una hoja de cálculo o en un documento Markdown.

### Criterios de aceptación

- [ ] `shelf export --format csv` escribe CSV en stdout: una fila de cabecera `id,title,author,status,added_at,finished_at` y después una fila por libro, ordenadas por id. Si falta `finished_at`, la celda queda vacía.
- [ ] Los títulos y autores con comas, comillas o saltos de línea sobreviven: al leer la salida con `csv.reader` de Python se recuperan los valores originales.
- [ ] `shelf export --format markdown` escribe una tabla Markdown con las columnas `ID`, `Title`, `Author` y `Status`, ordenada por id. Un `|` dentro de un título o autor se escribe como `\|`, para que la tabla no se rompa.
- [ ] `--format` es obligatorio y solo acepta `csv` y `markdown`. Cualquier otro valor termina con código 2.
- [ ] Con la estantería vacía, CSV escribe solo la fila de cabecera, y Markdown solo la fila de cabecera y la fila separadora.
- [ ] El comando solo escribe en stdout. El archivo de la estantería no se modifica.
- [ ] `python -m unittest` pasa, con tests nuevos para los dos formatos, los caracteres problemáticos y la estantería vacía.

### Archivos que probablemente cambian

- `shelf/commands/export.py` (nuevo)
- `tests/test_export.py` (nuevo)

### Fuera de alcance

- Escribir en un archivo. Eso ya lo hace la shell: `shelf export --format csv > ~/shelf.csv`.
- Exportar a JSON, importar, exportar etiquetas.

**Seguridad en paralelo:** Independiente. Solo añade archivos nuevos.

## S5: Eliminar un libro, con confirmación

**Título:** `S5: Eliminar un libro, con confirmación`

### Problema

Un libro añadido por error se queda en la estantería para siempre. Eliminar es destructivo, así que tiene que ser difícil hacerlo sin querer.

### Criterios de aceptación

- [ ] `shelf remove ID --yes` elimina el libro, escribe `Removed` seguido de la línea del libro (por ejemplo `Removed #3 [to-read] Dune by Frank Herbert`) y termina con código 0.
- [ ] `shelf remove ID` sin `--yes` no elimina nada. Escribe `Would remove #3 [to-read] Dune by Frank Herbert. Run again with --yes to confirm.` en stderr y termina con código 1.
- [ ] Un id desconocido escribe `shelf: error: no book with id 42` en stderr y termina con código 1, con o sin `--yes`. El archivo de la estantería no se modifica.
- [ ] Los demás libros conservan sus ids.
- [ ] `python -m unittest` pasa, con un test que demuestra que el libro sigue ahí después de `shelf remove ID` sin `--yes`.

### Archivos que probablemente cambian

- `shelf/commands/remove.py` (nuevo)
- `shelf/store.py` (un método `remove` junto a `move`)
- `tests/test_remove.py` (nuevo)

### Fuera de alcance

- Preguntas interactivas como `Are you sure? [y/N]`, deshacer, eliminar varios libros a la vez.
- La reutilización de ids. Un id nuevo es el id más alto más uno, así que si eliminas el libro más reciente, el siguiente `shelf add` reutiliza su id. En esta issue es aceptable: arreglarlo exige guardar un contador, y eso cambia el formato del archivo.

**Seguridad en paralelo:** Independiente. Añade un método a `shelf/store.py`, que C1 y C2 también cambian, pero en otra parte del archivo, así que git hace el merge sin conflictos.

## S6: Rechazar títulos vacíos y estados desconocidos

**Título:** `S6: Rechazar títulos vacíos y estados desconocidos`

### Problema

`shelf add` lo acepta todo. `shelf add "" "Frank Herbert"` guarda un libro sin título, y `shelf add "Dune" "Frank Herbert" --status finished` guarda un estado que ningún otro comando entiende. Los datos malos entran en el archivo sin avisar.

### Criterios de aceptación

- [ ] `shelf add` con un título vacío o formado solo por espacios termina con código 2, escribe en stderr un error que dice que el título no puede estar vacío y no guarda nada.
- [ ] `shelf add` con un `--status` distinto de `to-read`, `reading` o `done` termina con código 2, escribe en stderr un error que enumera los estados válidos y no guarda nada.
- [ ] Los dos errores usan el mismo formato que el resto de errores de uso: la línea `usage: shelf add …` y después `shelf add: error: …`.
- [ ] «No guarda nada» está probado con un test: si el archivo de la estantería no existía antes del comando, sigue sin existir después.
- [ ] Una entrada válida funciona exactamente igual que antes.
- [ ] `python -m unittest` pasa, con tests nuevos para los dos errores.

### Archivos que probablemente cambian

- `shelf/commands/add.py` (valida en la frontera de la línea de comandos; no cambies `shelf/models.py` ni `shelf/store.py`)
- `tests/test_cli.py`, en la clase `AddCommandTest`

### Fuera de alcance

- Validar libros que ya están en el archivo de la estantería.
- Quitar espacios de los títulos, validar autores.

**Seguridad en paralelo:** Independiente de S1–S5 y de C2, porque no toca el modelo ni el almacenamiento. C1 también cambia `shelf add` (añade `--tag`), así que S6 y C1 editan líneas vecinas de `shelf/commands/add.py`: un pequeño solapamiento textual. Haz primero el merge de S6.

## C1: Etiquetar libros

**Título:** `C1: Etiquetar libros`

### Problema

El estado dice en qué punto de tu lectura está un libro, no de qué trata. Quieres agrupar libros por tema (`sci-fi`, `work`, `book-club`) y listar un grupo.

### Criterios de aceptación

- [ ] `shelf add TITLE AUTHOR --tag sci-fi --tag classics` guarda las etiquetas. `--tag` es opcional y se puede repetir.
- [ ] Las etiquetas se guardan en minúsculas, sin espacios alrededor y sin duplicados, en el orden en que aparecen por primera vez: `--tag Sci-Fi --tag " sci-fi "` guarda `["sci-fi"]`.
- [ ] `shelf list` muestra las etiquetas de un libro después del autor, entre paréntesis: `#1 [to-read] Dune by Frank Herbert (sci-fi, classics)`. Los libros sin etiquetas se ven exactamente igual que antes.
- [ ] `shelf list --tag sci-fi` muestra solo los libros con esa etiqueta, sin distinguir mayúsculas. Si `shelf list --status` (S1) ya existe cuando empiezas, los dos filtros se combinan: un libro tiene que cumplir ambos.
- [ ] Cada libro del archivo de la estantería guarda sus etiquetas como una lista de cadenas.
- [ ] Los archivos escritos antes de este cambio, sin etiquetas, se siguen cargando. Sus libros no tienen etiquetas.
- [ ] `python -m unittest` pasa, incluido el test de `tests/test_store.py` que fija los campos guardados de un libro, actualizado con `tags`.

### Archivos que probablemente cambian

- `shelf/models.py` (un campo `tags` y las etiquetas en la línea del libro)
- `shelf/store.py` (`Store.add` acepta etiquetas)
- `shelf/commands/add.py` y `shelf/commands/list_books.py`
- `tests/test_store.py` y `tests/test_cli.py`

### Fuera de alcance

- Etiquetar libros que ya están en la estantería, renombrar o eliminar etiquetas.
- Etiquetas en `shelf export` o `shelf search`.

**Seguridad en paralelo:** En conflicto con C2. Las dos cambian cómo se guarda un libro en el archivo, las dos editan `shelf/models.py` y `shelf/store.py`, y las dos tienen que cambiar el test del formato guardado en `tests/test_store.py`. Ejecútalas en paralelo y decide el orden de merge antes de que empiece ninguna: la que haga merge en segundo lugar hace merge de `origin/main` en su rama y se adapta. C1 también tiene pequeños solapamientos textuales con S1 (`shelf list`) y S6 (`shelf add`).

## C2: Versionar el formato del archivo de la estantería

**Título:** `C2: Versionar el formato del archivo de la estantería`

### Problema

El archivo de la estantería es una lista JSON sin versión. La primera vez que cambie el formato, el programa no podrá distinguir un archivo antiguo de uno nuevo, y una copia antigua de `shelf` podría leer mal o sobrescribir un archivo más nuevo sin darse cuenta.

### Criterios de aceptación

- [ ] Cada guardado escribe un objeto JSON, `{"version": 2, "books": [...]}`, donde `books` contiene los mismos objetos de libro que el archivo contiene hoy.
- [ ] Un archivo de la versión 1 (una lista JSON sin envolver) se sigue cargando. Leerlo no lo reescribe: después de `shelf list`, el archivo no ha cambiado ni un byte. El siguiente comando que guarda escribe la versión 2.
- [ ] Un archivo con una versión que este programa no conoce, como `{"version": 99, "books": []}`, hace que cualquier comando termine con código 1 y escriba `shelf: error: unsupported shelf file version 99` en stderr. El archivo no se modifica.
- [ ] La versión actual es una única constante con nombre, `SCHEMA_VERSION`, definida en `shelf/models.py` junto a `Book`, para que quien cambie los campos de un libro la vea.
- [ ] Un test fija los campos guardados de un libro para cada versión del esquema. Añadir o quitar un campo de `Book` sin subir `SCHEMA_VERSION` hace fallar la suite.
- [ ] Un test carga un archivo de ejemplo (fixture) de la versión 1, escrito exactamente como lo escribe el programa actual, lo guarda y comprueba que el resultado es la versión 2 con los mismos libros.
- [ ] `python -m unittest` pasa.

### Archivos que probablemente cambian

- `shelf/store.py` (`Store.load`, `Store.save`, la migración desde la versión 1 y un error para versiones desconocidas basado en `ShelfError`)
- `shelf/models.py` (`SCHEMA_VERSION`)
- `tests/test_store.py` y un fixture de la versión 1 dentro de `tests/`

### Fuera de alcance

- Copias de seguridad de archivos antiguos, un comando `shelf migrate`, volver un archivo a la versión 1.

**Seguridad en paralelo:** En conflicto con C1. Las dos editan `shelf/models.py`, `shelf/store.py` y el test del formato guardado en `tests/test_store.py`, y quien haga merge en segundo lugar tiene que decidir si las etiquetas forman parte de la versión 2.

## S7: Hacer shelf más útil para clubes de lectura

**Título:** `S7: Hacer shelf más útil para clubes de lectura`

### Problema

«Nuestro club de lectura ha empezado a usar shelf. Hazlo más útil para clubes de lectura.»

Esa es toda la petición. Esta issue es vaga a propósito: todavía no escribas código para ella.

### Criterios de aceptación

- [ ] Un comentario en esta issue enumera las preguntas que hay que responder antes de construir. Por ejemplo: ¿quién lo usa, quien organiza el club o cada miembro? ¿Una estantería compartida o una por persona? ¿Necesita red, teniendo en cuenta que `shelf` solo usa la biblioteca estándar? ¿Cómo sería «más útil» dentro de un mes?
- [ ] El mismo comentario propone dos o tres opciones. Cada opción dice qué problema resuelve, qué comandos añadiría, qué archivos tocaría y si cambia el formato del archivo de la estantería.
- [ ] Una persona elige una opción, o ninguna, y lo dice en un comentario.
- [ ] La opción elegida se registra como una o más issues nuevas, escritas como S1–S6 y enlazadas desde esta, y esta issue se cierra.

### Archivos que probablemente cambian

Se sabrá cuando alguien decida. Cualquier cosa que guarde datos nuevos (reuniones, votaciones, miembros) cambia el formato del archivo de la estantería.

### Fuera de alcance

- Cualquier cambio de código en esta issue.

**Seguridad en paralelo:** Vaga: conversar antes. No la metas en un lote en paralelo. Cuando se divida en issues concretas, compara cada una con C1 y C2, porque la mayoría de las ideas para clubes de lectura cambian el formato del archivo.

## Crear las issues de GitHub con tu agente

Esto lo pide el laboratorio 5. Abre una sesión de tu agente en tu propia copia de `shelf` (consulta la sección [Use it for the labs del README de shelf](../shelf/README.md#use-it-for-the-labs)), sustituye `PATH_TO_GUIDE` por la carpeta donde clonaste esta guía y pega:

```text
Lee PATH_TO_GUIDE/practice/issues/es.md. Describe nueve issues de práctica para el proyecto shelf de este repositorio: de S1 a S6, C1, C2 y S7.

Primero ejecuta `gh repo view` y dime en qué repositorio de GitHub vas a crear las issues. Espera a que te dé el OK.

Después crea una issue de GitHub por cada entrada con `gh issue create`:
- Título: el texto que sigue a "Título:", tal cual.
- Cuerpo: las secciones Problema, Criterios de aceptación, Archivos que probablemente cambian y Fuera de alcance, en Markdown. Deja fuera la línea "Seguridad en paralelo": decidir qué issues pueden ir en paralelo es un paso aparte.
- Escribe cada cuerpo en un archivo temporal y pásalo con --body-file, para que las comillas invertidas y las comillas sobrevivan a la shell.
- Sin etiquetas, sin asignar a nadie y sin milestones.

Cuando termines, ejecuta `gh issue list --state all` y enséñame una tabla con cada ID, su número de issue y su título, para comprobar que no falta ni sobra ninguna. No empieces a implementar ninguna issue.
```

En qué fijarte en la respuesta:

- Se detiene después de `gh repo view` y te espera. Si crea las issues antes, has aprendido algo sobre la configuración de permisos de tu agente.
- La tabla final tiene nueve filas, sin duplicados.
- Los cuerpos de las issues en GitHub no tienen la línea «Seguridad en paralelo».

> [!TIP]
> Para el laboratorio 0 o el 2 solo necesitas una o dos issues. Cambia «una issue de GitHub por cada entrada» por «una issue de GitHub para S1 y otra para S2», o pega directamente el texto de la issue en tu sesión.

## Solucionario: pistas y conflictos

Léelo después de hacer el laboratorio 5, o si facilitas un workshop.

<details>
<summary>Mostrar el solucionario</summary>

| Issue | Archivos principales | Se solapa con |
| --- | --- | --- |
| S1 | `commands/list_books.py` | C1 (textual) |
| S2 | nuevo `commands/search.py` | Ninguna |
| S3 | nuevo `commands/stats.py` | Ninguna |
| S4 | nuevo `commands/export.py` | Ninguna |
| S5 | nuevo `commands/remove.py`, `store.py` | Ninguna |
| S6 | `commands/add.py` | C1 (textual) |
| C1 | `models.py`, `store.py`, `commands/add.py`, `commands/list_books.py` | C2 (semántico), S1 y S6 (textual) |
| C2 | `models.py`, `store.py` | C1 (semántico) |
| S7 | Por decidir | Conversar antes |

Comprobamos esta tabla implementando de S1 a S6, C1 y C2 de forma mínima, cada una en su propia rama desde el mismo punto de partida, y haciendo merge de las ramas:

- De S1 a S6 se combinan sin conflictos y los tests pasan.
- S2, S3, S4 y S5 se combinan sin conflictos con C1 y con C2, por separado o juntas, y los tests pasan. S1 y S6 se combinan sin conflictos con C2.
- S1 con C1 se detiene en `shelf/commands/list_books.py`. S6 con C1 se detiene en `shelf/commands/add.py`.
- C1 con C2 se detiene en `tests/test_store.py`. Git combina `models.py` y `store.py` sin quejarse. Si resuelves el test quedándote con cualquiera de los dos lados, falla un test del formato guardado hasta que alguien decide qué contiene la versión 2.

También repetimos el orden de los laboratorios con squash merges. Primero llegaron a `main` S1 y S2 (laboratorio 0), S3 (laboratorio 2) y S6 (laboratorio 3). Después S4, S5, C1 y C2 salieron cada una en su rama desde ese `main`. S4 y S5 hicieron merge sin conflictos, igual que la primera de C1 y C2. La otra, al hacer merge de `origin/main` en su rama, se detuvo solo en `tests/test_store.py`, en cualquiera de los dos órdenes, con el mismo fallo del formato guardado hasta que aplicamos la decisión.

La implementación de tu agente será distinta de la nuestra, así que toma estos resultados como probables, no como garantizados.

Una forma de repartir el trabajo en tres pistas para el laboratorio 6, cuando los laboratorios 0, 2 y 3 ya han integrado S1, S2, S3 y S6:

1. **Pista A:** S4 y S5, una detrás de otra. S4 añade un comando nuevo, y S5 añade otro más un método `remove` en `shelf/store.py`.
2. **Pista B:** C1.
3. **Pista C:** C2.

Si S1, S2, S3 o S6 siguen abiertas porque te saltaste algún laboratorio, añádelas a la pista A.

Las tres pueden ejecutarse a la vez. Haz primero el merge de la pista A. Después hay dos formas razonables de integrar C1 y C2, y el laboratorio 4 registra la elección como `D-0001`:

- **Primero C1.** C2 hace merge de `origin/main` en su rama y se adapta: la versión 2 incluye `tags` y la migración desde la versión 1 da a los libros antiguos una lista de etiquetas vacía. Una sola versión, menos código.
- **Primero C2.** C1 hace merge de `origin/main` y se adapta. Añadir `tags` cambia ahora un formato versionado, así que C1 sube `SCHEMA_VERSION` a 3 y añade una migración desde la versión 2. Más código, pero es lo que hace un proyecto real cuando la versión 2 ya se ha publicado.

Ninguna es incorrecta. Elegir es una decisión humana, y tomarla a conciencia es el objetivo del ejercicio.

</details>
