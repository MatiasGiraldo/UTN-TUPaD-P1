nombre = input("Ingrese su nombre: ")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
opcion = int(input("Ingrese la opcion deseada: "))
if opcion == 1 :
    print(nombre.upper())
elif opcion == 2 :
    print(nombre.lower())
elif opcion == 3 :
    print(nombre.title())
else : 
    print("Ha ingresado una opción incorrecta, vuelva a intentarlo")
