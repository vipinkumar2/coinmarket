from driver.driver import get_driver
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        driver = get_driver('115')

        driver.get('https://www.youtube.com/')
        # input('Enter "')
        driver.quit()