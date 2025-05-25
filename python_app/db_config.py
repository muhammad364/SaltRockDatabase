import mysql.connector
from mysql.connector import Error

def get_connection():
    """
    Establishes and returns a MySQL database connection.
    Update host, user, password as needed for your setup.
    """
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='SaltRock',
            user='root',          
            password='harry1710'
        )
        return conn
    except Error as e:
        print(f"[Error] Could not connect to database: {e}")
        return None

def close_connection(conn):
    """Closes the database connection cleanly."""
    if conn and conn.is_connected():
        conn.close()
