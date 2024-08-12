import reflex as rx


from tcag.components.footer import footer
from tcag.components.navbar_2 import navbar_white as navbar
from tcag.components.contact import contact_section
from tcag.components.banner import banner


@rx.page(route="/contact", title="Contact Us")
def contact_page():
    return rx.vstack(
        navbar(),
        banner("Contact Us"),
        contact_section(),
        footer(),
    )
