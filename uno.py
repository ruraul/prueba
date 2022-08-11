print("Ingresar los valores para el primer ejemplo")
valor_inicial = int(input("ingrese el valor inicial "))
valor_final = int(input("ingrese el valor final "))
valor_rango = int(input("ingrese el rango de la suma "))
resultado = 0

if(valor_inicial > valor_final):
    print("el valor final debe ser mayor al primer valor")
elif(valor_inicial < valor_final):
    
    for i in range(valor_inicial, valor_final + valor_rango , valor_rango):
        resultado = resultado + i
    print(resultado)
        
