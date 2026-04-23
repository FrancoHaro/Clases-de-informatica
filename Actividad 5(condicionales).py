print("Ingrese un número:")
a = float(input())
if a > 0:
    print(f"El número es positivo: {a}")
elif a < 0:
    print(f"El número es negativo: {a}")
else:
    print(f"El número es cero: {a}")
print("Fin del programa")
# %%
print("Ingrese un número entre 0 y 100:")
a = float(input())
if a < 0 or a > 100:
    print("Número fuera de rango")
else:
    if a < 70:
        print("D")
    else:
        if a < 80:
            print("C")
        else:
            if a < 90:
                print("B")
            else:
                if a < 100:
                    print("A")
print("Fin del programa")


# %%
