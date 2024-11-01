import mysql.connector as ms
from tkinter import messagebox

def connect_db():
    try:
        con = ms.connect(
            host="localhost",   # Update with your MySQL host
            user="root",        # Update with your MySQL username
            password="janani",  # Update with your MySQL password
            database="library_db"  # Update with your MySQL database
        )
        return con
    except ms.Error as err:
        messagebox.showinfo('Error', f"Error connecting to the database: {err}")
        return None

