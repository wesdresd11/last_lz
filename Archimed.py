mass = int(input("Введите массу тела(кг):"))
volume = float(input("Введите объем погруженной части тела(M**3):"))
rwater = 1000
g = 10
swimming = (rwater*volume*g)/(mass*g)
archimed = lambda swimming: True if swimming >= 1 else False
print(archimed(swimming))