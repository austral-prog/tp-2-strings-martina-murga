def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    gasto = float(input("Ingresar gasto: "))
    recibido = float(input("Dinero recibido: "))
    vuelto_total = recibido - gasto
    pesos = int(vuelto_total)
    centavos = round((vuelto_total - pesos) * 100)
    print("Vuelto")
    print(f"Pesos: {pesos}")
    print(f"Centavos: {centavos}")
