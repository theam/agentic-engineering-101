---
title: "Laboratorio 0 — El juego completo"
module: 0
kind: lab
minutes: 15
level: foundation
last_reviewed: 2026-11-27
---

# Laboratorio 0 — El juego completo

## Objetivo

Añade un filtro a Shelf, una pequeña aplicación de listas de lectura. Le pedirás el cambio a un agente, probarás el filtro con dos libros y abrirás un pull request en tu repositorio. Calcula unos 15 minutos para el ejercicio una vez que tengas listas las herramientas y el proyecto.

## Antes de empezar

Necesitas una terminal, Git, una cuenta de GitHub con la sesión iniciada en GitHub CLI, Python 3.10 o posterior y un agente de programación como Claude Code o Codex. Los comandos usan una shell compatible con Bash (Git Bash o WSL en Windows). Si en tu equipo Python 3 se ejecuta con `python`, usa ese comando en todo el laboratorio.

```sh
git --version
gh auth status
python3 --version
```

Abre tu agente habitual y comprueba que puedes iniciar sesión. Mantén activada la aprobación de comandos. Si GitHub CLI te pide que inicies sesión, ejecuta [`gh auth login`](https://cli.github.com/manual/gh_auth_login).

### Prepara tu repositorio de prácticas

Volverás a usar esta copia de Shelf en los siguientes laboratorios. Si ya creaste tu copia en GitHub, empieza en el paso 2. Si además la clonaste, abre su carpeta y pasa a **Comprueba la preparación**.

1. [Crear mi copia de Shelf](https://github.com/theam/shelf-starter/generate). Inicia sesión en GitHub, elige tu cuenta personal como propietaria y llama `shelf` al repositorio. Si vas a entregar en Academy, elige **Public** para que el equipo pueda abrir tu pull request. Pulsa **Create repository**. Tu copia ya tendrá el código inicial y los tests.
2. [Clona tu copia](https://cli.github.com/manual/gh_repo_clone) en tu ordenador. Si elegiste otro nombre para el repositorio, sustituye el primer `shelf` del comando de clonado por ese nombre. Conserva la carpeta local `~/code/shelf` para los siguientes laboratorios.

   ```sh
   mkdir -p ~/code
   gh repo clone shelf ~/code/shelf
   cd ~/code/shelf
   ```

### Comprueba la preparación

Desde la carpeta de Shelf, ejecuta:

```sh
gh repo view --json nameWithOwner --jq .nameWithOwner
python3 -m shelf --help
python3 -m unittest
```

**Ya puedes empezar** cuando el primer comando muestre tu cuenta de GitHub y el nombre de tu repositorio, Shelf enumere sus comandos y los tests terminen en `OK`. Puedes parar aquí y volver a esta carpeta otro día. [Consulta del repositorio con GitHub CLI](https://cli.github.com/manual/gh_repo_view)

## Pasos

### 1. Pídele un cambio pequeño a un agente

Abre tu agente en la carpeta de **Shelf**. Imagina que has añadido diez libros y quieres ver solo los que estás leyendo. Pega esta tarea del [catálogo de issues, S1](../../../practice/issues/es.md):

```text
Lee README.md, AGENTS.md y los tests. Abre una issue en mi repositorio de
Shelf con el título "S1: Filter shelf list by status". Trabaja en una rama nueva.
Añade --status a shelf list. Conserva el formato y el orden. Acepta to-read,
reading y done. Para un estado inválido, devuelve el código 2 e indica los
valores válidos por stderr. Si no hay coincidencias, muestra
"No books with status reading." (con el estado solicitado) y devuelve 0.
Mantén el comportamiento de shelf list sin filtro.
Añade tests y ejecuta la suite completa. Usa datos temporales para las
pruebas manuales. Enséñame los cambios y el resultado antes de hacer commit.
```

### 2. Prueba tú el cambio

En otra terminal, abre la **misma carpeta de Shelf**, en la rama del agente. Crea una lista temporal y compara las dos formas de listar los libros:

```sh
export SHELF_PATH="$(mktemp -d)/books.json"
python3 -m shelf add "Dune" "Frank Herbert"
python3 -m shelf add "Kindred" "Octavia E. Butler" --status reading
python3 -m shelf list
python3 -m shelf list --status reading
python3 -m unittest
```

La lista completa muestra los dos libros. El filtro debería mostrar solo `#2 [reading] Kindred by Octavia E. Butler` y los tests deberían terminar en `OK`. Si falla una comprobación, pásale la salida al agente y repítela después de la corrección.

### 3. Abre tu pull request

Lee el diff. Cuando el resultado sea el esperado, pídele al agente que haga commit, suba la rama y abra un pull request contra `main` **en tu repositorio de Shelf**. Pídele que incluya el resultado de los tests y enlace la issue que abrió. Abre la URL y comprueba el propietario, los archivos modificados y el resultado de los tests.

## Cómo saber que has terminado

- [ ] El filtro muestra solo el libro que marcaste como `reading` y pasan todos los tests.
- [ ] Puedes abrir el pull request de S1 en tu repositorio de Shelf.

**Con esto has terminado el laboratorio 00.** Si estás en Academy, pega la URL del pull request en **Link to your work** y envía la entrega. Conserva el repositorio para los siguientes laboratorios.

## Reflexiona

Guarda tres líneas para el [laboratorio 1](../01-from-chatbot-to-system/lab.md): qué le pediste al agente, qué comprobaste tú y en qué momento te quedaste esperando.

## Para ir más allá

**Opcional, después del módulo 03.** Prueba una segunda tarea del [catálogo de issues](../../../practice/issues/es.md), S2, que consiste en buscar libros por título o autor. Abre S2 como issue en tu repositorio de prácticas. Encárgasela a una segunda sesión en su propio [worktree de Git](../06-run-sessions-in-parallel/README.md). Pide a una sesión nueva que [revise un pull request](../07-agents-review-agents/README.md), contraste el cambio con su issue y ejecute los tests. Decide qué corregir, haz merge de los cambios que aceptes y retira los worktrees que hayas terminado de usar.

Empieza S2 desde la carpeta de Shelf. El segundo comando abre otra carpeta de trabajo con una rama nueva.

```sh
git fetch origin
git worktree add --no-track -b s2-search ../shelf-s2 origin/main
cd ../shelf-s2
```

Dale a la nueva sesión el número real de la issue S2. Pídele que muestre un test en el que buscar `GARCÍA` encuentre `García`, que ejecute la suite y que abra su propio pull request. Pásale la URL a la sesión que revisa y pregúntale: «¿Qué criterio de aceptación podría fallar todavía? Ejecuta los tests y enséñame la evidencia». Ante cada hallazgo, corrígelo, abre una issue para más adelante o anota por qué discrepas. Después de integrar S2 y guardar el trabajo que quieras conservar, vuelve a tu carpeta principal de Shelf y ejecuta `git worktree remove ../shelf-s2`.
