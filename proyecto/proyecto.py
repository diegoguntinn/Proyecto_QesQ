"""Welcome to Reflex! This file o"""

import reflex as rx
import os



class State(rx.State):
    """The app state."""

    ...
def tablero():
    return rx.link(
        rx.button("Jugar"),
        href="/tablero",
        external="False",
        )

@rx.page(route="/", title="tablero")
def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("¿quien es quien?", size="9"),
            tablero(),
            spacing="5",
            justify="center",
            min_height="85v",
            #rx.text("¿Quién", font_size="120px", font_weight="bold", margin="10px 0 0 0"),
            #rx.text("es", font_size="110px", font_weight="bold", margin="20px 0 0 20px"),
            #rx.text("Quién?", font_size="100px", font_weight="bold", margin="30px 0 0 40px"),
        #direction="column",  # Organizar en columna
        #align="flex-start",  # Alinear al inicio de la columna
        #justify="flex-start",  # Justificar al inicio verticalmente
        #height="100vh",  # Altura completa de la pantalla
        #width="100%",  # Ancho completo
        ),
        rx.logo(),
    )
app = rx.App()
app.add_page(index)