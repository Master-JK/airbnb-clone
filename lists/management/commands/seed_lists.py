import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists import models
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
            models.List,
            number,
            {
                "user": lambda x: random.choice(all_user),
            },
        )
        created_lists = seeder.execute()
        cleaned_lists = flatten(list(created_lists.values()))
        for pk in cleaned_lists:
            list_model = models.List.objects.get(pk=pk)
            to_add = all_room[random.randint(0, 5) : random.randint(6, 30)]
            list_model.rooms.add(*to_add)

        self.stdout.write(self.style.SUCCESS(f"{number} Lists created"))
