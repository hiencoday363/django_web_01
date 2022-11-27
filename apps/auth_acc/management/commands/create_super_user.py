from loguru import logger
from django.core.management import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create Super user'
    # create_super_user

    def handle(self, *args, **options):
        try:
            # delete all exist user
            User.objects.filter(is_staff=True).delete()
            # create new one
            User.objects.create_user(
                'admin',
                email='admin@admin.com',
                password='123456a@',
                is_staff=True,
                is_superuser=True
            )
            logger.info("-------------Successful-------------")
        except:
            logger.info("-------------Failure-------------")
