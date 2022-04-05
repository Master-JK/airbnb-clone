from datetime import datetime, timedelta
import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from reservations import models
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command create many lists"

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
            models.Reservation,
            number,
            {
                "status": lambda x: random.choice(["pending", "confirmed", "canceled"]),
                "guest": lambda x: random.choice(all_user),
                "room": lambda x: random.choice(all_room),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(3, 25)),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} Converstations created"))
