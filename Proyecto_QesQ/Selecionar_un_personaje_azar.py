personajes = {
    "Alex": "images/Alex.png",
    "Alfred": "images/Alfred.png",
    "Anita": "images/Anita.png",
    "Anne": "images/Anne.png",
    "Bernard": "images/Bernard.png",
    "Bill": "images/Bill.png",
    "Charles": "images/Charles.png",
    "Claire": "images/Claire.png",
    "David": "images/David.png",
    "Eric": "images/Eric.png",
    "Frans": "images/Frans.png",
    "George": "images/George.png",
    "Herman": "images/Herman.png",
    "Joe": "images/Joe.png",
    "Maria": "images/Maria.png",
    "Max": "images/Max.png",
    "Paul": "images/Paul.png",
    "Peter": "images/Peter.png",
    "Philip": "images/Philip.png",
    "Richard": "images/Richard.png",
    "Robert": "images/Robert.png",
    "Sam": "images/Sam.png",
    "Susan": "images/Susan.png",
    "Tom": "images/Tom.png"
}
import random

personaje_maquina = random.choice(list(personajes.keys()))
imagen_personaje_maquina = personajes[personaje_maquina]

print(f"La máquina ha elegido: {personaje_maquina}")
print(f"Ruta de la tarjeta: {imagen_personaje_maquina}")
