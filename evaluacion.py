# ===== PARTE A =====
# Respuesta 1: 
"""
a) Indica el tipo de dato de cada variable.
nombre: str
edad: int
promedio: float
materias: list
"""
# Respuesta 2:
"""
b) Escribe qué mostraría el programa en pantalla.
El programa mostraría lo siguiente en pantalla:
class 'str'
class 'int'
class 'float'
class 'list'
6
"""
# Respuesta 3:
"""
c) Explica qué hace len(nombre).
len(nombre) devuelve la cantidad de caracteres que tiene la variable nombre. Por ejemplo, si nombre es "Mateo", len(nombre) devolvería 5, ya que "Mateo" tiene 5 caracteres.
"""
# Respuesta 4:
"""
a) ¿Qué diferencia hay entre almacenar un valor en una variable y mostrarlo con
print()?
Almacenaar un valor en una variable es asignarle un valor a esa variable mientras que mostrarlo0 con print() es mostrar el valor almacenado de la variable en la pantalla o terminal.
"""
# Respuesta 5:
"""
b) ¿Por qué input() devuelve texto aunque el usuario escriba un número?
input() devuelve texto porque su función principal es recibir datos del usuario en forma de string. Incluso si el usuario escribe un número, input() lo interpretara como texto. 
"""
# Respuesta 6:
"""
c) Explica la diferencia entre **, // y %.
** Eleva un número a la potencia de otro.
// Es el operador de división entera, que devuelve el cociente sin el resto.
% Devuelve el resto o el residuo de la división.
"""
# Respuesta 7:
"""
e) Escribe una instrucción que permita consultar las palabras reservadas de Python.
import keyword
print(keyword.kwlist)
"""
# ===== PARTE B =====
# Código corregido
"""
print("Ingrese la base del anuncio: ")
base = input()
print("Ingrese la altura del anuncio: ")
altura = input()
print("Ingrese el precio por metro cuadrado: ")
precio = input()
superficie = float(base) * float(altura)
valor = superficie * float(precio)
print("Superficie total: " + str(superficie))
print("Valor estimado: " + str(valor))
"""
# Respuesta 1:
"""
a) ¿Cuáles eran los errores principales?
Los errores eran que se intentaba hacer operaciones matematicas con variables tipo string.
"""
# Respuesta 2:
"""
b) ¿Por qué tu corrección sí funciona?
Las variabes las converti en tipo float antes de realizar las operaciones matemáticas, lo que permite que phyton las realice de forma correcta.
"""
# Respuesta 3:
"""
Escribe un fragmento de código que haga lo siguiente:
1. Cree la variable frase con el texto "Aprender Python es útil".
2. Muestre la frase en minúsculas.
3. Muestre la cantidad de caracteres de la frase.
4. Verifique si la palabra "Python" está dentro de la frase.
5. Reemplace "útil" por "interesante".
6. Divida la frase en palabras usando split(). 

Respuesta:
texto = "Aprender Python es útil"
print(texto.lower())
print(len(texto))
print("Python" in texto)
print(texto.replace("útil", "interesante"))
print(texto.split())


