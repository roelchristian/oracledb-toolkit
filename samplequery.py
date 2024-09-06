from src import logger, config
from src.connection import OracleConnection
import os

logger = logger.setup_logging(__name__)
file_path = os.path.abspath(__file__)

logger.info(f"Running {file_path}...")

oracle = OracleConnection(config.ORACLE)
sql = "select * from table"

# Create a connection using OracleConnection.connect_to_db()
connection = oracle.connect_to_db()

# Execute query and get results as dataframe
df = oracle.execute_query(connection, sql)

print(df.head())