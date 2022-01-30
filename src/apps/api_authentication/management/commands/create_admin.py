from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = 'Create super user'

    def add_arguments(self, parser):
        parser.add_argument('-u', '--username', type=str, help="Define an admin's name.")
        parser.add_argument('-e', '--email', type=str, help="Define an admin's email.")
        parser.add_argument('-w', '--password', type=str, help="Define an admin's password.")
        parser.add_argument('-f', '--firstname', type=str, help="Define a database")
        parser.add_argument('-l', '--lastname', type=str, help="Define a database")

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        firstname = kwargs['firstname']
        lastname = kwargs['lastname']
        email = kwargs['email']
        password = kwargs.get('password', None)
        try:
            User = get_user_model()
            user = User(
                username=username,
                email=email,
                is_superuser=True,
                first_name=firstname,
                last_name=lastname,
            )
            if password:
                user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS('Good Job! The super user has been created Successfully'))
        except IntegrityError as e:
            raise CommandError('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
