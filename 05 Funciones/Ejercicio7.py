def operaciones_basicas(a,b): 
    suma = a + b
    resta = a - b
    div = a / b # da decimales
    multi = a * b
    tupla = [suma, resta, div, multi]
    return tupla

num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))
tupla = operaciones_basicas(num1,num2)
print(f"El resultado de sumarlo es {tupla[0]} ")
print(f"El resultado de restarlo es {tupla[1]} ")
print(f"El resultado de dividirlo es {tupla[2]} ")
print(f"El resultado de multiplicarlo es {tupla[3]} ")