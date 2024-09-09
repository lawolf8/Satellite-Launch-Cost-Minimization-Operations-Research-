import os, sys
import Optional
import pyodbc
import pandas as pd

class server:
    def __init__(self) -> None:
        user = os.getenv("USERNAME", "Default")
        password = os.getenv("SQL_PASSWORD")
        self.server_connection(user, password)
    def server_connection(self, user=str, password=str) -> Optional[str]:
        SERVER = os.getenv("SAT_SERVER")
        DATABASE = os.getenv("SAT_DB")
        USERNAME = user
        PASSWORD = password
        connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
        conn = pyodbc.connect(connectionString)
        return conn
    def data_query(self, data) -> Optional[pd.DataFrame]:
        import launch_data as launch
        data = launch.data_main.main()
        
    def dataupload(self, data, conn) -> bool:
        cursor = conn.cursor()
        cursor.execute(SQL_QUERY)