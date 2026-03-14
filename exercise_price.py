def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
    """
    precio_base = 100
    precio_impuesto = precio_base * 0.21
    precio_subtotal = precio_impuesto + precio_base
    monto_propina = precio_subtotal * 0.10
    precio_final = precio_subtotal + monto_propina

    print(precio_impuesto)
    print(precio_subtotal)
    print(monto_propina)
    print(precio_final)
