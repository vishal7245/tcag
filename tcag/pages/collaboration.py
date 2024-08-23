import reflex as rx


from tcag.components.footer import footer
from tcag.components.navbar_2 import navbar_white as navbar
from tcag.components.banner import banner

list_style = {
    "font-size": "1.4rem",
    "color": "gray",
    "margin-bottom": "1rem",
    "text-align": "justify",
}

@rx.page(route="/collaborations", title="Collaborations")
def collaboration():
    return rx.vstack(
        navbar(),
        banner("Collaborations"),
        rx.section(
            rx.vstack(
                rx.heading(
                    "Latest Collaborations",
                    size="7",
                    margin_top="2rem",
                    margin_bottom="1rem",
                    color="teal",
                    font_weight="bold",
                ),
                rx.list.unordered(
                    rx.list.item(rx.text("We are in collaboration with ARTEMIS Hospital and have signed an MoU for advanced healthcare initiatives.", style=list_style), color="black"),
                    rx.list.item(rx.text("We have partnered with ARTEMIS Hospital and signed a Memorandum of Understanding (MoU) to pursue advanced healthcare initiatives.", style=list_style), color="black"),
                    rx.list.item(rx.text("We are in collaboration with the Institute of Liver and Biliary Sciences and have signed an MoU for specialized research and treatment.", style=list_style), color="black"),
                    rx.list.item(rx.text("We are in collaboration with Genomic Valley Bharat Pvt. Ltd. and have signed an MoU for genomic research and development.", style=list_style), color="black"),
                ),
                width="100%",
                align_items="center",
                margin_x="auto",
                max_width="800px",
            ),
            width="100%",
            margin_bottom="200px"
        ),
        footer(),
        width="100%",
        align_items="center",
    )
    
