import oracledb
from src import logger, config
import pandas as pd

class OracleConnection():

    def __init__(self, config):
        self.config = config
        # TODO: Hide the password if printing the config
        self.logger = logger.setup_logging("OracleConnection")

    def connect_to_db(self) -> oracledb.Connection:
        """
        Connect to the Oracle database
        """
        try:
            self.logger.info("Initializing Oracle client library")
            oracledb.init_oracle_client(lib_dir = self.config["oracle_client_path"])

            self.logger.info("Creating connection object")
            connection = oracledb.connect(
                user = self.config["username"],
                password = self.config["password"],
                host = self.config["host"],
                port = self.config["port"],
                service_name = self.config["service_name"]
            )

            self.logger.info("Connection established")
            return connection

        except oracledb.DatabaseError as e:
            error, = e.args
            if error.code == 1017:
                self.logger.error("Authentication error. Please check your credentials.")
            else:
                self.logger.error(f"Database connection error: {error}")
            exit(1)

    def execute_query(self, connection: oracledb.Connection, sql: str) -> pd.DataFrame:
        """
        Execute a sql query over the connection
        """

        cursor = connection.cursor()
        self.logger.info("Executing query...")
        try:
            cursor.execute(sql)
            cols = [col[0] for col in cursor.description]
            data = cursor.fetchall()
            cursor.close()

            self.logger.info("Query executed successfully")
            self.logger.info("Converting to DataFrame...")
            df = pd.DataFrame(data, columns=cols)

            return df
        
        except oracledb.DatabaseError as e:
            error, = e.args
            self.logger.error(f"Error executing query: {error}")
            exit(1)
        
        except Exception as e:
            self.logger.error(f"Error executing query: {e}")
            exit(1)
