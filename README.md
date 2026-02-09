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

## Exercise index

### 01_tipos_datos_basicos
- ej01_operaciones_basicas.py
- ej02_celsius_fahrenheit.py
- ej03_area_perimetro_rectangulo.py
- ej04_media_tres_notas.py
- ej05_intercambiar_variables.py
- ej06_segundos_a_hms.py
- ej07_calcular_iva.py
- ej08_euros_centimos.py

### 02_estructuras_alternativas
- ej01_suma_signo.py
- ej02_par_impar.py
- ej03_dias_del_mes.py
- ej04_login_simple.py
- ej05_bisiesto.py
- ej06_mayuscula.py
- ej07_mayor_de_tres.py
- ej08_calculadora_simple.py

### 03_bucles
- ej01_mostrar_1_a_n.py
- ej02_tabla_multiplicar.py
- ej03_suma_1_a_n.py
- ej04_factorial.py
- ej05_contar_signos.py
- ej06_hasta_cero.py
- ej07_primo.py
- ej08_adivina_numero.py

### 04_secuencias
- ej01_contar_vocales.py
- ej02_invertir_cadena.py
- ej03_palindromo.py
- ej04_contar_palabras.py
- ej05_max_min_media_lista.py
- ej06_buscar_en_lista.py
- ej07_eliminar_duplicados.py
- ej08_tupla_persona.py

### 05_diccionarios
- ej01_agenda_basica.py
- ej02_frecuencia_letras.py
- ej03_frecuencia_palabras.py
- ej04_notas_alumnos.py
- ej05_inventario_simple.py
- ej06_traducciones.py
- ej07_frecuencia_numeros.py
- ej08_mostrar_ordenado.py

### 06_excepciones
- ej01_pedir_entero_valido.py
- ej02_division_segura.py
- ej03_pedir_float_valido.py
- ej04_menu_validado.py

### 07_modulos
- ej01_math_circulo.py
- ej02_random_dado.py
- ej03_datetime_dia_semana.py
- ej04_pathlib_contar_archivos.py

### 08_poo
- ej01_persona.py
- ej02_cuenta_bancaria.py
- ej03_rectangulo_clase.py
- ej04_animales_herencia.py

