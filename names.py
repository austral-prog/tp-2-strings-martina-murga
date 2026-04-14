def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    nombre=input()
    apellido=input()
    nombre_completo=(f"{nombre} {apellido}")
    print(f"{nombre_completo.lower()}")
    print(f"{nombre_completo.title()}")
    print(f"{nombre_completo.upper()}")
    print(f"\t{nombre_completo.lower()}")
