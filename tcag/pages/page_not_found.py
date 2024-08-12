import reflex as rx
from tcag.components.navbar_2 import navbar_white as navbar
from tcag.components.footer import footer

hero_style = {
    "width": "100%",
    "height": "90vh",
    "backgroundImage": "url('/not-found.jpg')",
    "backgroundSize": "cover",
    "backgroundPosition": "center",
}

class State(rx.State):
    @rx.var
    def not_found_path(self) -> str:
        return "/".join(self.router.page.params.get("path", []))

@rx.page(route="/[...path]", title="404 - Page Not Found")
def page_not_found():
    return rx.vstack(
        navbar(),
        rx.box(style=hero_style),
        rx.text(f"404 - Page Not Found: /{State.not_found_path}"),
        footer(),
    )