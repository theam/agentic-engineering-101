# shelf

`shelf` is a tiny reading list for the command line. You add books, start them, finish them and list them.

It is the practice project for the labs of Agentic Engineering 101. It is small enough to understand in five minutes and big enough to split into parallel tracks of work.

- Python 3.10 or newer. Standard library only, so there is nothing to install.
- Your shelf is one JSON file.
- The tests use `unittest` and run in about a second.

## Try it

Run these from this folder (`practice/shelf`). Use `python3` instead of `python` if that is how Python 3 is called on your machine.

```sh
export SHELF_PATH=/tmp/practice-shelf.json   # keep practice data out of your real shelf
python -m shelf add "Dune" "Frank Herbert"
python -m shelf add "Kindred" "Octavia E. Butler" --status reading
python -m shelf start 1
python -m shelf finish 1
python -m shelf list
```

The last command prints:

```text
#1 [done] Dune by Frank Herbert
#2 [reading] Kindred by Octavia E. Butler
```

For the full list of commands and options, run:

```sh
python -m shelf --help
python -m shelf add --help
```

The help comes from the code, so it is always current. That is why this README does not list every command: adding a command should not require editing this file.

### Where your shelf is stored

In `~/.shelf.json`, unless the `SHELF_PATH` environment variable names another file.

### Exit codes

| Code | Meaning |
| --- | --- |
| `0` | The command worked. |
| `1` | The command failed, for example `shelf finish 42` when there is no book 42. The reason is printed to stderr as `shelf: error: …`. |
| `2` | Invalid usage, for example a missing argument. `argparse` prints the usage and the error to stderr. |

### Install the `shelf` command (optional)

You don't need to install anything to do the labs. If you want a `shelf` command on your path, install the project in a virtual environment:

```sh
python -m venv .venv
source .venv/bin/activate    # on Windows: .venv\Scripts\activate
pip install -e .
shelf --help
```

## Run the tests

From this folder:

```sh
python -m unittest
```

The output ends with `OK`. Add `-v` to see every test name.

The command-line tests run the real program (`python -m shelf`) in a subprocess. Each test points `SHELF_PATH` and `HOME` at its own temporary folder, so the tests never read or write your real `~/.shelf.json`.

## How the code is organized

```text
shelf/
  cli.py          parses arguments, runs the command, turns errors into exit codes
  commands/       one module per command, found automatically
  models.py       the Book dataclass and the valid statuses
  store.py        reads and writes the shelf file
tests/
  support.py      ShelfTestCase: a temporary shelf and a helper that runs the real CLI
  test_cli.py     one test class per command
  test_store.py   storage, including the exact shape of the file on disk
```

One module per command is deliberate. When two agents add two different commands, they add two different files, and their pull requests don't collide. [Module 5, "Decompose into tracks"](../../content/en/05-decompose-into-tracks/README.md), explains why that matters.

## Use it for the labs

Do the labs in a repository of your own, so you can open pull requests without touching this guide. Copy the project, turn it into a git repository and publish it with the [GitHub CLI](https://cli.github.com/):

```sh
# From the root of your copy of this guide
mkdir -p ~/code
cp -r practice/shelf ~/code/shelf
cd ~/code/shelf
git init -b main
git add .
git commit -m "Start from the Agentic Engineering 101 practice project"
gh repo create shelf --private --source=. --remote=origin --push
```

What the last command does:

- `gh repo create shelf` creates a repository called `shelf` in your GitHub account. Pick another name if you already have one called `shelf`.
- `--private` keeps it private. Use `--public` if you prefer.
- `--source=.` uses the current folder as the local repository, and `--remote=origin` adds the new repository as the `origin` remote.
- `--push` pushes your first commit.

If `gh` says you are not logged in, run `gh auth login` first.

The issues you will work on are in the [practice issue catalog](../issues/en.md). Lab 5 turns them into GitHub issues in your new repository.

## En español

`shelf` es una lista de lectura mínima para la línea de comandos y el proyecto de práctica de los laboratorios de Agentic Engineering 101. Solo necesita Python 3.10 o superior, sin dependencias.

- Pruébalo desde esta carpeta con `python -m shelf --help`.
- Tus libros se guardan en `~/.shelf.json`. Para usar otro archivo, define la variable de entorno `SHELF_PATH`.
- Ejecuta los tests desde esta carpeta con `python -m unittest`. Nunca tocan tu `~/.shelf.json` real.
- Para los laboratorios, copia el proyecto a un repositorio propio con los comandos de la sección [Use it for the labs](#use-it-for-the-labs).
- Las issues de práctica, en español, están en el [catálogo de issues](../issues/es.md).

El código, los mensajes del programa y los tests están en inglés.
