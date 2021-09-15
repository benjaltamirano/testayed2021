"""
El programa debe:
*   mostrar el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""
while True:
    palabra_usuario=(input("ingrese una palabra: "))
    if palabra_usuario == "salir":
        print("Ya fue")
    else:
        print(f"ingresaste {palabra_usuario}")
        break
