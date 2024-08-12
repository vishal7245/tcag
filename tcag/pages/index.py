import reflex as rx

from tcag.components.faq import faq_section
from tcag.components.footer import footer
from tcag.components.navbar import navbar
from tcag.components.contact import contact_section
from tcag.components.services import services_section
from tcag.components.image_gallery import image_gallery
from tcag.components.hero import hero_section
from tcag.components.testimonials import testimonials_section
from tcag.components.about_section import about_section


@rx.page(title="T-CAG Life Sciences")
def index():
    return rx.vstack(
        navbar(),
        hero_section(),
        about_section(),
        services_section(),
        faq_section(),
        testimonials_section(),
        image_gallery(),
        contact_section(),
        footer(),
        spacing="0",
    )
