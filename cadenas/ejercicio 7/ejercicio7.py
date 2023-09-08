correo_electronico = input("Por favor, introduce tu correo electrónico: ")

nombre_usuario, dominio = correo_electronico.split("@")

nuevo_correo = nombre_usuario + "@ceu.es"

print("Nuevo correo electrónico:", nuevo_correo)
