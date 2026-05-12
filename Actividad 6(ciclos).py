# %%
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
# %%
suma = 0
contador = 0
notas = [8, 7, 9, 10, 6]
for nota in notas:
    print("La nota es:", nota)
    contador = contador + 1
    suma = suma + nota

promedio = suma / contador
print(f"El promedio es: {promedio}")

# %%

# %%
language = "Python"
for letter in language:
    print(letter)
# %%

# %%
palabra = input("Ingrese una palabra:").lower()
vocales = 0
consonantes = 0
letras = len(palabra)
for letra in palabra:
    print(letra)
    if letra  == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" :
        vocales = vocales + 1
    else:
        consonantes = consonantes + 1
print(f"El número de consonantes en la palabra '{palabra}' es: {consonantes}")
print(f"El número de vocales en la palabra '{palabra}' es: {vocales}")
print(f"El número total de letras en la palabra '{palabra}' es: {letras}")
