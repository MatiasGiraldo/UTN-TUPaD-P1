def tabla_multiplicar (num):
    for i in range (10):
        multiplica = (i+1) * num
        resultado = print(f"{num} x {i+1} = {multiplica}")
    return resultado
num = int(input("Ingrese numero: "))
tabla_multiplicar(num)