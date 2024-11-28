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
        
    ]

    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.grid(
            rx.foreach(
                rx.Var.range(24),  # Crea 24 tarjetas
                lambda i: rx.card(
                    # Aquí personalizamos el contenido de cada tarjeta
                    f"Card {i + 1}",
                    height="10vh",
                    children=[
                        rx.text(card_contents[i % len(card_contents)])  # Modifica el contenido de cada tarjeta
                    ]
                ),
            ),
            columns="8",
            spacing="4",
            width="100%",
        )
    )


app = rx.App()
app.add_page(index)
