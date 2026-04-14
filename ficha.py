def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    nombre = input("Nombre completo: ")
    email = input("Email: ")
    n1 = input("Nota 1: ")
    n2 = input("Nota 2: ")
    n3 = input("Nota 3: ")
    nombre = nombre.strip().title()
    email = email.lower()
    nombre_len = len(nombre)
    indice_espacio = nombre.find(" ")
    iniciales = nombre[0] + nombre[indice_espacio + 1]
    p_nombre = nombre[:indice_espacio].lower()
    p_apellido = nombre[indice_espacio + 1:].lower()
    usuario = f"{p_apellido}.{p_nombre}"
    tiene_arroba = "@" in email
    dominio = email[email.find("@") + 1:]
    nombre_guion = nombre.replace(" ", "_")
    cuenta_a = nombre.lower().count("a")
    codigo_secreto = nombre[::-1].upper()
    nota1 = int(n1)
    nota2 = int(n2)
    nota3 = int(n3)
    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    promedio_entero = suma // 3
    ficha_texto = f"""
    {"=" * 24}
     FICHA DE ALUMNO
    {"=" * 24}
    Nombre: {nombre} ({nombre_len} letras)
    Iniciales: {iniciales}
    Email: {email} (Válido: {tiene_arroba})
    Dominio: {dominio}
    Usuario: {usuario}
    Nombre ID: {nombre_guion}
    Letras 'a': {cuenta_a}
    Código Secreto: {codigo_secreto}
    Notas: {nota1}, {nota2}, {nota3}
    Suma total: {suma}
    Promedio: {promedio:.2f}
    Promedio Entero: {promedio_entero}
    {"=" * 24}
    """
    print(ficha_texto)
