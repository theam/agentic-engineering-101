---
title: "Laboratorio 6 — Tres pistas a la vez"
module: 6
kind: lab
minutes: 90
level: intermediate
last_reviewed: 2026-09-17
---

# Laboratorio 6 — Tres pistas a la vez

## Objetivo

Ejecuta a la vez las tres pistas de trabajo (tracks) que planificaste en el [laboratorio 5](../05-decompose-into-tracks/lab.md), cada una en su propio worktree y con sus propios datos. Atiende las sesiones por turnos a medida que te necesiten, haz merge en el orden planificado y resuelve el conflicto entre C1 y C2 aplicando la decisión que ya tomaste.

Por el camino, lleva un registro de atención. El código es del proyecto de práctica; el registro va sobre ti.

## Antes de empezar

- **Laboratorio 5 terminado:** las issues existen, `kb/tracks.md` recoge tu orden de merge entre C1 y C2 según `D-0001` (la decisión que registraste en el [laboratorio 4](../04-context-is-infrastructure/lab.md)), y `kb/kickoffs/` contiene `a.md`, `c1.md` y `c2.md`, subidos a `main`. Si te saltaste el laboratorio 5, usa el solucionario del final del [catálogo de issues](../../../practice/issues/es.md) y escribe tres prompts de arranque cortos con, como mínimo, un objetivo, el orden de merge, la decisión sobre la versión 2 y un «terminado cuando». Si también te saltaste el laboratorio 4, toma ahora esa decisión y escríbela.
- **Si te saltaste laboratorios anteriores,** cualquiera de S1, S2, S3 o S6 que siga abierta va en la pista A, que hace merge primero, como explica el paso 5 del [laboratorio 5](../05-decompose-into-tracks/lab.md).
- **Tu repositorio** está al día en `main`: `git fetch origin && git status`. Los comandos de abajo suponen que está en `~/code/shelf`; ajústalos si lo tienes en otro sitio.
- **Espacio en pantalla para seis paneles:** un agente y una terminal normal por pista. Sirven los paneles divididos de tu terminal, tmux o una terminal que entienda de agentes (consulta el [módulo 06](README.md#gestionar-muchas-sesiones)).
- **Notificaciones activadas** en tu agente o en tu terminal, para que te avise una sesión que termina o necesita algo.
- **Un registro de atención** fuera del repositorio, por ejemplo `~/lab6-log.md`.
- **Unos 90 minutos.** La mayor parte es tiempo de los agentes. Tu trabajo son las decisiones.

**En tu propio repositorio:** elige tres pistas de tu propia descomposición, con al menos una pareja que tenga un orden de merge planificado. En lugar de `SHELF_PATH`, da a cada worktree su propio puerto y su propia base de datos (consulta el [módulo 06](README.md#aislar-recursos-no-solo-archivos)).

## Pasos

### 1. Escribe el orden de merge al principio del registro (2 minutos)

```text
Orden de merge: A (S4, luego S5)  ->  C1  ->  C2   (o C2 antes que C1: sigue D-0001)
Decisión (D-0001): <la versión 2 incluye etiquetas | C1 sube a la versión 3>
Registro: hora | sesión | qué necesitaba | mis minutos | ¿lo habría evitado el prompt?
```

Coloca las sesiones en pantalla en el mismo orden: arriba, la pista que hace merge primero.

**Punto de control:** el orden de tu registro coincide con `kb/tracks.md` y con `D-0001`.

### 2. Crea tres worktrees (5 minutos)

Desde tu repositorio:

```bash
cd ~/code/shelf
git fetch origin
git worktree add --no-track -b s4-export ../shelf-a origin/main
git worktree add --no-track -b c1-tags ../shelf-c1 origin/main
git worktree add --no-track -b c2-file-version ../shelf-c2 origin/main
git worktree list
```

Usa el nombre de rama de la *primera* issue de la pista A (aquí, S4). La sesión creará más tarde la rama de su segunda issue.

**Punto de control:** `git worktree list` muestra cuatro entradas, cada una en su rama, y `git -C ../shelf-c1 status -sb` imprime `## c1-tags` sin ningún upstream detrás.

### 3. Da a cada pista sus propios datos (5 minutos)

Los tests ya usan archivos temporales. Las ejecuciones a mano no, así que da a cada pista su propio archivo de estantería. En la **terminal normal** de cada pista:

```bash
mkdir -p ~/shelf-lab-data
cd ~/code/shelf-c1                               # ../shelf-a y ../shelf-c2 en las otras
export SHELF_PATH=~/shelf-lab-data/c1.json       # a.json y c2.json en las otras
python -m unittest
```

Ahora demuestra el aislamiento. En la terminal de C1 ejecuta `python -m shelf add "Dune" "Frank Herbert"`. En la de C2 ejecuta `python -m shelf list`.

**Punto de control:** la terminal de C2 imprime `Your shelf is empty. Add a book with: shelf add TITLE AUTHOR`, y los tests pasan en los tres worktrees.

### 4. Arranca las sesiones (10 minutos)

En el **panel del agente** de cada pista, arranca el agente desde el worktree con la misma variable y ponle a la sesión el nombre de la pista:

```bash
cd ~/code/shelf-c1
export SHELF_PATH=~/shelf-lab-data/c1.json
claude -n c1-tags        # o bien: codex
```

Pega el prompt de arranque de la pista (`kb/kickoffs/c1.md` también está en el worktree, porque lo subiste antes de crear los worktrees). Añade esto al final:

```text
Antes de cambiar nada, dime en cinco puntos qué harás primero y qué archivos
vas a tocar. Después espera a que te dé el visto bueno.
```

Para la pista A, añade también:

```text
Cuando esté abierto el PR de la primera issue, empieza la segunda en una rama
nueva, desde un main actualizado, en este mismo worktree:
git fetch origin && git switch --no-track -c <rama> origin/main
```

**Fíjate en:** en cada plan de cinco puntos, archivos que son de otra pista. Si el plan de C2 menciona `shelf/commands/add.py`, o el de la pista A menciona `models.py`, para y corrígelo antes de dar el visto bueno.

**Punto de control:** tres sesiones con nombre, cada una esperando con su plan. Apunta en tu registro el nombre o el ID de cada sesión.

### 5. Atiende por turnos (entre 30 y 50 minutos)

Da el visto bueno a los planes de arriba abajo. Después sigue estas reglas hasta que todas las pistas hayan informado de un PR:

1. **No te quedes mirando la salida.** Si nada te necesita, relee el siguiente prompt de arranque, prepara las comprobaciones del merge o no hagas nada.
2. **Cuando llegue una notificación,** termina la decisión que estás tomando y ve a la sesión en espera *más alta*, no a la última que ha sonado.
3. **Anota cada interacción** en una línea:

   ```text
   10:42 | c2 | pregunta si una versión desconocida sale con 1 o con 2 | 1 min | sí: la issue dice 1, el prompt no lo señalaba
   ```

4. **Decide en una frase, y que dure.** Si una sesión pregunta algo que ni la issue ni el prompt resuelven, responde y añade la respuesta al archivo del prompt de arranque de esa pista, para que una sesión reiniciada la conozca.
5. **Cada sesión en su carril.** Ninguna sesión para procesos que no arrancó, edita el worktree de otra pista o hace push a `main`.

**Fíjate en:** sesiones que informan con la URL del PR, los comandos que ejecutaron y cualquier cosa que tuvieron que decidir. Una sesión que dice «terminado» sin salida de tests no ha terminado.

**Punto de control:** `gh pr list` muestra un PR abierto por cada issue de las tres pistas, y tu registro tiene una entrada por cada interacción.

### 6. Haz merge de la pista A (5 minutos)

La revisión completa es el [laboratorio 7](../07-agents-review-agents/lab.md). Antes de hacer merge aquí, haz lo mínimo en la terminal normal de la pista A, para cada PR:

```bash
gh pr diff <número> --name-only
python -m unittest
```

**Fíjate en:** solo archivos que son de la pista A (archivos nuevos en `shelf/commands/` y en `tests/`, más `shelf/store.py` por el método `remove` de S5). Cualquier otra cosa es una pregunta para la sesión antes de hacer merge.

```bash
gh pr merge <número> --squash
```

> [!TIP]
> **¿Vas a seguir con el laboratorio 7?** Revisa un PR de este laboratorio antes de que haga merge. El preferido es el PR de la segunda pista C: cuando llegues al paso 9, déjalo abierto, haz el laboratorio 7 sobre él y vuelve después para los pasos 9 y 10. Si además quieres practicar con el caso límite que S5 deja fuera de alcance (reutilizar un id tras eliminar el libro más reciente), deja abierto aquí también el PR de S5: mergea sin conflictos con C1 y C2, así que puede esperar. El orden de merge sigue valiendo para todo lo demás.

**Punto de control:** `gh pr view <número> --json state --jq .state` imprime `MERGED` para cada PR de la pista A, salvo el de S5 si lo dejaste abierto para el laboratorio 7.

### 7. Haz merge de la primera entre C1 y C2 (5 minutos)

Las mismas comprobaciones, en la terminal normal de esa pista: `gh pr diff <número> --name-only`, luego `python -m unittest` y luego `gh pr merge <número> --squash`. Después dile a la otra sesión:

```text
<C1 o C2> ya ha hecho merge en main.
```

No des más instrucciones todavía. El prompt de arranque ya dice qué hacer. Observa si lo hace.

**Punto de control:** el primer PR aparece como `MERGED`, y has anotado cuánto tardó la segunda sesión en empezar a adaptarse.

### 8. Resuelve el conflicto en la segunda pista (15 minutos)

Si la sesión no ha empezado sola, o se ha puesto a editar directamente, envíale esto:

```text
Haz merge de origin/main en tu rama. No hagas rebase ni force-push.
Antes de resolver ningún conflicto, explica cada uno: qué cambió cada lado y
qué dice nuestra decisión que debe quedar. Recuerda que git puede integrar un
archivo sin conflictos y dejarlo mal igualmente. Después resuelve, ejecuta
python -m unittest y enséñame los tests del formato guardado y su salida.
Haz push cuando pasen.
```

Hacemos merge de `origin/main` en la rama en lugar de rebase para que nadie tenga que hacer force-push. El force-push es uno de los comandos que el [módulo 03](../03-close-the-loop/README.md) mantiene lejos de los agentes, y el squash merge del final hace que el historial de la rama dé igual.

**Fíjate en:**

- Git se detiene en `tests/test_store.py`, mientras que `models.py` y `store.py` se integran «sin conflictos». La explicación debería decir por qué no basta con que se integren limpios.
- **Si C1 hizo merge primero:** la versión 2 incluye `tags`, y al cargar un archivo antiguo con una lista a secas cada libro recibe una lista de etiquetas vacía. Comprueba tú un caso límite: un archivo con lista a secas escrito *después* del merge de C1 ya contiene etiquetas. ¿Las conserva la migración?
- **Si C2 hizo merge primero:** C1 sube `SCHEMA_VERSION` a 3, añade una migración desde la versión 2, y el test de campos guardados fija las dos versiones.

**Punto de control:** `python -m unittest` pasa en el worktree, y `gh pr view <número> --json mergeable --jq .mergeable` imprime `MERGEABLE`. (Si imprime `UNKNOWN`, GitHub todavía lo está calculando; vuelve a ejecutarlo en unos segundos.)

### 9. Haz merge y comprueba `main` (5 minutos)

```bash
gh pr merge <número> --squash
cd ~/code/shelf
git pull
python -m unittest
git log --oneline -6
```

Después prueba el resultado a mano con un archivo nuevo:

```bash
export SHELF_PATH=~/shelf-lab-data/main.json
python -m shelf add "Dune" "Frank Herbert" --tag sci-fi
python -m shelf list
cat "$SHELF_PATH"
```

**Punto de control:** los tests pasan en `main`, `git log` muestra los merges en el orden planificado, `list` imprime `#1 [to-read] Dune by Frank Herbert (sci-fi)` y el archivo es un objeto JSON con una `version` y una lista `books` cuyo libro tiene `tags`.

### 10. Limpia (5 minutos)

Primero confirma qué se ha integrado: `gh pr list --state merged`. Después, desde tu checkout principal, elimina solo los worktrees cuyos PR hayan hecho merge:

```bash
git worktree remove ../shelf-a
git worktree remove ../shelf-c1
git worktree remove ../shelf-c2
git branch -D s4-export s5-remove c1-tags c2-file-version
git worktree prune
git worktree list
rm -rf ~/shelf-lab-data
```

Ajusta los nombres de rama a los que usaron tus pistas. Hace falta `-D` porque los squash merges dejan los commits de la rama fuera de `main`; es seguro cuando `gh` confirma que el PR hizo merge. Si dejaste un PR abierto para el laboratorio 7, conserva también su worktree y su rama. Si tienes un `kb/ACTIVE.md`, borra las filas de las pistas que ya se han entregado.

**Punto de control:** `git worktree list` solo muestra tu checkout principal, más cualquier worktree que hayas conservado a propósito.

## Cómo saber que has terminado

- [ ] `gh pr list --state merged` muestra los PR de las tres pistas (salvo los que hayas dejado abiertos para el laboratorio 7).
- [ ] `git log --oneline` en `main` muestra los merges en el orden que planificaste en el laboratorio 5.
- [ ] `python -m unittest` pasa en un `main` actualizado.
- [ ] Un archivo de estantería escrito por `main` tiene `version` y libros con `tags`; un test carga un archivo en el antiguo formato de lista a secas.
- [ ] `git worktree list` solo muestra tu checkout principal, más cualquier worktree que hayas conservado a propósito.
- [ ] Tu registro de atención tiene una línea por cada vez que una sesión te necesitó.

## Reflexiona

Usa tu registro para responder:

- ¿Cuántas veces te necesitó una sesión? ¿Cuántas habría evitado una issue o un prompt de arranque mejor? Actualiza ahora las plantillas de prompt, mientras lo recuerdas.
- ¿Qué es lo máximo que una sesión te esperó, y por qué? ¿Y lo máximo que *tú* esperaste sin nada que decidir?
- ¿El conflicto de git te mostró el problema real entre C1 y C2, o necesitaste la decisión? ¿Qué habría pasado si cada sesión hubiera decidido por su cuenta?
- ¿Te ayudaron las notificaciones o te interrumpieron? ¿Habría funcionado mejor el [consejo de Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey) de desactivarlas con tres sesiones? ¿Y con diez?
- ¿Tres era el número adecuado para ti hoy? ¿Qué tendría que cumplirse para llevar cinco?

## Para ir más allá

- **Prueba el modelo de una sola carpeta.** Elige dos issues pequeñas que sigan abiertas (S3 y S6 si te saltaste los laboratorios 2 y 3; si no, dos issues que hayan salido de conversar sobre S7, como en el «Para ir más allá» del laboratorio 5) e impleméntalas a la vez en un checkout compartido, con cada agente haciendo commit solo de los archivos que ha cambiado. Anota cada sorpresa y compáralo con las pistas en worktrees.
- **Usa un subagente.** Ejecuta la pista A como subagente en su propio worktree, lanzado desde una sesión de planificación, en lugar de darle una ventana propia. Compara lo que pudiste ver y reconducir.
- **Haz un traspaso a mitad de pista.** Para a mitad de camino la sesión que hace merge en segundo lugar, pídele que escriba un paquete de traspaso ([módulo 05](../05-decompose-into-tracks/README.md#paquetes-de-traspaso)) y termina la pista desde una sesión nueva que solo reciba el prompt de reanudación.
- **Prueba el otro orden de merge.** En una rama de pruebas, integra C1 y C2 en el orden contrario y compara cuánto código y cuántos tests produjo cada orden.
