num = int(input("Ingrese numero: "))
num_inv = 0
while num > 0:
    dig = num % 10
    num_inv = num_inv * 10 + dig
    num = num // 10
print(num_inv)