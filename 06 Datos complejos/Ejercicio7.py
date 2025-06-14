# el numero representa a cada estudiante que aprobó un parcial
Parcial_1 = {102, 107, 110, 111, 113}
Parcial_2 = {103, 106, 107, 108 , 111}

print(f"Los alumnos que aprobaron ambos parciales: {Parcial_1 & Parcial_2}")
print(f"Los alumnos que aprobaron solo uno de los dos: {Parcial_1 ^ Parcial_2}")
print(f"Los alumnos que aprobaron ambos parciales: {Parcial_1 | Parcial_2}")