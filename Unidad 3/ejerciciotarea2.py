"""
El programa debe:
*    Pedir al usuario una cantidad de tramos de un viaje
*    Pedir al usuario la duración en minutos de cada tramo
*    Calcular el tiempo total de viaje
*    No deben generar errores
"""
try:
    usuario=int(input("ingrese cantidad de tramos del viaje: "))
    minutos=float(input("ingrese minutos de cada tramo: "))
    viaje_minutos= usuario*minutos
    viaje_horas=(usuario*minutos)/60
    print(f"El viaje va a durar {viaje_minutos} minutos")
    print(f"O el viaje va a durar {viaje_horas} horas")
except:
    print("Error")