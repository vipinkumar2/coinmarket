from multiprocessing.util import LOGGER_NAME
from django.core.management.base import BaseCommand
from home.bot import coinmarket
from CMC.settings import LOGGER
from home.models import user_details


class Command(BaseCommand):
    def __init__(self) -> None:
        self.logger = LOGGER


    def handle(self, *args, **kwargs):
        self.logger.info('Script started to profile update !')
        for user in  user_details.objects.filter(profile_updated = False):
            coinmarket_bot = coinmarket(profile_dir=user.profile_name,hide_browser=False)
            coinmarket_bot.login()
            coinmarket_bot.profile_update()
            input('Enter to close the driver :')
            coinmarket_bot.quite_driver()
        ...