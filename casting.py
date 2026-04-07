def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    gasto= float(input("ingrese un gasto: "))
    recibido= float(input("ingrese el dinero recibido: "))
    vuelto= recibido-gasto
    pesos = int(vuelto)
    centavos = round((vuelto - pesos) * 100)
    
    print("Vuelto total:", vuelto)
    print("Pesos:", pesos)
    print("Centavos:", centavos)
