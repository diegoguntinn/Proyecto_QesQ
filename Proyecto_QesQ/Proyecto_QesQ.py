import reflex as rx

from rxconfig import config

class State(rx.State):
    """The app state."""

    ...

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
     )

app = rx.App()
app.add_page(index)
