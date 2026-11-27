# Issues de práctica para `shelf`

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
