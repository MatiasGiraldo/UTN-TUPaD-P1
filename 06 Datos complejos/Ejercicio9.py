agenda = {
    ('lunes','13:00'): "Clase de canto",
    ('martes','16:00'): "Practicas",
    ('jueves','19:00'): "Repaso para el parcial"  
}

dia_consultado = input("Ingrese el dia: ")
hora_consultada = input("Ingrese la hora del día (ej: 15:00): ")

Consulta = (dia_consultado.lower(), hora_consultada)
for key in agenda:
    if Consulta == key:
        print(agenda[Consulta])