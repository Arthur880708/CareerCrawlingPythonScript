import configparser

class IniFileParser:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self._telegram_token = config['telegram']['token']
        self._telegram_chat_id = config['telegram']['chat_id']

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = IniFileParser()
        return cls._instance

    @property
    def telegram_token(self):
        return str(self._telegram_token)

    @telegram_token.setter
    def telegram_token(self, value):
        self._telegram_token = value

    @property
    def telegram_chat_id(self):
        return str(self._telegram_chat_id)

    @telegram_chat_id.setter
    def telegram_chat_id(self, value):
        self._telegram_chat_id = value
