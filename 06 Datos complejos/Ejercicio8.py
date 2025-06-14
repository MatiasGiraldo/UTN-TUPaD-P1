Stock = {
    'llave': 8,
    'clavo': 60,
    'tornillo': 70,
    'destornillador': 14
}

producto = input("Ingrese nombre del producto: ")
if producto in Stock:
    print(f"El stock de la llave es: {Stock[producto]}")    
    stock_producto = int(input("Agregue unidades al stock del producto: "))
    Stock[producto] = stock_producto + Stock[producto]
else:
    print(f"{producto} es un nuevo producto")
    producto_nuevo = producto
    Stock[producto_nuevo] = int(input("Ingrese el stock del nuevo producto: "))

print(Stock)
