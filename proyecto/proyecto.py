import reflex as rx
import os





class TableroState(rx.State):
    img_src: str = "Alex.png"  # Initial image source

    def toggle_image(self):
        # Toggle the image source
        self.img_src = "XAlex.png" if self.img_src == "Alex.png" else "Alex.png"

def tablero():
    return rx.grid(
        rx.card(
            "Alex",
            rx.image(src=TableroState.img_src),  # Bind the image source to state
            on_click=TableroState.toggle_image,  # Add the click event handler
        )
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

def input() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Haz una pregunta"),
        rx.button("Enviar"),
        align = "center",
    )


def index() -> rx.Component:
    return rx.container(
        chat(),
        action_bar(),
    )

def personaje():
    return rx.popover.root(
        rx.popover.trigger(
            rx.button("Respuesta"),
        ),
        rx.popover.content(
            rx.flex(
                rx.image(src=r"Alex.png",size="20"),
                rx.popover.close(
                    rx.button("Close"),
                ),
                direction="column",
                spacing="3",
            ),
        ),
    )

@rx.page(route="/", title="proyecto")
def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.color_mode.button(position="top-right"),
            tablero(),
            input(),
            personaje(),
        )
    )
    ##a##
app = rx.App()