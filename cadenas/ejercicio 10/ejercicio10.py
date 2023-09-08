cesta_de_compra = input("Por favor, introduce los productos de la cesta de compra separados por comas: ")

productos = cesta_de_compra.split(",")

print("Productos en la cesta de compra:")
for producto in productos:
    print(producto.strip())  
