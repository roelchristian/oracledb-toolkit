from dotenv import load_dotenv
import os
load_dotenv()

ORACLE = {
    'username' : os.getenv('ORACLE_USERNAME'),
    'password' : os.getenv('PASSWORD'),
    'host' : os.getenv('HOST'),
    'port' : os.getenv('PORT'),
    'service_name' : os.getenv('SERVICE_NAME'),
    'oracle_client_path' : os.getenv('ORACLE_CLIENT_PATH')
}

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))