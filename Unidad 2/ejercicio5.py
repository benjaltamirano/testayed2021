"""
El programa debe:

pedir por teclado el dinero actual de una persona
pedir por teclado el precio del insumo que quiere comprar en USD
convertir ese dinero a dolares( 1USD -> 170$)
devoler por pantalla True en caso que pueda comprar, False en caso que no
No deben aparecer errores
"""
dinero_actual=float(input("Ingrese dinero actual"))
precio_insumo=float(input("Ingrese el precio del isnumo (usd): "))
dinero_actual_usd= dinero_actual/170
print(dinero_actual_usd>=precio_insumo)

