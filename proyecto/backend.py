import random
import reflex
import os

# Diccionario de personajes con sus características
Personajes = {
    "Alex": ["hombre", "menton", "bigote", "corto"],
    "Alferd": ["hombre", "largo", "pelirojo", "bigote"],
    "Anita": ["mujer", "rubio", "largo", "lazos", "coloretes"],
    "Anne": ["mujer", "corto", " marron", "gorda",],
    "Bernard": ["hombre", "sombrero", "menton", "nariz grande", "marron"],
    "Bill": ["hombre", "calvo", "pelirojo", "coloretes", "gordo"],
    "Charles": ["hombre", "rubio", "bigote"],
    "Claire": ["mujer", "sombrero", "pelirojo", "gafas"],
    "David": ["hombre", "rubio", "barba"],
    "Eric": ["hombre", "sombrero", " rubio"],
    "Frans": ["hombre", "pelirojo"],
    "George": ["hombre", "menton", "sombrero", "blanco", "triste"],
    "Herman": ["hombre", "calvo", "pelirojo", "grande"],
    "Joe": ["hombre", "menton", "rubio", "gafas"],
    "Maria": ["mujer", "sombrero", "marron"],
    "Max": ["hombre", "marron", "bigote"],
    "Paul": ["hombre", "menton", "gafas", "blanco"],
    "Philip": ["hombre", "marron", "barba"],
    "Richard": ["hombre", "calvo", "barba", "bigote"],
    "Robert": ["hombre", "coloretes", "menton", "marron", "grande", "triste"],
    "Sam": ["hombre", "gafas", "calvo"],
    "Susan": ["mujer", "coloretes", "blanco","largo"],
    "Tom": ["hombre", "gafas", "calvo", "alargada"],
    "Peter": ["hombre", "blanco", "grande"],
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