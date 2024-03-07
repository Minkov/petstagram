from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "petstagram.accounts"

    def ready(self):
        import petstagram.accounts.signals
