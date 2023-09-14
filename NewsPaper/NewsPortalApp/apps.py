from django.apps import AppConfig


class NewsportalappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'NewsPortalApp'

    def ready(self):
        import NewsPortalApp.signals
