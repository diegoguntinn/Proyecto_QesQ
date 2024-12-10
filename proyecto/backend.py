import random
import reflex
import os

# Diccionario de personajes con sus características
Personajes = {
    "Alex": ["hombre", "negro", "corto", "menton", "bigote"],
    "Alferd": ["hombre", "pelirojo", "largo", "bigote"],
    "Anita": ["mujer", "rubio", "largo", "lazos", "coloretes"],
    "Anne": ["mujer", "negro", "corto", "gorda",],
    "Bernard": ["hombre", "marron", "corto", "sombrero", "menton", "nariz grande", ],
    "Bill": ["hombre", "pelirojo", "calvo", "coloretes", "gordo"],
    "Charles": ["hombre", "rubio", "corto", "bigote"],
    "Claire": ["mujer", "pelirojo", "corto", "sombrero",  "gafas"],
    "David": ["hombre", "rubio", "corto", "barba"],
    "Eric": ["hombre", "rubio", "corto", "sombrero",],
    "Frans": ["hombre", "pelirojo", "corto"],
    "George": ["hombre", "blanco", "corto", "menton", "sombrero", "triste"],
    "Herman": ["hombre", "calvo", "pelirojo", "grande"],
    "Joe": ["hombre", "rubio", "corto", "menton", "gafas"],
    "Maria": ["mujer", "marron", "largo", "sombrero"],
    "Max": ["hombre", "negro", "corto", "bigote"],
    "Paul": ["hombre", "blanco", "corto", "menton", "gafas", ],
    "Peter": ["hombre", "blanco", "corto", "grande"],
    "Philip": ["hombre", "negro", "corto", "barba"],
    "Richard": ["hombre", "marron", "calvo", "barba", "bigote"],
    "Robert": ["hombre", "marron", "corto", "coloretes", "menton", "grande", "triste"],
    "Sam": ["hombre", "blanco", "calvo", "gafas"],
    "Susan": ["mujer", "blanco", "largo", "coloretes"],
    "Tom": ["hombre", "negro", "calvo", "gafas", "alargada"],
}

# Selección aleatoria de personaje por la máquina
#personaje_maquina = random.choice(list(Personajes.keys()))

caracteristicas_unicas = ["alex","charles","richard","sam","peter","tom","susan","robert","maria","philip","joe","paul","max","hernan","george","frans","eric","david","claire","bernard","bill","anne","anita","alfred",'barba', 'barba marron', 'barba rubia', 'bigote', 'bigote rubio', 'calvo', 'cara alargada', 'gafas azules', 'gafas grises', 'gafas negras', 'gafas rojas', 'gordo', 'hombre', 'labios grandes', 'lazitos', 'mayor', 'menton', 'medio calvo', 'mujer', 'nariz grande', 'ojos azules', 'ojos marrones', 'pelo blanco', 'pelo blanco y largo', 'pelo largo', 'pelo marron', 'pelo rizo', 'pelo rubio', 'peliroja', 'pelirojo', 'rubia', 'sombrero', 'sombrero flores', 'sonrojada', 'sonrojado', 'triste']
# Fragmento del bucle que evalúa palabra por palabra

#def pregunta(form_input1):
#    pregunta = pregunta.lower()
#    for palabra in pregunta.split():  # Dividir la pregunta en palabras
#        if palabra in caracteristicas_unicas:  # Comprobar si la palabra está en la lista de características
#            if palabra in Personajes[personaje_maquina]:  # Verificar si el personaje tiene la característica
#                print("Si")
#            else:
#                print("No")
#            break  # Salir del bucle al encontrar una coincidencia válida
#        else:
#            continue
def answer():    
    pregunta = 'es hombre?'
    # Verificar si alguna palabra o frase está en la historia
    resultados = [palabra for palabra in caracteristicas_unicas if palabra in pregunta]

    # Imprimir las palabras/frases encontradas
    if resultados:
        print("Si", resultados)
    else:
        print("No", resultados)