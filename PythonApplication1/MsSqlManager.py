import pyodbc
import asyncio

from IniFileParser import IniFileParser as Config

class MsSqlManager:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = MsSqlManager()
        return cls._instance

    def __init__(self):
        # Set up the connection details
        self.server = Config.get_instance().sql_server_name
        self.database = Config.get_instance().sql_db_name
        self.username = Config.get_instance().sql_user_name
        self.password = Config.get_instance().sql_password

    def SetTable(self, name):
        self.cursor = self.conn.cursor()

        if not self.cursor.tables(table=name).fetchone():
            self.cursor.execute(f'''
                CREATE TABLE {name} (
                    id INT PRIMARY KEY,
                    name    VARCHAR(50),
                    value   VARCHAR(50),
                )
            ''')
            self.conn.commit()
        self.table = name

    async def connectDB(self):
        # Connect to the database
        conn_str = (
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={self.server};'
            f'DATABASE={self.database};'
            f'UID={self.username};'
            f'PWD={self.password}'
        )
        loop = asyncio.get_event_loop()

        try:
            self.conn = await loop.run_in_executor(None, pyodbc.connect, conn_str)
        except pyodbc.Error as e:
            print(f'Error connecting to database: {e}')

    def ShowAllTables(self):
        self.cursor.execute(f'SELECT name FROM sys.tables')
        rows = self.cursor.fetchall()
        
        # Print the results
        for row in rows:
            print(row[0])

    def CloseConnection(self):
        self.conn.close()