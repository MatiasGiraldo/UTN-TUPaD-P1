alumnos = {
    'Marcos': (6, 8, 10),
    'Carol': (10, 5, 7), 
    'Manuel': (1, 7, 10), 
    }

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es {promedio}")

