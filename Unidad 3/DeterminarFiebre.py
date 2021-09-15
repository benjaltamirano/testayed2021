"""
Determinar si una persona tiene fiebre. (fiebre : 37.5 grados) o tiene menos de 30° y sino esta sano
"""
persona=float(input("ingrese temperatura corporal"))
if persona>= 37.5:
    print("Tenes temperatura corporal elevada")
elif persona < 30:
    print("Tenes 30 grados de temperatura")
else:
    print("Estas sano")
    