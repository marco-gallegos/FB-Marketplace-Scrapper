import dotenv
from pathlib import Path
import os

# explicitly providing path to '.env'
# env_patah = Path('.') / '../.env'
env_path = dotenv.find_dotenv(usecwd=True)

dotenv.load_dotenv(dotenv_path=env_path,verbose=True)

HOST = os.getenv('DB_HOST') if os.getenv('DB_HOST') else 'localhost'
USER = os.getenv('DB_USER') if os.getenv('DB_USER') else 'root'
DB = os.getenv('DB_NAME') if os.getenv('DB_NAME') else'fbscrapper'
PASS = os.getenv('DB_PASSWORD') if os.getenv('DB_PASSWORD') else 'root'
ACCOUNTS = [(os.getenv('ACCOUNT_NAME'), os.getenv('ACCOUNT_PASSWORD'))]
MAIN_URL = "https://www.facebook.com"
