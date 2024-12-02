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
                    rx.image(src=f"/assets/{image}", alt=f"Imagen de {image.split('.')[0]}", height="100%"),
                    rx.text(image.split(".")[0], padding="10px"),
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