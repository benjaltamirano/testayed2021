"""
###**Ejercicio**
El programa debe:
*     Preguntar al usuario una cantidad a invertir
*     Preguntar al usuario el interés anual y el número de años
*     Mostrar por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""
dinero=float(input("Ingrese cantidad de dinero a invertir: "))
interes_anual=float(input("Ingrese el interes anual en porcentaje: "))
años=int(input("Ingrese cantidad de años que desea inverir su dinero: "))
for i in range(1,años+1):
    dinero+=dinero*interes_anual/100
    print(f"El capital obtenido en el año {i} es de ${dinero}")
