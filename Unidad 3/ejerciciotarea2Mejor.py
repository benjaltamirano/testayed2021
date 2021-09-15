while True:
    try:
        while True:
            cantidad_tramos=int(input("Ingrese cantidad de tramos"))
            if cantidad_tramos<=0:
                print("ingrese un num mayor a 0")
            else:
                break
        tiempo_total_viaje=0
        for i in range(cantidad_tramos):
            while True:
                tiempo_tramo=int(input(f"ingrese la duracion del tramo{i+1}"))
                if (tiempo_tramo) <0:
                    print("ingrese un numero mayor a 0")
                else:
                    tiempo_total_viaje+=tiempo_tramo
                    break
        print(f"el tiempo total del viaje fue: {(tiempo_total_viaje/60)} horas")
        break
    except:
        print("error")
