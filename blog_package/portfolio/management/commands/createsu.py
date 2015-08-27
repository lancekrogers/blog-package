from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="blogadmin").exists():
            User.objects.create_superuser("blogadmin", "blog@blog.com", "blogadmin")
        else:
            print('admin user already exist')