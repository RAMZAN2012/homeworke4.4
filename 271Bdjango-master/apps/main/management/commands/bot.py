from django.core.management.base import BaseCommand
from apps.main.service import bot

class Command(BaseCommand):
    help = "Bot"
    
    def handle(self, *args, **kwargs):
        print("START BOT")
        bot.polling(non_stop=True, interval=0)