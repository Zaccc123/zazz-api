from django.apps import AppConfig


class ZazzappConfig(AppConfig):
    name = 'zazzapp'

    def ready(self):
        import zazzapp.signals
