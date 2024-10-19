import os
import mysql
from dotenv import load_dotenv

load_dotenv()


def create_connection():
    # Connect to the database
    return mysql.connector.connect(
            host=os.getenv("DB_HOST"),        # Your database host
            user=os.getenv("DB_USERNAME"),    # Your database username
            password=os.getenv("DB_PASSWORD"), # Your database password
            database=os.getenv("DB_NAME")  # Your database name
        )