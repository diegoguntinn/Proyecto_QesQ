"""Welcome to Reflex! This file o"""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...

def index() -> rx.Component:


    card_contents = [
        "Contenido de la tarjeta 1",
        "Contenido de la tarjeta 2",
        "Contenido de la tarjeta 3",
        "Contenido de la tarjeta 4",
        "Contenido de la tarjeta 5",
        "Contenido de la tarjeta 6",
        "Contenido de la tarjeta 7",
        "Contenido de la tarjeta 8",
        "Contenido de la tarjeta 9",
        "Contenido de la tarjeta 10",
        "Contenido de la tarjeta 11",
        "Contenido de la tarjeta 12",
        "Contenido de la tarjeta 13",
        "Contenido de la tarjeta 14",
        "Contenido de la tarjeta 15",
        "Contenido de la tarjeta 16",
        "Contenido de la tarjeta 17",
        "Contenido de la tarjeta 18",
        "Contenido de la tarjeta 19",
        "Contenido de la tarjeta 20",
        "Contenido de la tarjeta 21",
        "Contenido de la tarjeta 22",
        "Contenido de la tarjeta 23",
        "Contenido de la tarjeta 24",]

    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.grid(
    rx.foreach(
        rx.Var.range(24),
        lambda i: rx.card(f"Persona {i + 1}", height="10vh"),
    ),
    columns="8",
    spacing="4",
    width="100%",
)
    )
    

app = rx.App()
app.add_page(index)
