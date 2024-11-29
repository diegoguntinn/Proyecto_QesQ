"""Welcome to Reflex! This file o"""

import reflex as rx
import os



class State(rx.State):
    """The app state."""

    ...

def index() -> rx.Component:
    # Obtén los nombres de los archivos de imagen en la carpeta 'imagenes'.
    image_dir = os.path.join(os.path.dirname(__file__), "../assets")
    image_files = sorted([f for f in os.listdir(image_dir) if f.endswith((".png", ".jpg", ".jpeg"))])

    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.grid(
            rx.foreach(
                image_files,
                lambda image: rx.card(
                    rx.image(
                        src=f"/assets/{image}",
                        alt=f"Imagen de {image.split('.')[0]}",
                        height="100%",
                    ),
                    rx.text(
                        image.split(".")[0],
                        padding="10px",
                        ),
                    height="20vh",
                ),
            ),
            columns="8",
            spacing="4",
            width="100%",
        ),
    )


app = rx.App()
app.add_page(index)