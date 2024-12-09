import reflex as rx
import os
import random
import rxconfig as config

from proyecto import style
from proyecto.state import State
from proyecto.backend import Personajes

class ClassState(rx.State):
    img_src_alex: str = "Alex.png"  # Initial image source
    img_src_alfred: str = "Alfred.png"
    img_src_anita: str = "Anita.png"
    img_src_anne: str = "Anne.png"
    img_src_bernard: str = "Bernard.png"
    img_src_bill: str = "Bill.png"
    img_src_charles: str = "Charles.png"
    img_src_claire: str = "Claire.png"
    img_src_david: str = "David.png"
    img_src_eric: str = "Eric.png"
    img_src_frans: str = "Frans.png"
    img_src_george: str = "George.png"
    img_src_herman: str = "Herman.png"
    img_src_joe: str = "Joe.png"
    img_src_maria: str = "Maria.png"
    img_src_max: str = "Max.png"
    img_src_paul: str = "Paul.png"
    img_src_peter: str = "Peter.png"
    img_src_philip: str = "Philip.png"
    img_src_richard: str = "Richard.png"
    img_src_robert: str = "Robert.png"
    img_src_sam: str = "Sam.png"
    img_src_susan: str = "Susan.png"
    img_src_tom: str = "Tom.png"


    def toggle_image_alex(alex):
        # Toggle the image source
        alex.img_src_alex = "XAlex.png" if alex.img_src_alex == "Alex.png" else "Alex.png"
    
    def toggle_image_alfred(alfred):
        # Toggle the image source
        alfred.img_src_alfred = "XAlfred.png" if alfred.img_src_alfred == "Alfred.png" else "Alfred.png"

    def toggle_image_anita(anita):  
        anita.img_src_anita = "XAnita.png" if anita.img_src_anita == "Anita.png" else "Anita.png"

    def toggle_image_anne(anne):  
        anne.img_src_anne = "XAnne.png" if anne.img_src_anne == "Anne.png" else "Anne.png"

    def toggle_image_bernard(bernard):  
        bernard.img_src_bernard = "XBernard.png" if bernard.img_src_bernard == "Bernard.png" else "Bernard.png"

    def toggle_image_bill(bill):  
        bill.img_src_bill = "XBill.png" if bill.img_src_bill == "Bill.png" else "Bill.png"

    def toggle_image_charles(charles):  
        charles.img_src_charles = "XCharles.png" if charles.img_src_charles == "Charles.png" else "Charles.png"

    def toggle_image_claire(claire):  
        claire.img_src_claire = "XClaire.png" if claire.img_src_claire == "Claire.png" else "Claire.png"

    def toggle_image_david(david):  
        david.img_src_david = "XDavid.png" if david.img_src_david == "David.png" else "David.png"

    def toggle_image_eric(eric):  
        eric.img_src_eric = "XEric.png" if eric.img_src_eric == "Eric.png" else "Eric.png"

    def toggle_image_frans(frans):  
        frans.img_src_frans = "XFrans.png" if frans.img_src_frans == "Frans.png" else "Frans.png"

    def toggle_image_george(george):  
        george.img_src_george = "XGeorge.png" if george.img_src_george == "George.png" else "George.png"

    def toggle_image_herman(herman):  
        herman.img_src_herman = "XHerman.png" if herman.img_src_herman == "Herman.png" else "Herman.png"

    def toggle_image_joe(joe):  
        joe.img_src_joe = "XJoe.png" if joe.img_src_joe == "Joe.png" else "Joe.png"

    def toggle_image_maria(maria):  
        maria.img_src_maria = "XMaria.png" if maria.img_src_maria == "Maria.png" else "Maria.png"

    def toggle_image_max(max):  
        max.img_src_max = "XMax.png" if max.img_src_max == "Max.png" else "Max.png"

    def toggle_image_paul(paul):  
        paul.img_src_paul = "XPaul.png" if paul.img_src_paul == "Paul.png" else "Paul.png"

    def toggle_image_peter(peter):  
        peter.img_src_peter = "XPeter.png" if peter.img_src_peter == "Peter.png" else "Peter.png"

    def toggle_image_philip(philip):  
        philip.img_src_philip = "XPhilip.png" if philip.img_src_philip == "Philip.png" else "Philip.png"

    def toggle_image_richard(richard):  
        richard.img_src_richard = "XRichard.png" if richard.img_src_richard == "Richard.png" else "Richard.png"

    def toggle_image_robert(robert):  
        robert.img_src_robert = "XRobert.png" if robert.img_src_robert == "Robert.png" else "Robert.png"

    def toggle_image_sam(sam):  
        sam.img_src_sam = "XSam.png" if sam.img_src_sam == "Sam.png" else "Sam.png"

    def toggle_image_susan(susan):  
        susan.img_src_susan = "XSusan.png" if susan.img_src_susan == "Susan.png" else "Susan.png"

    def toggle_image_tom(tom):  
        tom.img_src_tom = "XTom.png" if tom.img_src_tom == "Tom.png" else "Tom.png"




