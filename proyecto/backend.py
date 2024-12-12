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



#caracteristicas_unicas = ["alex","charles","richard","sam","peter","tom","susan","robert","maria","philip","joe","paul","max","hernan","george","frans","eric","david","claire","bernard","bill","anne","anita","alfred",'barba', 'bigote', 'calvo', 'gafas','gordo', 'hombre', 'lazitos', 'mayor', 'menton', 'mujer', 'blanco', 'largo', 'marron', 'rubio', 'peliroja', 'pelirojo', 'rubia', 'sombrero', 'sonrojada', 'sonrojado', 'triste','negro']