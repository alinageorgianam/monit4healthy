from django.apps import AppConfig


class M4HConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'm4h'

    def ready(self):
        import m4h.signals  # Importă semnalele