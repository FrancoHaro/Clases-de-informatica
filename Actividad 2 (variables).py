# Actividad en clase 2
"""Franco Haro
15//4/2026
Actividad 2: Variables"""

# Variables de texto
# %%
nombre = "Franco"
print(nombre)
apellido = "Haro"
print(apellido)
nombre_completo = "Franco Haro"
print(nombre_completo)
pais = "Ecuador"
print(pais)
año = 2026
print(año)
esta_casado = False
print(esta_casado)
es_verdadero = True
print(es_verdadero)
luz_encendida = True
print(luz_encendida)
print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(año))
print(type(esta_casado))
print(type(es_verdadero))
print(type(luz_encendida))
print(len(nombre))
# %%
# Variables numericas
# %%
numero_uno = 5
print(numero_uno)
numero_dos = 4
print(numero_dos)
total = numero_uno + numero_dos
print("La suma es: ", total)
diferencia = numero_uno - numero_dos
print("La resta es: ", diferencia)
producto = numero_uno * numero_dos
print("El producto es: ", producto)
division = numero_uno / numero_dos
print("La división es: ", division)
residuo = numero_uno % numero_dos
print("El residuo es: ", residuo)
potencia = numero_uno ** numero_dos
print("La potencia es: ", potencia)
division_entera = numero_uno // numero_dos
print("La división entera es: ", division_entera)

# %%

# %%
nombre , apellido , nombre_completo , pais , año , esta_casado , es_verdadero , luz_encendida = "Franco" , "Haro" , "Franco Haro" , "Ecuador" , 2026 , False , True , True
print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(año))
print(type(esta_casado))
print(type(es_verdadero))
print(type(luz_encendida))
# %%

# Circulo
# %%
radio = 30
pi = 3.14
print("El radio del círculo es: ", radio)
area_circulo = pi * radio ** 2
print("El área del círculo es: ", area_circulo)
circunferencia_circulo = 2 * pi * radio
print("La circunferencia del círculo es: ", circunferencia_circulo)
print("Ingrese el radio del círculo: ")
radio_usuario = float(input())
area_circulo_usuario = pi * radio_usuario ** 2
print("El área del círculo con radio ", radio_usuario, " es: ", area_circulo_usuario)

# %%

# Input
# %%
print("Ingrese su nombre: ")
nombre_usuario = input()
print("Ingrese su apellido: ")
apellido_usuario = input()
print("Ingrese su país: ")
pais_usuario = input()
print("Ingrese su edad: ")
edad_usuario = int(input())
# %%

help("keywords")
