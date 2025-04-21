def celsius_a_fahrenheit(celsius) :
    return celsius * (9/5) + 32

celsius = float(input("Ingrese temperatura en grados celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"Su equivalente en Fahrenheit es {fahrenheit}")