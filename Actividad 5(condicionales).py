print("Ingrese un número")
a = int(input())

if a == 0:
    print("El número es cero")
else:
    if a > 0:
        if a % 2 == 0:
            print("El número es positivo y par")
        else:
            print("El número es positivo e impar")
    else:
        if a % 2 == 0:
            print("El número es negativo y par")
        else:
            print("El número es negativo e impar")
print("Fin del programa")

print ("Ingrese un número")
b = int(input())
if b > 0 and b % 2 == 0:
    print("El número es positivo y par")
elif b > 0 and b % 2 == 1:
    print("El número es positivo e impar")
elif b < 0 and b % 2 == 0:
    print("El número es negativo y par")
elif b < 0 and b % 2 == 1:
    print("El número es negativo e impar")
else:
    print("El numero es cero")

