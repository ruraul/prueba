mayor = None
menor = None
nuevo_numero = 0

def menu():

    print("Selecciona una operación")
    print("\t1 agregar")
    print("\t2 terminar")
    print("\t4 salir")

while True:
    menu()
    opcionMenu = input("insertar numero del menu")
    if opcionMenu == '1':
        print("Agregar numero")
        nuevo_numero = int(input("ingrese el valor del nuevo numero: "))
        if(menor is None):
            menor = nuevo_numero
            
        if(mayor is None and nuevo_numero > menor):
            mayor = nuevo_numero
        
        if(nuevo_numero < menor):
            menor = nuevo_numero
        
        if(nuevo_numero > mayor and menor):
            mayor = nuevo_numero

    elif opcionMenu == '2':
        print(f"El numero mayor es: {mayor} y el numero menor es: {menor}")

    elif opcionMenu =='4':
        break
        