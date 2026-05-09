from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.conf import settings


class Command(BaseCommand):
    help = "Create a Django app with custom structure inside backend/apps"

    def add_arguments(self, parser):
        parser.add_argument("app_name", type=str)

    def handle(self, *args, **options):
        app_name = options["app_name"]

        base_dir = Path(settings.BASE_DIR)
        apps_dir = base_dir / "apps"
        app_dir = apps_dir / app_name
        template_dir = base_dir / "templates" / "app_template"

        apps_dir.mkdir(exist_ok=True)

        if app_dir.exists():
            raise CommandError(f"App '{app_name}' already exists")

        app_dir.mkdir()

        call_command(
            "startapp",
            app_name,
            str(app_dir),
            template=str(template_dir),
        )

        self.stdout.write(
            self.style.SUCCESS(f"✔ App '{app_name}' created with custom template")
        )