import random
import reflex
import os

# Diccionario de personajes con sus características
Personajes = {
    "Alex": ["hombre", "negro", "corto", "menton", "bigote", "grandes"],
    "Alferd": ["hombre", "pelirojo", "largo", "bigote"],
    "Anita": ["mujer", "rubio", "largo", "lazos", "lacitos", "coloretes", "sonrojado"],
    "Anne": ["mujer", "negro", "corto", "gorda", "pendientes", "rizo"],
    "Bernard": ["hombre", "marron", "corto", "sombrero", "gorro", "menton", "grande"],
    "Bill": ["hombre", "pelirojo", "calvo", "coloretes", "perilla", "sonrojado", "gordo"],
    "Charles": ["hombre", "rubio", "corto", "bigote", "grandes"],
    "Claire": ["mujer", "pelirojo", "corto", "sombrero", "sombrero", "gafas", "pendientes"],
    "David": ["hombre", "rubio", "corto", "barba", "perilla"],
    "Eric": ["hombre", "rubio", "corto", "sombrero", "gorro"],
    "Frans": ["hombre", "pelirojo", "corto", "rizo"],
    "George": ["hombre", "blanco", "corto", "menton", "sombrero", "gorro", "triste"],
    "Herman": ["hombre", "calvo", "pelirojo", "grande"],
    "Joe": ["hombre", "rubio", "corto", "menton", "gafas"],
    "Maria": ["mujer", "marron", "largo", "sombrero", "gorro", "pendientes"],
    "Max": ["hombre", "negro", "corto", "bigote", "grande", "grandes"],
    "Paul": ["hombre", "blanco", "corto", "menton", "gafas", ],
    "Peter": ["hombre", "blanco", "corto", "grande", "grandes"],
    "Philip": ["hombre", "negro", "corto", "barba", "coloretes", "sonrojado"],
    "Richard": ["hombre", "marron", "calvo", "barba", "bigote", "alargada"],
    "Robert": ["hombre", "marron", "corto", "coloretes", "sonrojado", "menton", "grande", "triste"],
    "Sam": ["hombre", "blanco", "calvo", "gafas"],
    "Susan": ["mujer", "blanco", "largo", "coloretes", "sonrojado", "grandes"],
    "Tom": ["hombre", "negro", "calvo", "gafas", "alargada"],
}



#caracteristicas_unicas = ["alex","charles","richard","sam","peter","tom","susan","robert","maria","philip","joe","paul","max","hernan","george","frans","eric","david","claire","bernard","bill","anne","anita","alfred",'barba', 'bigote', 'calvo', 'gafas','gordo', 'hombre', 'lazitos', 'mayor', 'menton', 'mujer', 'blanco', 'largo', 'marron', 'rubio', 'peliroja', 'pelirojo', 'rubia', 'sombrero', 'sonrojada', 'sonrojado', 'triste','negro']
