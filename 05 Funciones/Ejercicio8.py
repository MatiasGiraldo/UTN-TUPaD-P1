def calcular_imc(peso, altura):
    return peso / (altura*altura)

peso = float(input("Ingrese peso en Kg: "))
altura = float(input("Ingrese altura en metros: "))
IMC = calcular_imc(peso,altura)
print(f"Su indice de masa corpotal es {round(IMC,2)}")