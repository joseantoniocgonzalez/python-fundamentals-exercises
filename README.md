# Python Fundamentals Exercises

Practice repository for building a solid Python 3 foundation through short exercises based on a structured syllabus.

## Topics covered
- Basic data types (numbers, booleans), variables, input/output
- Strings
- Control flow (if/elif/else)
- Loops (while, for) + counters, accumulators, flags
- Lists and tuples
- Dictionaries
- Exceptions
- Modules (basics)
- Structured programming with functions (including recursion)
- Object-Oriented Programming (encapsulation, inheritance, delegation)

## Project structure
src/
  01_tipos_datos_basicos/
  02_estructuras_control/
  03_secuencias_strings_listas_tuplas/
  04_diccionarios/
  05_excepciones/
  06_modulos/
  07_funciones_programacion_estructurada/
  08_poo/
tests/

## How to run
1) Create and activate a virtual environment:
   - python3 -m venv .venv
   - source .venv/bin/activate

2) Install dev dependencies:
   - pip install -r requirements-dev.txt

3) Run tests (if present):
   - pytest -q

4) Lint (optional):
   - ruff check .

## Naming conventions
- Exercises live in src/<section>/ as:
  - ex_001_short_name.py
- Optional statement file next to it:
  - ex_001_short_name.md

## Notes
This is a learning/practice repo. Exercises and tests are added progressively.

## Run an exercise
From the repository root:

- Example:
  - python3 src/02_estructuras_alternativas/ej02_par_impar.py

Each exercise is a standalone script that uses standard input/output (input/print).

## Structure (folders)
All exercises are standalone scripts (style: input/print).

- src/01_tipos_datos_basicos
  - Numeric/boolean types, variables, basic I/O, simple calculations.
- src/02_estructuras_alternativas
  - if/elif/else exercises (conditions).
- src/03_bucles
  - for/while loops, counters and accumulators.
- src/04_secuencias
  - Strings + lists + tuples exercises.
- src/05_diccionarios
  - Dictionaries (maps) exercises.

## Quick run examples
Run any exercise from the repository root:

- Basics:
  - python3 src/01_tipos_datos_basicos/ej01_operaciones_basicas.py
- Conditionals:
  - python3 src/02_estructuras_alternativas/ej02_par_impar.py
- Loops:
  - python3 src/03_bucles/ej08_adivina_numero.py
- Sequences:
  - python3 src/04_secuencias/ej03_palindromo.py
- Dictionaries:
  - python3 src/05_diccionarios/ej05_inventario_simple.py
