import telegram
from IniFileParser import IniFileParser as Config

class TelegramMessageSender:
    async def send_message(self, text):
        TOKEN = Config.get_instance().telegram_token
        bot = telegram.Bot(token=TOKEN)
        chat_id = Config.get_instance().telegram_chat_id
        await bot.send_message(chat_id=chat_id, text=text)