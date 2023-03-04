import sys, asyncio

from NexonCareerCrawling import NexonCareerCrawling as NCC
from TelegramMessageSender import TelegramMessageSender as TMS

def main():
    """
    Nexon Crawler
    """
    # ncc = NCC()
    # ncc.StartCrawling()

    """
    Telegram Message Sender
    """
    tms = TMS()
    asyncio.run(tms.send_message("Hello"))

if __name__ == '__main__':
    main()