def tablero():
    return rx.grid(
        rx.card(
            rx.box(
                "Alex",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_alex),  # Bind the image source to state
            on_click=ClassState.toggle_image_alex,  # Add the click event handler
            ),
        rx.card(
            rx.box(
                "Alfred",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_alfred),
            on_click=ClassState.toggle_image_alfred,
            ),
        rx.card(
            rx.box(
                "Anita",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_anita),
            on_click=ClassState.toggle_image_anita,
            ),
        rx.card(
            rx.box(
                "Anne",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_anne),
            on_click=ClassState.toggle_image_anne,
            ),
        rx.card(
            rx.box(
                "Bernard",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_bernard),
            on_click=ClassState.toggle_image_bernard,
            ),
        rx.card(
            rx.box(
                "Bill",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_bill),
            on_click=ClassState.toggle_image_bill,
            ),
        rx.card(
            rx.box(
                "Charles",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_charles),
            on_click=ClassState.toggle_image_charles,
            ),
        rx.card(
            rx.box(
                "Claire",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_claire),
            on_click=ClassState.toggle_image_claire,
            ),
        rx.card(
            rx.box(
                "David",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_david),
            on_click=ClassState.toggle_image_david,
            ),
        rx.card(
            rx.box(
                "Eric",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_eric),
            on_click=ClassState.toggle_image_eric,
            ),
        rx.card(
            rx.box(
                "Frans",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_frans),
            on_click=ClassState.toggle_image_frans,
            ),
        rx.card(
            rx.box(
                "George",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_george),
            on_click=ClassState.toggle_image_george,
            ),
        rx.card(
            rx.box(
                "Herman",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_herman),
            on_click=ClassState.toggle_image_herman,
            ),
        rx.card(
            rx.box(
                "Joe",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_joe),
            on_click=ClassState.toggle_image_joe,
            ),
        rx.card(
            rx.box(
                "Maria",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_maria),
            on_click=ClassState.toggle_image_maria,
            ),
        rx.card(
            rx.box(
                "Max",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_max),
            on_click=ClassState.toggle_image_max,
            ),
        rx.card(
            rx.box(
                "Paul",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_paul),
            on_click=ClassState.toggle_image_paul,
            ),
        rx.card(
            rx.box(
                "Peter",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_peter),
            on_click=ClassState.toggle_image_peter,
            ),
        rx.card(
            rx.box(
                "Philip",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_philip),
            on_click=ClassState.toggle_image_philip,
            ),
        rx.card(
            rx.box(
                "Richard",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_richard),
            on_click=ClassState.toggle_image_richard,
            ),
        rx.card(
            rx.box(
                "Robert",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_robert),
            on_click=ClassState.toggle_image_robert,
            ),
        rx.card(
            rx.box(
                "Sam",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_sam),
            on_click=ClassState.toggle_image_sam,
            ),
        rx.card(
            rx.box(
                "Susan",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_susan),
            on_click=ClassState.toggle_image_susan,
            ),
        rx.card(
            rx.box(
                "Tom",
                text_align="center",  # Centra el texto horizontalmente
            ),
            rx.image(src=ClassState.img_src_tom),
            on_click=ClassState.toggle_image_tom,
            ),

        size="20",
        columns="8",
        spacing="4",
        width="100%",
        align = "center",
    )


