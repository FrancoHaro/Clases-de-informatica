# Edad y estatura de una persona
# %%
edad = 16
estatura = 1.77
# %%

#Triangulo
# %%
input("Ingrese la base del triángulo: ")
base = float(input())
input("Ingrese la altura del triángulo: ")
altura = float(input())
area_triangulo = (base * altura) / 2
print("El área del triángulo es: ", area_triangulo)
input("Ingrese el lado A del triángulo: ")
lado_a = float(input())
input("Ingrese el lado B del triángulo: ")
lado_b = float(input())
input("Ingrese el lado C del triángulo: ")
lado_c = float(input())
perimetro_triangulo = lado_a + lado_b + lado_c
print("El perímetro del triángulo es: ", perimetro_triangulo)
# %%

# Rectangulo
# %%
input("Ingrese la longitud del rectángulo: ")
longitud = float(input())
input("Ingrese el ancho del rectángulo: ")
ancho = float(input())
area_rectangulo = longitud * ancho
print("El área del rectángulo es: ", area_rectangulo)
perimetro_rectangulo = 2 * (longitud + ancho)
print("El perímetro del rectángulo es: ", perimetro_rectangulo)
# %%

# Circumferencia
# %%
input("Ingrese el radio de la circunferencia: ")
radio_circunferencia = float(input())
pi = 3.14
area_circunferencia = pi * radio_circunferencia ** 2
print("El área de la circunferencia es: ", area_circunferencia)
circunferencia_circunferencia = 2 * pi * radio_circunferencia
print("La circunferencia de la circunferencia es: ", circunferencia_circunferencia)
# %%

# Pendiente euclideana
# %%
punto_a = (2, 2)
punto_b = (6, 10)
pendiente_euclideana = (punto_b[1] - punto_a[1]) / (punto_b[0] - punto_a[0])
print("La pendiente euclideana entre los puntos A y B es: ", pendiente_euclideana)
# %%

# Valor de y
# %%
input("Ingrese el valor de x: ")
x = float(input())
y = x ** 2 + 6 * x + 9
print("El valor de y para x = ", x, " es: ", y)
# %%

# Longitud de una palabra
# %%
