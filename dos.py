print("ingresa tus 3 nimeros favoritos y te dire cual es el mayor y el menor")
numeros = []

for i in range (3):
    numero = int(input(f"introduce el valor del numero {i+1} "))
    numeros.append(numero)
    menor = numeros[0]
    mayor = numeros[0]

    for numero in numeros:
        if numero < menor:
            menor = numero
    
    for numero in numeros:
        if numero > mayor:
            mayor = numero
    
print("menor: ", menor)
print("mayor: ", mayor)

