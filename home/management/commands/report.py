from platform import java_ver
from django.core.management.base import BaseCommand
from CMC.settings import LOGGER
from home.bot import coinmarket
from home.models import comments, user_details
import datetime, requests
from django.db.models import Sum


date_from = datetime.datetime.now() - datetime.timedelta(days=1)
class Command(BaseCommand):
    def __init__(self) -> None:
        self.logger = LOGGER


    def handle(self, *args, **kwargs):
        for user in user_details.objects.filter(status = "ACTIVE"):
            user.total_commented += 1
            user.save()
        self.logger.info('report script has been started !')

        total_account = user_details.objects.filter(status = "ACTIVE").count()
        total_account_created_24hours = user_details.objects.filter(status = "ACTIVE",created_at__gte=date_from).count()
        updated_account = user_details.objects.filter(profile_updated = True).count()
        updated_account_24hours = user_details.objects.filter(profile_updated = True,created_at__gte=date_from).count()
        total_comment = user_details.objects.aggregate(Sum('total_commented'))['total_commented__sum']
        total_comment_24hours = comments.objects.filter(created_at__gte=date_from).count()
        total_banned_account = user_details.objects.filter(status = "BANNED").count()
        banned_account_24hours = user_details.objects.filter(status = "BANNED",created_at__gte=date_from).count()
        print(total_comment)

        report = [
            f'Total accounts : {total_account}',
            f'Total updated accounts : {updated_account}',
            f'Total send comments : {total_comment}',
            f'Total banned user : {total_banned_account}',
            f'Total accounts created in last 24 hours  : {total_account_created_24hours}',
            f'Total updated accounts in last 24 hours : {updated_account_24hours}',
            f'Total send comments in last 24 hours : {total_comment_24hours}',
            f'Total banned user in last 24 hours : {banned_account_24hours}',
        ]
        text = ""
        text += "*" * 50+'\n'
        text += f"\t\tTelegram Account status\nTime : {datetime.datetime.now()}"+'\n'
        text += "*" * 50+'\n'
        for i in report: 
            text+= f"{i}"
            text+="\n"
        text += "*" * 50+'\n'
        print(text)

        if text:
            payload = {"text":text}
            print(payload)
            r = requests.post(WEB_HOOK_URL, json=payload)
            # LOGGER.info(f"WEB HOOK Post Response: {r.text}")
            # LOGGER.info(r.text)
WEB_HOOK_URL = "https://hooks.slack.com/services/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"
