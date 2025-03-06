import reflex as rx

config = rx.Config(
    app_name="tcag",
    db_url="sqlite:///reflex.db",
    cors_allowed_origins=["*"],
)


