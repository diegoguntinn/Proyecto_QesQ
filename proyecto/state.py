# state.py
import reflex as rx
import random
from proyecto.backend import Personajes

class State(rx.State):
    question: str

    chat_history: list[tuple[str, str]]
    answers: str 

    personaje_maquina = random.choice(list(Personajes.keys()))

    caracteristicas_unicas = ["alex","charles","richard","sam","peter","tom","susan","robert","maria","philip","joe","paul","max","herman","george","frans","eric","david","claire","bernard","bill","anne","anita","alfred",'barba', 'barba marron', 'barba rubia', 'bigote', 'bigote rubio', 'calvo', 'cara alargada', 'gafas azules', 'gafas grises', 'gafas negras', 'gafas rojas', 'gordo', 'hombre', 'labios grandes', 'lazitos', 'mayor', 'menton', 'medio calvo', 'mujer', 'nariz grande', 'ojos azules', 'ojos marrones', 'pelo blanco', 'pelo blanco y largo', 'pelo largo', 'pelo marron', 'pelo rizo', 'pelo rubio', 'peliroja', 'pelirojo', 'rubia', 'sombrero', 'sombrero flores', 'sonrojada', 'sonrojado', 'triste']

    personaje_maquina: str


    def answer(self):
      
        self.answers = 'Esta caracteristica no es valida' 

        for palabra in self.question.split():  # Dividir la pregunta en palabras
            if palabra in self.caracteristicas_unicas:
                self.answers = 'esta en la lista'  # Comprobar si la palabra está en la lista de características
                
                if palabra in Personajes[self.personaje_maquina]:  # Verificar si el personaje tiene la característica
                    self.answers = "Si"
                elif palabra.capitalize() == self.personaje_maquina:
                    self.answers = f"GG ganaste"
                elif palabra not in Personajes[self.personaje_maquina]:
                    self.answers = "No"
                else:
                    self.answers = f"Q malo"
                break  
            else:
                continue
        self.chat_history = []  # reinicia el historial de chat a un chat vacio
        self.chat_history.append((self.question, self.answers))