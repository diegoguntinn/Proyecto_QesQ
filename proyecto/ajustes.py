import reflex as rx
import os

class State(rx.State):
    """The app state."""

    ...
@rx.page(route="/ajustes", title="ajustes")
def ajustes() -> rx.Component:
    # Ruta de la carpeta 'assets'
    
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.grid(
            rx.foreach(
                image_files,
                lambda image: rx.card(
                    rx.text(diego),  # Nombre derivado del archivo
                    height="20vh",
                ),
            ),
            columns="8",
            spacing="4",
            width="100%",
        ),
    )