#def tablero():
#    return rx.grid(
#        rx.card("Alex",rx.image(src=r"Alex.png")),
#        rx.card("Alfred",rx.image(src=r"Alfred.png")),
#        rx.card("Anita",rx.image(src=r"Anita.png")),
#        rx.card("Anne",rx.image(src=r"Anne.png")),
#        rx.card("Bernard",rx.image(src=r"Bernard.png")),
#        rx.card("Bill",rx.image(src=r"Bill.png")),
#        rx.card("Charles",rx.image(src=r"Charles.png")),
#        rx.card("Claire",rx.image(src=r"Claire.png")),
#        rx.card("David",rx.image(src=r"David.png")),
#        rx.card("Eric",rx.image(src=r"Eric.png")),
#        rx.card("Frans",rx.image(src=r"Frans.png")),
#        rx.card("George",rx.image(src=r"George.png")),
#        rx.card("Herman",rx.image(src=r"Herman.png")),
#        rx.card("Joe",rx.image(src=r"Joe.png")),
#        rx.card("Maria",rx.image(src=r"Maria.png")),
#        rx.card("Max",rx.image(src=r"Max.png")),
#        rx.card("Paul",rx.image(src=r"Paul.png")),
#        rx.card("Peter",rx.image(src=r"Peter.png")),
#        rx.card("Philip",rx.image(src=r"Philip.png")),
#        rx.card("Richard",rx.image(src=r"Richard.png")),
#        rx.card("Robert",rx.image(src=r"Robert.png")),
#        rx.card("Sam",rx.image(src=r"Sam.png")),
#        rx.card("Susan",rx.image(src=r"Susan.png")),
#        rx.card("Tom",rx.image(src=r"Tom.png")),
#        
#        size="20",
#        columns="8",
#        spacing="4",
#        width="100%",
#        align = "center",
#    )

#def input() -> rx.Component:
#    return rx.hstack(
#        rx.input(placeholder="Haz una pregunta"),
#        rx.button("Enviar"),
#        align = "center",
#    )


#def indexx() -> rx.Component:
#    return rx.container(
#        chat(),
#        action_bar(),
#    )
#
def personaje():
    return rx.popover.root(
        rx.popover.trigger(
            rx.button("Respuesta"),
        ),
        rx.popover.content(
            rx.flex(
                rx.image(src=random.choice(list(Personajes.keys())) + ".png"),
                #rx.text(random.choice(list(Personajes.keys()))),
                rx.popover.close(
                    rx.button("Close"),
                ),
                direction="column",
                spacing="3",
            ),
        ),
    )

class FormInputState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def form_input1():
    return rx.card(
        rx.vstack(
            rx.heading("Hacer Preguntas"),
            rx.form.root(
                rx.hstack(
                    rx.input(
                        name="input",
                        placeholder="Escriba Pregunta",
                        type="text",
                        required=True,
                    ),
                    rx.button("Preguntar", type="submit"),
                    width="100%",
                ),
                on_submit=FormInputState.handle_submit,
                reset_on_submit=True,
            ),
            rx.divider(),
            rx.hstack(
                rx.heading("Results:"),
                rx.badge(
                    FormInputState.form_data.to_string()
                ),
            ),
            align_items="left",
            width="100%",
        ),
        width="50%",
    )





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




#def chat() -> rx.Component:
#    return rx.container(
#        rx.box(
#            "Es hombre?",
#            # The user's question is on the right.
#            text_align="right",
#        ),
#        rx.box(
#            "Si",
#            # The answer is on the left.
#            text_align="left",
#        ),
#    )




def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(question, text_align="right"),
        rx.box(answer, text_align="left"),
        margin_y="1em",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


...


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Ask a question",
            on_change=State.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_click=State.answer,
            style=style.button_style,
        ),
    )


def index() -> rx.Component:
    return rx.container(chat())



@rx.page(route="/", title="proyecto")
def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.color_mode.button(position="top-right"),
        #    tablero(),
        #    indexx(),
        #    input(),
            personaje(),
        #    form_input1(),
        #    qa(),
            chat(),
            action_bar(),
        #    index(),

        )
    )
app = rx.App()