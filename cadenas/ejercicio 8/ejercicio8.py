precio_str = input("Por favor, introduce el precio en euros (con dos decimales): ")

precio = float(precio_str)

euros = int(precio)
centimos = int((precio - euros) * 100)

print(f"El precio introducido es de {euros} euros y {centimos} céntimos.")
