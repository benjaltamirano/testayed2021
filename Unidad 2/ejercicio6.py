try:
    dinero_actual= float(input("Ingrese dinero actual"))
    precio_insumo= float(input("Ingrese el precio del isnumo (usd): "))
    dinero_actual_usd= dinero_actual/170
    print(dinero_actual_usd>=precio_insumo)
except:
    print("escribiste mal uachin")
