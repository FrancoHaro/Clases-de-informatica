# %%
stringVariasLineas = """
Franco
Haro
Informatica
"""
print(stringVariasLineas)
colegio = "iSM"
longitud = len(colegio)
print("La longitud de la palabra colegio es: ", longitud)
print(len("ISM"))
nombre = "Franco"
apellido = "Haro "
nombre_completo = nombre + " " + apellido
print("Mi nombre completo es: ", nombre_completo)
print(nombre_completo * 2)
print("Phyton \nchallenge")
print("Semana 1 \tSemana 2 \tSemana 3")
print("Simbolo(\\)")
print(f"Mi nombre es {nombre} y mi apellido es {apellido}")
languaje = "Python"
a, b, c, d, e, f = languaje
print(a)
languaje = "Python"
print(languaje[0:3])
print(languaje[1])
print(languaje[2])
print(languaje[3])
print(languaje[4])

last_tree = languaje[-3:]
print(last_tree)

greeting = "Hello, World!"
print(greeting[::-1])

challenge = "Treinta dias en Python"
print()
# %%

# Actividad 4 (strings)
# %%
# Crear la variable 

texto = "Programación Para Todos" 

# Mostrar el contenido 

print(f"Contenido: {texto}") 

# Cantidad de caracteres 

print(f"Longitud: {len(texto)}") 

print(texto.upper())       # MAYÚSCULAS 

print(texto.lower())       # minúsculas 

print(texto.title())       # Formato De Título 

print(texto.capitalize())  # Solo la primera letra 

print(texto.startswith("Programación")) # True 

print(texto.endswith("Todos"))          # True 

print(texto.find("Para"))               # 13 (posición de inicio) 

print("Python" in texto)                # False (no está en la cadena original) 

# Reemplazar palabra 

nuevo_texto = texto.replace("Programación", "Python") 

print(nuevo_texto) 

# Dividir en palabras 

palabras = texto.split() 

print(palabras)  # ['Programación', 'Para', 'Todos'] 

# Unir con un separador 

unido = " - ".join(palabras) 

print(unido)     # Programación - Para – Todos 

print(f"Primer carácter: {texto[0]}")     # 'P' 

print(f"Último carácter: {texto[-1]}")    # 's' 

print(f"Carácter en pos 5: {texto[5]}")   # 'a' 


mi_nombre = "Gemini AI" 


# Mensaje con f-string 

print(f"Hola, mi nombre es {mi_nombre}") 


# Acronimo

# Crear un acrónimo (G.A.) 

# Dividimos el nombre y tomamos la primera letra de cada parte 

acronimo = "".join([palabra[0] for palabra in mi_nombre.split()]) 

print(f"Acrónimo: {acronimo}") 