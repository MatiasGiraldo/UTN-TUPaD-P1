def calcular_promedio(a,b,c): 
    return (a+b+c) / 3

num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))
num3 = int(input("Ingrese tercer numero: "))

promedio = calcular_promedio(num1,num2,num3)
print(f"El promedio de los tres numeros es {promedio}")