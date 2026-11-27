# Solucionario: pistas y conflictos

Compara el plan que escribiste en el laboratorio 05 con estos resultados. Para cada diferencia, comprueba los archivos implicados y explica si tu plan también funcionaría.

## Seguridad en paralelo por issue

- Un **solapamiento textual** significa que dos ramas editan las mismas líneas. Git se detiene y te pide que elijas. Resolverlo lleva un minuto y no exige ninguna decisión de producto.
- Un **conflicto semántico** significa que dos ramas cambian el mismo contrato, aquí el formato del archivo de la estantería. Git puede incluso hacer el merge sin quejarse, y el resultado seguir estando mal. Alguien tiene que tomar una decisión.

El [módulo 5](../../content/es/05-decompose-into-tracks/README.md) explica cómo aprovechar esto al dividir el trabajo en pistas.

- **S1.** Independiente de S2–S6 y de C2. C1 también cambia `shelf list` (añade `--tag`), así que S1 y C1 editan las mismas líneas de `shelf/commands/list_books.py`: un pequeño solapamiento textual. Haz primero el merge de S1.
- **S2.** Independiente. Solo añade archivos nuevos.
- **S3.** Independiente. Solo añade archivos nuevos.
- **S4.** Independiente. Solo añade archivos nuevos.
- **S5.** Independiente. Añade un método a `shelf/store.py`, que C1 y C2 también cambian, pero en otra parte del archivo, así que git hace el merge sin conflictos.
- **S6.** Independiente de S1–S5 y de C2, porque no toca el modelo ni el almacenamiento. C1 también cambia `shelf add` (añade `--tag`), así que S6 y C1 editan líneas vecinas de `shelf/commands/add.py`: un pequeño solapamiento textual. Haz primero el merge de S6.
- **C1.** En conflicto con C2. Las dos cambian cómo se guarda un libro en el archivo, las dos editan `shelf/models.py` y `shelf/store.py`, y las dos tienen que cambiar el test del formato guardado en `tests/test_store.py`. Ejecútalas en paralelo y decide el orden de merge antes de que empiece ninguna: la que haga merge en segundo lugar hace merge de `origin/main` en su rama y se adapta. C1 también tiene pequeños solapamientos textuales con S1 (`shelf list`) y S6 (`shelf add`).
- **C2.** En conflicto con C1. Las dos editan `shelf/models.py`, `shelf/store.py` y el test del formato guardado en `tests/test_store.py`, y quien haga merge en segundo lugar tiene que decidir si las etiquetas forman parte de la versión 2.
- **S7.** Vaga: conversar antes. No la metas en un lote en paralelo. Cuando se divida en issues concretas, compara cada una con C1 y C2, porque la mayoría de las ideas para clubes de lectura cambian el formato del archivo.

## Solapamientos comprobados

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

## Cómo usan los laboratorios este catálogo

| Laboratorio | Issues | Qué haces con ellas |
| --- | --- | --- |
| [Laboratorio 0: el juego completo](../../content/es/00-start-here/lab.md) | S1 | Un agente añade el filtro por estado. S2 y la revisión independiente son opcionales después del módulo 03. |
| [Laboratorio 2: un agente, bien usado](../../content/es/02-one-agent-done-well/lab.md) | S3 | Llevas una issue por el ciclo conversar → planificar → construir → verificar y apuntas cada corrección que haces. |
| [Laboratorio 3: cierra el ciclo](../../content/es/03-close-the-loop/lab.md) | S6 | Escribes primero los tests de S6, añades un hook Stop que ejecuta los tests y ves cómo devuelve a un agente a arreglar su implementación. |
| [Laboratorio 4: el contexto es infraestructura](../../content/es/04-context-is-infrastructure/lab.md) | C1, C2 | Sin código. Decides cuál de las dos hace merge primero y lo registras como la decisión `D-0001`. |
| [Laboratorio 5: descomponer en pistas](../../content/es/05-decompose-into-tracks/lab.md) | Todas | Creas en GitHub las issues que aún no existen, detectas los solapamientos y la pareja en conflicto, reutilizas `D-0001` para el orden de merge y escribes prompts de arranque para tres pistas: S4 y S5, C1, y C2. |
| [Laboratorio 6: sesiones en paralelo](../../content/es/06-run-sessions-in-parallel/lab.md) | S4, S5, C1, C2 | Ejecutas las tres pistas en tres worktrees, haces merge primero de S4 y S5, después de C1 y C2 en el orden que fija `D-0001`, y resuelves su conflicto. |
| [Laboratorio 7: agentes que revisan agentes](../../content/es/07-agents-review-agents/lab.md) | Un pull request del laboratorio 6, mejor el de C1 o el de C2 | Lo revisas con un revisor de contexto limpio y con un revisor de otro proveedor, y clasificas los hallazgos. |

Si te saltas un laboratorio, sus issues siguen abiertas. Los laboratorios 5 y 6 dicen dónde van.

S7 no tiene laboratorio propio. Úsala cuando quieras practicar cómo convertir una petición vaga en trabajo concreto. En el laboratorio 5, fíjate en si tu agente la planifica sin más o si primero hace preguntas. El [sprint en paralelo](../../workshops/es/README.md#el-sprint-en-paralelo) del día 2 del workshop intensivo se basa en ella: conversar sobre ella, dividirla en issues nuevas y ejecutarlas después en paralelo.
