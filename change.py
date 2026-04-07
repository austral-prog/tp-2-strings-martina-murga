def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    gasto= float(input("gasto: "))
    recibido= float(input("dinero recibido: "))
    vuelto= recibido-gasto
    pesos = int(vuelto)
    centavos = (vuelto - pesos) * 100
    
    print(vuelto)
    print(pesos)
    print(centavos)
