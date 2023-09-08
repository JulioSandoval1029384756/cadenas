frase = input("Por favor, introduce una frase: ")

vocal = input("Ahora, introduce una vocal: ")

if vocal in "aeiouAEIOU":

    frase_con_vocal_mayuscula = frase.replace(vocal, vocal.upper())
    print("Frase con la vocal en mayúscula:", frase_con_vocal_mayuscula)
else:
    print("Lo que ingresaste no es una vocal.")
