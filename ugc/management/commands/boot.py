from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot
import telebot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.utils.request import Request


def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'Произошла ошибка: {e}'
            print(error_message)
            raise e
    return inner


bot = telebot.TeleBot(settings.TOKEN)
@log_errors
class Command(BaseCommand):
    help = 'Telegram-bot'

    def handle(self, *args, **options):
        @bot.message_handler(commands=['start'])
        def start_message(message):
            bot.send_message(message.chat.id, 'В какой группе вы учитесь?')