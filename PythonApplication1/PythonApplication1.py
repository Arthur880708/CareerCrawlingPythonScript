import sys, asyncio

from NexonCareerCrawling import NexonCareerCrawling as NCC
from TelegramMessageSender import TelegramMessageSender as TMS
from MsSqlManager import MsSqlManager as MsSQL

def main():
    """
    Nexon Crawler
    """
    # ncc = NCC()
    # ncc.StartCrawling()

    """
    Telegram Message Sender
    """
    # tms = TMS()
    # asyncio.run(tms.send_message("Hello"))

    """
    MS-SQL Manager
    """
    asyncio.run(MsSQL.get_instance().connectDB())
    MsSQL.get_instance().SetTable("TEST")
    MsSQL.get_instance().ShowAllTables()
    MsSQL.get_instance().CloseConnection()

if __name__ == '__main__':
    main()