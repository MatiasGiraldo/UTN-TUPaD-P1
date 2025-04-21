num1 = int(input("Ingrese el primer numero distinto de 0: "))
num2 = int(input("Ingrese el segundo numero distinto de 0: "))
suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
div = num1 / num2
if (num1 == 0 or num2 == 0): 
    print("Ha ingresado un numero igual a 0")
else:{
    print(f"Los resultados de sumar, restar, multiplicar y dividir ambos numeros son {suma}, {resta}, {multi}, {div}")
}