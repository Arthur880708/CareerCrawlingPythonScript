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

        # telegram info
        self._telegram_token = config['telegram']['token']
        self._telegram_chat_id = config['telegram']['chat_id']

        # ms sql info
        self._sql_server_name = config['ms_sql']['server_name']
        self._sql_db_name = config['ms_sql']['db_name']
        self._sql_user_name = config['ms_sql']['user_name']
        self._sql_password = config['ms_sql']['password']

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = IniFileParser()
        return cls._instance


    # telegram info
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



    # ms-sql info
    @property
    def sql_server_name(self):
        return str(self._sql_server_name)

    @sql_server_name.setter
    def sql_server_name(self, value):
        self._sql_server_name = value

    @property
    def sql_db_name(self):
        return str(self._sql_db_name)

    @sql_db_name.setter
    def sql_db_name(self, value):
        self._sql_db_name = value

    @property
    def sql_user_name(self):
        return str(self._sql_user_name)

    @sql_user_name.setter
    def sql_user_name(self, value):
        self._sql_user_name = value

    @property
    def sql_password(self):
        return str(self._sql_password)

    @sql_password.setter
    def sql_password(self, value):
        self._sql_password = value