import reflex as rx

config = rx.Config(
    app_name="tcag",
    db_url="sqlite:///reflex.db",
    frontend_port=3003,
    cors_allowed_origins=["*"],
)


