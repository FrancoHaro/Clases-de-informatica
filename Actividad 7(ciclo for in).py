# LISTAS
# %%
notas = [8.5, 6.0, 9.0, 7.0, 5.5]
acumulador = 0
suma = 0
aprobados = 0
reprobados = 0
for nota in notas:
    print(f"La nota {acumulador + 1} es: {nota}")
    acumulador = acumulador + 1
    suma = suma + nota
    if nota < 7:
        print("Estudiante reprobado")
        reprobados = reprobados + 1
    else:
        print("Estudiante aprobado")
        aprobados = aprobados + 1
print(f"La suma de las notas es: {suma}")
print(f"El promedio de las notas es: {suma / acumulador}")
print(f"El número de estudiantes aprobados es: {aprobados}")
print(f"El número de estudiantes reprobados es: {reprobados}")
# %%

# %%
contraseña = "Python2026"
numeros = 0
abcedario = 0
o = 0
for letra in contraseña:
    print(letra)
    if letra == "1" or letra == "2" or letra == "3" or letra == "4" or letra == "5" or letra == "6" or letra == "7" or letra == "8" or letra == "9" or letra == "0":
        numeros = numeros + 1
    else: 
        abcedario = abcedario + 1
    if letra.upper() == "O":
        o = o + 1
print(f"El número de letras en la contraseña es: {abcedario}")
print(f"El número de números en la contraseña es: {numeros}")
print(f"El número de letras 'o' en la contraseña es: {o}")
# %%


