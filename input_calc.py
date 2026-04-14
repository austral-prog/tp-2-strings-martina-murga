def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    base = input("Ingrese la base: ")
    altura = input("Ingrese la altura: ")
    base = float(base)
    altura = float(altura)
    area = base * altura
    perimetro = 2 * (base + altura)
    print(f"Base: {base}")
    print(f"Altura: {altura}")
    print(f"Área: {area}")
    print(f"Perímetro: {perimetro}")
rectangle()
