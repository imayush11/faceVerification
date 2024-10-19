import mysql.connector
import os
from mysql.connector import errorcode
from dotenv import load_dotenv

load_dotenv()

def create_user_table():
    # Connect to the database
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),        # Your database host
            user=os.getenv("DB_USERNAME"),    # Your database username
            password=os.getenv("DB_PASSWORD"), # Your database password
            database=os.getenv("DB_NAME")  # Your database name
        )
        cursor = conn.cursor()

        # Check if the 'user' table exists
        cursor.execute("""
            SELECT COUNT(*)
            FROM information_schema.tables 
            WHERE table_name = 'user';
        """)
        if cursor.fetchone()[0] == 0:
            # Table does not exist, create it
            create_table_query = """
            CREATE TABLE user (
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                user_name TEXT NOT NULL,
                face_image LONGBLOB
            );
            """
            cursor.execute(create_table_query)
            print("Table 'user' created successfully.")
        else:
            print("Table 'user' already exists.")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied: check your username and password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        cursor.close()
        conn.close()

create_user_table()
