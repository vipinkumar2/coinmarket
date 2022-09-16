from django.core.management.base import BaseCommand
from CMC.settings import LOGGER
from home.bot import coinmarket
from home.models import user_details

class Command(BaseCommand):
    def __init__(self) -> None:
        self.logger = LOGGER


    def handle(self, *args, **kwargs):
        self.logger.info('Script started to sign up a new account')
        while True:
            # try:
                if len(user_details.objects.all()) == 0:
                    cmc_bot = coinmarket(profile_dir=int(1),hide_browser=False)
                else:
                    last_user = user_details.objects.last()
                    new_user_profile_dir = last_user.profile_name + 1
                    cmc_bot = coinmarket(profile_dir=int(new_user_profile_dir),hide_browser=False)
                cmc_bot.sign_up()
                cmc_bot.quite_driver()
            # except Exception as e: 
            #     print(e)