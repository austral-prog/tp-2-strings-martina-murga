def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"
    longitud = len(palabra)
    primera = palabra[0]
    ultima = palabra[-1]
    decorada = f"***{palabra * 3}***"
    print(f"Longitud: {longitud}")
    print(f"Primera letra: {primera}")
    print(f"Última letra: {ultima}")
    print(decorada)
