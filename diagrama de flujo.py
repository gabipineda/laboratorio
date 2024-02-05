def verificar_mayor_de_edad(edad):
    if edad >= 18:
        return "La persona es mayor de edad"
    else:
        return "La persona es menor de edad"

edad = int(input("Por favor, ingresa tu edad: "))
resultado = verificar_mayor_de_edad(edad)
print(resultado)