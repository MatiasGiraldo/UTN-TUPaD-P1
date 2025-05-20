def suma_digitos(num):
    if num < 10:
        return num
    else:
        return (num % 10) + suma_digitos(num // 10)
    
num= int(input("Ingrese numero: "))
if num > 0:
    print(suma_digitos(num))
else:
    print("ERROR, ha ingresado un numero negativo")