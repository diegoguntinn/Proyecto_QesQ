# state.py
import reflex as rx


class State(rx.State):
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    @rx.event
    def answer(self):
        Personajes = {
    "Alex": ["hombre", "menton", "bigote", "ojos marrones", "pelo marron","alex"],
    "Alferd": ["hombre", "pelo largo", "pelirojo", "ojos azules", "bigote","alfred"],
    "Anita": ["mujer", "pelo rubio", "pelo largo", "lazitos", "ojos azules", "sonrojada","anita"],
    "Anne": ["mujer", "pelo rizo", "ojos marrones", "pelo marron", "gorda","anne"],
    "Bernard": ["hombre", "sombrero", "menton", "nariz grande", "ojos marrones", "pelo marron","bernard"],
    "Bill": ["hombre", "medio calvo", "pelirojo", "sonrojado", "gordo", "ojos marrones","bill"],
    "Charles": ["hombre", "pelo rubio", "ojos marrones", "bigote rubio","charles"],
    "Claire": ["mujer", "sombrero flores", "peliroja", "gafas azules", "ojos marrones","claire"],
    "David": ["hombre", "pelo rubio", "ojos marrones", "barba rubia","david"],
    "Eric": ["hombre", "sombrero", "pelo rubio", "ojos marrones","eric"],
    "Frans": ["hombre", "pelirojo", "ojos marrones", "pelo rizo","frans"],
    "George": ["hombre", "menton", "sombrero", "pelo blanco", "ojos marrones", "triste","george"],
    "Herman": ["hombre", "medio calvo", "pelirojo", "ojos marrones", "nariz grande","hernan"],
    "Joe": ["hombre", "menton", "pelo rubio", "gafas rojas", "ojos marrones","joe"],
    "Maria": ["mujer", "sombrero", "pelo marron", "ojos marrones","maria"],
    "Max": ["hombre", "pelo marron", "bigote", "ojos marrones", "pelo rizado","max"],
    "Paul": ["hombre", "menton", "gafas grises", "pelo blanco", "ojos marrones", "mayor","paul"],
    "Philip": ["hombre", "pelo rizo", "pelo marron", "ojos marrones", "barba marron","philip"],
    "Richard": ["hombre", "calvo", "ojos marrones", "barba", "bigote","richard"],
    "Robert": ["hombre", "sonrojado", "menton", "pelo marron", "nariz grande", "ojos azules", "triste","robert"],
    "Sam": ["hombre", "gafas negras", "medio calvo", "ojos marrones","sam"],
    "Susan": ["mujer", "sonrojada", "pelo blanco","pelo largo", "labios grandes", "ojos marrones","susan"],
    "Tom": ["hombre", "gafas rojas", "ojos azules", "medio calvo", "cara alargada","tom"],
    "Peter": ["hombre", "pelo blanco", "ojos azules", "nariz grande","peter"],
}

# Selección aleatoria de personaje por la máquina
personaje_maquina = random.choice(list(Personajes.keys()))

caracteristicas_unicas:["alex","charles","richard","sam","peter","tom","susan","robert","maria","philip","joe","paul","max","hernan","george","frans","eric","david","claire","bernard","bill","anne","anita","alfred",'barba', 'barba marron', 'barba rubia', 'bigote', 'bigote rubio', 'calvo', 'cara alargada', 'gafas azules', 'gafas grises', 'gafas negras', 'gafas rojas', 'gordo', 'hombre', 'labios grandes', 'lazitos', 'mayor', 'menton', 'medio calvo', 'mujer', 'nariz grande', 'ojos azules', 'ojos marrones', 'pelo blanco', 'pelo blanco y largo', 'pelo largo', 'pelo marron', 'pelo rizo', 'pelo rubio', 'peliroja', 'pelirojo', 'rubia', 'sombrero', 'sombrero flores', 'sonrojada', 'sonrojado', 'triste']
# Fragmento del bucle que evalúa palabra por palabra
# Verificar si alguna palabra o frase está en la historia
    resultados = [palabra for palabra in caracteristicas_unicas if palabra in pregunta]

    # Imprimir las palabras/frases encontradas
    if resultados:
        answer=("Si", resultados)
    else:
        answer=("No", resultados)
        # Our chatbot is not very smart right now...
        #answer = "I don't know!"
    self.chat_history.append((self.question, answer))