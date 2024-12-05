import reflex as rx
import os





class ClassState(rx.State):
    img_src_alex: str = "Alex.png"  # Initial image source
    img_src_alfred: str = "Alfred.png"
    img_src_anita: str = "Anita.png"
    img_src_anne: str = "Anne.png"
    img_src_bernard: str = "Bernard.png"
    img_src_bill: str = "Bill.png"
    img_src_charles: str = "Charles.png"
    img_src_claire: str = "Claire.png"
    img_src_david: str = "David.png"
    img_src_eric: str = "Eric.png"
    img_src_frans: str = "Frans.png"
    img_src_george: str = "George.png"
    img_src_herman: str = "Herman.png"
    img_src_joe: str = "Joe.png"
    img_src_maria: str = "Maria.png"
    img_src_max: str = "Max.png"
    img_src_paul: str = "Paul.png"
    img_src_peter: str = "Peter.png"
    img_src_philip: str = "Philip.png"
    img_src_richard: str = "Richard.png"
    img_src_robert: str = "Robert.png"
    img_src_sam: str = "Sam.png"
    img_src_susan: str = "Susan.png"
    img_src_tom: str = "Tom.png"


    def toggle_image_alex(alex):
        # Toggle the image source
        alex.img_src_alex = "XAlex.png" if alex.img_src_alex == "Alex.png" else "Alex.png"
    
    def toggle_image_alfred(alfred):
        # Toggle the image source
        alfred.img_src_alfred = "XAlfred.png" if alfred.img_src_alfred == "Alfred.png" else "Alfred.png"

    def toggle_image_anita(anita):  
        anita.img_src_anita = "XAnita.png" if anita.img_src_anita == "Anita.png" else "Anita.png"

    def toggle_image_anne(anne):  
        anne.img_src_anne = "XAnne.png" if anne.img_src_anne == "Anne.png" else "Anne.png"

    def toggle_image_bernard(bernard):  
        bernard.img_src_bernard = "XBernard.png" if bernard.img_src_bernard == "Bernard.png" else "Bernard.png"

    def toggle_image_bill(bill):  
        bill.img_src_bill = "XBill.png" if bill.img_src_bill == "Bill.png" else "Bill.png"

    def toggle_image_charles(charles):  
        charles.img_src_charles = "XCharles.png" if charles.img_src_charles == "Charles.png" else "Charles.png"

    def toggle_image_claire(claire):  
        claire.img_src_claire = "XClaire.png" if claire.img_src_claire == "Claire.png" else "Claire.png"

    def toggle_image_david(david):  
        david.img_src_david = "XDavid.png" if david.img_src_david == "David.png" else "David.png"

    def toggle_image_eric(eric):  
        eric.img_src_eric = "XEric.png" if eric.img_src_eric == "Eric.png" else "Eric.png"

    def toggle_image_frans(frans):  
        frans.img_src_frans = "XFrans.png" if frans.img_src_frans == "Frans.png" else "Frans.png"

    def toggle_image_george(george):  
        george.img_src_george = "XGeorge.png" if george.img_src_george == "George.png" else "George.png"

    def toggle_image_herman(herman):  
        herman.img_src_herman = "XHerman.png" if herman.img_src_herman == "Herman.png" else "Herman.png"

    def toggle_image_joe(joe):  
        joe.img_src_joe = "XJoe.png" if joe.img_src_joe == "Joe.png" else "Joe.png"

    def toggle_image_maria(maria):  
        maria.img_src_maria = "XMaria.png" if maria.img_src_maria == "Maria.png" else "Maria.png"

    def toggle_image_max(max):  
        max.img_src_max = "XMax.png" if max.img_src_max == "Max.png" else "Max.png"

    def toggle_image_paul(paul):  
        paul.img_src_paul = "XPaul.png" if paul.img_src_paul == "Paul.png" else "Paul.png"

    def toggle_image_peter(peter):  
        peter.img_src_peter = "XPeter.png" if peter.img_src_peter == "Peter.png" else "Peter.png"

    def toggle_image_philip(philip):  
        philip.img_src_philip = "XPhilip.png" if philip.img_src_philip == "Philip.png" else "Philip.png"

    def toggle_image_richard(richard):  
        richard.img_src_richard = "XRichard.png" if richard.img_src_richard == "Richard.png" else "Richard.png"

    def toggle_image_robert(robert):  
        robert.img_src_robert = "XRobert.png" if robert.img_src_robert == "Robert.png" else "Robert.png"

    def toggle_image_sam(sam):  
        sam.img_src_sam = "XSam.png" if sam.img_src_sam == "Sam.png" else "Sam.png"

    def toggle_image_susan(susan):  
        susan.img_src_susan = "XSusan.png" if susan.img_src_susan == "Susan.png" else "Susan.png"

    def toggle_image_tom(tom):  
        tom.img_src_tom = "XTom.png" if tom.img_src_tom == "Tom.png" else "Tom.png"




