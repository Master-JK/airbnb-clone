import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from reviews import models
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command create many reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many time do you want to create"
        )

    def handle(self, *args, **options):
        all_user = user_models.User.objects.all()
        all_room = room_models.Room.objects.all()

        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(
            models.Review,
            number,
            {
                "accuracy": lambda x: random.randint(0, 6),
                "communication": lambda x: random.randint(0, 6),
                "cleaniness": lambda x: random.randint(0, 6),
                "location": lambda x: random.randint(0, 6),
                "check_in": lambda x: random.randint(0, 6),
                "value": lambda x: random.randint(0, 6),
                "user": lambda x: random.choice(all_user),
                "room": lambda x: random.choice(all_room),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} Reviews created"))
