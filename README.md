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