def tablero():
    return rx.grid(
        rx.card(
            "Alex",
            rx.image(src=ClassState.img_src_alex),  # Bind the image source to state
            on_click=ClassState.toggle_image_alex,  # Add the click event handler
            ),
        rx.card(
            "Alfred",
            rx.image(src=ClassState.img_src_alfred),
            on_click=ClassState.toggle_image_alfred,
            ),
        rx.card(
            "Anita",
            rx.image(src=ClassState.img_src_anita),
            on_click=ClassState.toggle_image_anita,
            ),
        rx.card(
            "Anne",
            rx.image(src=ClassState.img_src_anne),
            on_click=ClassState.toggle_image_anne,
            ),
        rx.card(
            "Bernard",
            rx.image(src=ClassState.img_src_bernard),
            on_click=ClassState.toggle_image_bernard,
            ),
        rx.card(
            "Bill",
            rx.image(src=ClassState.img_src_bill),
            on_click=ClassState.toggle_image_bill,
            ),
        rx.card(
            "Charles",
            rx.image(src=ClassState.img_src_charles),
            on_click=ClassState.toggle_image_charles,
            ),
        rx.card(
            "Claire",
            rx.image(src=ClassState.img_src_claire),
            on_click=ClassState.toggle_image_claire,
            ),
        rx.card(
            "David",
            rx.image(src=ClassState.img_src_david),
            on_click=ClassState.toggle_image_david,
            ),
        rx.card(
            "Eric",
            rx.image(src=ClassState.img_src_eric),
            on_click=ClassState.toggle_image_eric,
            ),
        rx.card(
            "Frans",
            rx.image(src=ClassState.img_src_frans),
            on_click=ClassState.toggle_image_frans,
            ),
        rx.card(
            "George",
            rx.image(src=ClassState.img_src_george),
            on_click=ClassState.toggle_image_george,
            ),
        rx.card(
            "Herman",
            rx.image(src=ClassState.img_src_herman),
            on_click=ClassState.toggle_image_herman,
            ),
        rx.card(
            "Joe",
            rx.image(src=ClassState.img_src_joe),
            on_click=ClassState.toggle_image_joe,
            ),
        rx.card(
            "Maria",
            rx.image(src=ClassState.img_src_maria),
            on_click=ClassState.toggle_image_maria,
            ),

        rx.card(
            "Max",
            rx.image(src=ClassState.img_src_max),
            on_click=ClassState.toggle_image_max,
            ),

        rx.card(
            "Paul",
            rx.image(src=ClassState.img_src_paul),
            on_click=ClassState.toggle_image_paul,
            ),

        rx.card(
            "Peter",
            rx.image(src=ClassState.img_src_peter),
            on_click=ClassState.toggle_image_peter,
            ),

        rx.card(
            "Philip",
            rx.image(src=ClassState.img_src_philip),
            on_click=ClassState.toggle_image_philip,
            ),

        rx.card(
            "Richard",
            rx.image(src=ClassState.img_src_richard),
            on_click=ClassState.toggle_image_richard,
            ),

        rx.card(
            "Robert",
            rx.image(src=ClassState.img_src_robert),
            on_click=ClassState.toggle_image_robert,
            ),

        rx.card(
            "Sam",
            rx.image(src=ClassState.img_src_sam),
            on_click=ClassState.toggle_image_sam,
            ),

        rx.card(
            "Susan",
            rx.image(src=ClassState.img_src_susan),
            on_click=ClassState.toggle_image_susan,
            ),

        rx.card(
            "Tom",
            rx.image(src=ClassState.img_src_tom),
            on_click=ClassState.toggle_image_tom,
            ),

        size="20",
        columns="8",
        spacing="4",
        width="100%",
        align = "center",
    )


#def tablero():
#    return rx.grid(
#        rx.card("Alex",rx.image(src=r"Alex.png")),
#        rx.card("Alfred",rx.image(src=r"Alfred.png")),
#        rx.card("Anita",rx.image(src=r"Anita.png")),
#        rx.card("Anne",rx.image(src=r"Anne.png")),
#        rx.card("Bernard",rx.image(src=r"Bernard.png")),
#        rx.card("Bill",rx.image(src=r"Bill.png")),
#        rx.card("Charles",rx.image(src=r"Charles.png")),
#        rx.card("Claire",rx.image(src=r"Claire.png")),
#        rx.card("David",rx.image(src=r"David.png")),
#        rx.card("Eric",rx.image(src=r"Eric.png")),
#        rx.card("Frans",rx.image(src=r"Frans.png")),
#        rx.card("George",rx.image(src=r"George.png")),
#        rx.card("Herman",rx.image(src=r"Herman.png")),
#        rx.card("Joe",rx.image(src=r"Joe.png")),
#        rx.card("Maria",rx.image(src=r"Maria.png")),
#        rx.card("Max",rx.image(src=r"Max.png")),
#        rx.card("Paul",rx.image(src=r"Paul.png")),
#        rx.card("Peter",rx.image(src=r"Peter.png")),
#        rx.card("Philip",rx.image(src=r"Philip.png")),
#        rx.card("Richard",rx.image(src=r"Richard.png")),
#        rx.card("Robert",rx.image(src=r"Robert.png")),
#        rx.card("Sam",rx.image(src=r"Sam.png")),
#        rx.card("Susan",rx.image(src=r"Susan.png")),
#        rx.card("Tom",rx.image(src=r"Tom.png")),
#        
#        size="20",
#        columns="8",
#        spacing="4",
#        width="100%",
#        align = "center",
#    )

def input() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Haz una pregunta"),
        rx.button("Enviar"),
        align = "center",
    )


#def index() -> rx.Component:
#    return rx.container(
#        chat(),
#        action_bar(),
#    )

def personaje():
    return rx.popover.root(
        rx.popover.trigger(
            rx.button("Respuesta"),
        ),
        rx.popover.content(
            rx.flex(
                rx.image(src=r"Peter.png",size="20"),
                rx.popover.close(
                    rx.button("Close"),
                ),
                direction="column",
                spacing="3",
            ),
        ),
    )

@rx.page(route="/", title="proyecto")
def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.color_mode.button(position="top-right"),
            tablero(),
            input(),
            personaje(),
        )
    )
app = rx.App()