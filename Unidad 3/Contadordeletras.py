frase=input("ingrese frase: ")
letra=input("ingrese letra que quiere contar: ")
contador=0

for i in frase:
    if i == letra:
        contador+=1

print(f"el numero de veces de la letra:{letra} es {contador}")
    
