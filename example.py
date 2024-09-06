from oracledb_toolkit.connection import OracleConnection
from oracledb_toolkit import config

conn = OracleConnection(config.ORACLE)
connection = conn.connect_to_db()
sql = """
select view_name from all_views
"""

df = conn.execute_query(connection, sql)

print(df.head())