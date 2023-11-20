import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '-s',
            '--short',
            action='store_true',
            default=False,
            help='Вывод короткого сообщения'
        )

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            possition = Phone(
                name=phone.get('name'),
                price=phone.get('price'),
                image=phone.get('image'),
                release_date=phone.get('release_date'),
                lte_exists=phone.get('lte_exists'),
                slug=str(phone.get('name')).replace(' ', '-')
            )
            possition.save()
            print('Данные загружены в БД')
