"""
##**Ejercicio 4.5 (Cajero automatico)**
El programa debe:
*   Simular un cajero automatico y pedir usuario y contraseña (user, 1234) caso verdadero mostrar menu 
    y en caso falso seguir pidiendo.
*   En caso de mal ingreso de usuario o contraseña 3 veces el programa debe detenerse
*   El menu debe mostrar las funciones posteriores.
*   Contar con 4 funciones:
  1.  Consultar el saldo (inicio de 50000)
  2.  Ingresar dinero y actualizar saldo
  3.  Retirar dinero y actualizar saldo
  4.  Salir, y volver al menu de usuario y contraseña
*   Gestionar posibles errores
"""
import funcionesSaldo as fs
import funcionAutenticar as fa

while True:
    condicion=input("""Por favor ingrese una opcion
        - 1.consultar saldo
        - 2.Ingresar dinero
        - 3.Retirar dinero
        - 4.division
        ingreso : """)
    if condicion == "1":
        dinero_disponible = fs.consultar_saldo(dinero_disponible)
    elif (condicion == "2"):
        dinero_disponible=fs.ingresar_y_actualizar(dinero_disponible)
    elif (condicion == "3:"):
        dinero_disponible= fs.retirar_y_actualizar(dinero_disponible)
    elif (condicion == "4:"):
        pass
    elif (condicion == "5:"):
        print("Gracias por usar la Calculadora")
        
    else:
        print("error, ninguna opcion es correcta")