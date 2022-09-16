from django.core.management.base import BaseCommand
from CMC.settings import LOGGER
from home.bot import coinmarket
from home.models import user_details

class Command(BaseCommand):
    def __init__(self) -> None:
        self.logger = LOGGER


    def handle(self, *args, **kwargs):
        self.logger.info('Script started to login created account')

        for user in user_details.objects.filter(status = "ACTIVE"):
            
            cmc_bot = coinmarket(profile_dir=int(user.profile_name),hide_browser=False)
            cmc_bot.login()
            cmc_bot.comment_on_xana()
            input('Enter :')
            cmc_bot.quite_driver()


        