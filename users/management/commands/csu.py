from django.core.management.base import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):
    help = 'Создание Админа'

    def handle(self, *args, **options):
        user = CustomUser.objects.create(
            email='admin@sky.pro',
            first_name='Admin',
            last_name='Sky',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123s')
        user.save()

