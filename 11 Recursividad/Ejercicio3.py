def pot(base,exp):
    if exp == 0:
        return 1
    else:
        return base * (base ** (exp-1))
    resul= base * (base ** (exp-1))
    
print(pot(5,3))