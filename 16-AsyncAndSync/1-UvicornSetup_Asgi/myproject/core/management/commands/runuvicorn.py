from django.core.management.base import BaseCommand
import uvicorn

class Command(BaseCommand):
    help = "Run the django app with uvicorn"
    def handle(self, *args, **options):
        uvicorn.run("myproject.asgi:application", host = "127.0.0.1", port = 8000, reload = True)

        