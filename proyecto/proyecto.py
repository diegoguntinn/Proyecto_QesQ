import reflex as rx
import os

class State(rx.State):
    """The app state."""

    ...
def cuadricula():
    return rx.link(
        rx.button("Jugar"),
        href="/tablero",
        external="False",
    )

@rx.page(route="/", title="proyecto")
def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("¿quien es quien?", size="9"),
            cuadricula(),
            spacing="5",
            justify="center",
            min_height="85v",
        ),
        rx.logo(),
    )

app = rx.App()