numero_telefono = input("Por favor, ingresa el número de teléfono en formato +34-XXXXXXXXX-XX: ")

partes = numero_telefono.split("-")

if len(partes) == 3 and partes[0] == "+34" and len(partes[1]) == 9 and len(partes[2]) == 2:
    numero_principal = partes[1] 
    print("Número de teléfono sin prefijo ni extensión:", numero_principal)
else:
    print("El formato del número de teléfono no es válido.")
