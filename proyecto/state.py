# state.py
import reflex as rx
import random
from proyecto.backend import Personajes

class State(rx.State):
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]
    answers: str 
#    @rx.event

    personaje_maquina = random.choice(list(Personajes.keys()))

    caracteristicas_unicas = ["alex","charles","richard","sam","peter","tom","susan","robert","maria","philip","joe","paul","max","herman","george","frans","eric","david","claire","bernard","bill","anne","anita","alfred",'barba', 'barba marron', 'barba rubia', 'bigote', 'bigote rubio', 'calvo', 'cara alargada', 'gafas azules', 'gafas grises', 'gafas negras', 'gafas rojas', 'gordo', 'hombre', 'labios grandes', 'lazitos', 'mayor', 'menton', 'medio calvo', 'mujer', 'nariz grande', 'ojos azules', 'ojos marrones', 'pelo blanco', 'pelo blanco y largo', 'pelo largo', 'pelo marron', 'pelo rizo', 'pelo rubio', 'peliroja', 'pelirojo', 'rubia', 'sombrero', 'sombrero flores', 'sonrojada', 'sonrojado', 'triste']

    personaje_maquina: str

    def pregunta(self):
        #question = pregunta.lower()
        for palabra in self.question.split():  # Dividir la pregunta en palabras
            if palabra in self.caracteristicas_unicas:
                self.answers = 'esta en la lista'  # Comprobar si la palabra está en la lista de características
                if palabra in Personajes[self.personaje_maquina]:  # Verificar si el personaje tiene la característica
                    self.answers = "Si"
                else:
                    self.answers = "No"
                break  # Salir del bucle al encontrar una coincidencia válida
            else:
                continue
    def answer(self):
#        
#
## Selección aleatoria de personaje por la máquina
        

        caracteristicas_unicas = ["alex","charles","richard","sam","peter","tom","susan","robert","maria","philip","joe","paul","max","herman","george","frans","eric","david","claire","bernard","bill","anne","anita","alfred",'barba', 'barba marron', 'barba rubia', 'bigote', 'bigote rubio', 'calvo', 'cara alargada', 'gafas azules', 'gafas grises', 'gafas negras', 'gafas rojas', 'gordo', 'hombre', 'labios grandes', 'lazitos', 'mayor', 'menton', 'medio calvo', 'mujer', 'nariz grande', 'ojos azules', 'ojos marrones', 'pelo blanco', 'pelo blanco y largo', 'pelo largo', 'pelo marron', 'pelo rizo', 'pelo rubio', 'peliroja', 'pelirojo', 'rubia', 'sombrero', 'sombrero flores', 'sonrojada', 'sonrojado', 'triste']
    # Fragmento del bucle que evalúa palabra por palabra
    # Verificar si alguna palabra o frase está en la historia
    
        
    # Verificar si alguna palabra o frase está en la historia
        
        self.answers = 'error critico, diego tonto' 
    # Imprimir las palabras/frases encontradas
       # pregunta = pregunta.lower()
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
                break  # Salir del bucle al encontrar una coincidencia válida
            else:
                continue
        self.chat_history = []
        self.chat_history.append((self.question, self.answers))