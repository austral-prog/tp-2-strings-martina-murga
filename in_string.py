def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    nombre = input().lower()
    tiene_a = 'a' in nombre
    tiene_e = 'e' in nombre
    tiene_i = 'i' in nombre
    tiene_o = 'o' in nombre
    tiene_u = 'u' in nombre
    print(f"Contiene a: {tiene_a}")
    print(f"Contiene e: {tiene_e}")
    print(f"Contiene i: {tiene_i}")
    print(f"Contiene o: {tiene_o}")
    print(f"Contiene u: {tiene_u}")
