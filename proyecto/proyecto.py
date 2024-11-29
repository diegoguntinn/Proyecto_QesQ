"""Welcome to Reflex! This file o"""

import reflex as rx
import os



class State(rx.State):
    """The app state."""

    ...

def index() -> rx.Component:
    # Ruta de la carpeta 'assets'
    assets_dir = os.path.join(os.path.dirname(__file__), "../assets")
    # Obtener los nombres de los archivos de imagen
    try:
        image_files = sorted([f for f in os.listdir(assets_dir) if f.endswith((".png", ".jpg", ".jpeg"))])
        print("Imágenes encontradas:", image_files)  # Agregar para depurar
    except FileNotFoundError:
        image_files = []  # Si la carpeta no existe, manejarlo adecuadamente.

    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.grid(
            rx.foreach(
                image_files,
                lambda image: rx.card(
                    rx.image(
                        src=f"{image}",  # Ruta actualizada a 'assets'
                        alt=f"Imagen de {image.split('.')[0]}",
                         width="100%",
                        height="100%",
                        object_fit="cover",
                    ),
                    rx.text(image.split(".")[0], padding="10px"),  # Nombre derivado del archivo
                    height="20vh",
                ),
            ),
            columns="8",
            spacing="4",
            width="100%",
        ),
    )


app = rx.App()
app.add_page(indexe)