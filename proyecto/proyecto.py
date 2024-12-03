# import reflex as rx
#i mport os
#
#class State(rx.State):
#    """The app state."""
#
#
#@rx.page(route="/", title="proyecto")
#
#def index() -> rx.Component:
#    
#    assets_dir = os.path.join(os.path.dirname(__file__), "../assets/")
#    try:
#        image_files = sorted([f for f in os.listdir(assets_dir) if f.endswith((".png", ".jpg", ".jpeg"))])
#        print("Imágenes encontradas:", image_files)
#    except FileNotFoundError:
#        image_files = []
#    
#    image_files = sorted([foto for foto in os.listdir(assets_dir)])
#    
#
#    return rx.container(
#        rx.color_mode.button(position="top-right"),
#        rx.grid(
#            rx.foreach(
#                image_files,
#                lambda image: rx.card(
#                    rx.image(
#                        src=f"{image}",
#                    #    alt=f"Imagen de {image.split('.')[0]}",
#                        width="100%",
#                        height="100%",
#                        object_fit="cover",
#                    ),
#                ),
#            ),
#            columns="8",
#            spacing="4",
#            width="100%",
#        ),
#    )
#
#
#app = rx.App()

import reflex as rx
import os

class State(rx.State):
    """The app state."""

    ...
@rx.page(route="/tablero", title="tablero")
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
                        src="assets/Tom.png",  # Ruta actualizada a 'assets'
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
app.add_page(index)