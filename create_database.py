# createDB.py
import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish connection to MySQL server
        # Replace with your actual MySQL credentials
        conn = mysql.connector.connect(
            host="localhost",
            user="root",        # Replace with your MySQL username
            password=""  # Replace with your MySQL password
        )
        
        if conn.is_connected():
            cursor = conn.cursor()
            
            # Create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS silozwe")
            print("Database 'silozwe' created successfully!")
            
            # Optional: Switch to the new database
            cursor.execute("USE silozwe")
            print("Switched to 'silozwe' database")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        
    finally:
        # Close database connection
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()