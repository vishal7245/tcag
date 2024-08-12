import reflex as rx


from tcag.components.footer import footer
from tcag.components.navbar_2 import navbar_white as navbar
from tcag.components.banner import banner
from tcag.components.rss_feed import news_section


@rx.page(route="/news", title="News and Updates")
def news_and_updates():
    return rx.vstack(
        navbar(),
        banner("News and Updates"),
        news_section(),
        footer(),
    )





    