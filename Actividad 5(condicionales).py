# %%
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
# %%

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
# %%
# %%
print("Ingrese un número")
c = int(input())
print("El numero es positivo y par" if c >0 and c % 2 == 0 else "El numero es positivo e impar" if c > 0 and c % 2 == 1 else "El numero es negativo y par" if c < 0 and c % 2 == 0 else "El numero es negativo e impar" if c < 0 and c % 2 == 1 else "El numero es cero")
