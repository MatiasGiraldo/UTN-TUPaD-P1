from math import pi
def calcular_area_circulo (radio):
    return radio * radio * pi
def calcular_perimetro_circulo (radio):
    return 2 * pi * radio 

radio = float(input("Ingrese radio del circulo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El area es {area} y el perimetro es {perimetro}")