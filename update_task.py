import sqlite3
import sys
from pathlib import Path

def update_task():
    # gets names of .db files in current dir
    files = [f.stem for f in Path('.').iterdir() if f.is_file() and f.suffix == '.db']
    if len(files) <= 0:
        sys.exit("🆘 Error: database not found!")
    db_name = files[0]

    conn = sqlite3.connect(f'{db_name}.db')
    cursor = conn.cursor()

    searched_date = input("Enter date to update: ")
    try:
        searched_date = searched_date.split(" ")
    except:
        sys.exit("🆘 Error: enter a valid date!")
    date = searched_date[0]
    month = searched_date[1]

    is_done = input("Is the task done or not? (y/n): ")

    if is_done == "y":
        # here ? is a placeholder
        cursor.execute("""
        UPDATE tasks
        SET status = 'completed'
        WHERE date = ? AND month = ?;
        """, (date, month))
    elif is_done == "n":
        cursor.execute("""
        UPDATE tasks
        SET status = 'pending'
        WHERE date = ? AND month = ?;
        """, (date, month))

    conn.commit()
    conn.close()