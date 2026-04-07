def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    gasto= float(input("ingrese un gasto: "))
    recibido= float(input("ingrese el dinero recibido: "))
    vuelto= recibido-gasto
    pesos = int(vuelto)
    centavos = round((vuelto - pesos) * 100)
    
    print("Vuelto total:", vuelto)
    print("Pesos:", pesos)
    print("Centavos:", centavos)
