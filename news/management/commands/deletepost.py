from django.core.management.base import BaseCommand, CommandError
from news.models import Post


class Command(BaseCommand):
    help = 'Удаление из модели Post'
    requires_migrations_checks = True

    def handle(self, *args, **options):
        self.stdout.readable()
        self.stdout.write('Do you want to delete all Post? yes/no')
        answer = input()

        if answer == 'yes':
            Post.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Succesfully wiped Post'))
            return

        self.stdout.write(self.style.ERROR('Access denied'))
