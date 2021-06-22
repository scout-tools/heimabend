from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User


class Command(BaseCommand):
    help = 'add users'

    def handle(self, *args, **options):
        UserModel = get_user_model()

        if not UserModel.objects.filter(username='Robert').exists():
            user = UserModel.objects.create_user(
                'Robert', password='robert')
            user.is_superuser = True
            user.is_staff = True
            user.save()

        if not UserModel.objects.filter(username='Hagi').exists():
            user = UserModel.objects.create_user(
                'Hagi', password='hagi')
            user.is_superuser = False
            user.is_staff = True
            user.save()

        if not UserModel.objects.filter(username='Sheldon').exists():
            user = UserModel.objects.create_user(
                'Sheldon', password='sheldon')
            user.is_superuser = False
            user.is_staff = True
            user.save()

        if not UserModel.objects.filter(username='Resi').exists():
            user = UserModel.objects.create_user(
                'Resi', password='resi')
            user.is_superuser = False
            user.is_staff = True
            user.save()

        if not UserModel.objects.filter(username='Emelle').exists():
            user = UserModel.objects.create_user(
                'Emelle', password='emelle')
            user.is_superuser = False
            user.is_staff = True
            user.save()

        if not UserModel.objects.filter(username='Nadine').exists():
            user = UserModel.objects.create_user(
                'Nadine', password='nadine')
            user.is_superuser = False
            user.is_staff = True
            user.save()

        print('user created')
