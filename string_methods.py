def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
    Linea 2
    Linea 3"""

    print(nombre.strip())
    print(nombre.lstrip())
    print(nombre.rstrip())
    print(f"Mayúsculas: {nombre.upper()}")
    print(f"Minúsculas: {nombre.lower()}")
    print(f"Título: {nombre.title()}")
    print(f"Posición de Python: {frase.find('Python')}")
    print(f"Cantidad de letras a: {frase.count('a')}")
    print(f"¿Dice gran?: {'gran' in frase}")
    print(f"Frase nueva: {frase.replace('gran', 'bueno')}")
    print(f"Slicing paso 2: {frase[0:10:2]}")
    print(f"Nombre al revés: {nombre[::-1]}")
    print("Texto con varias líneas:")
    print(multilinea)
