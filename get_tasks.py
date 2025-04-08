import sqlite3
import sys
from pathlib import Path
from prettytable.colortable import ColorTable, Themes
    

def get_tasks():
    table = ColorTable(theme=Themes.OCEAN_DEEP)
    # gets names of .db files in current dir
    files = [f.stem for f in Path('.').iterdir() if f.is_file() and f.suffix == '.db']
    if len(files) <= 0:
        sys.exit("🆘 Error: database not found!")
    db_name = files[0]

    conn = sqlite3.connect(f'{db_name}.db')
    cursor = conn.cursor()

    tasks = cursor.execute('SELECT * FROM tasks')
    rows = tasks.fetchall()

    table.field_names = ["Date", "Chapter", "Status"]
    for row in rows:
        status = row[4]
        emoji = "⚠️"
        if status == 'pending':
            emoji = "❌"
        elif status == 'completed':
            emoji = "✅"
        table.add_row([f"{row[1]} {row[2]}", row[3], emoji])

    print(table)

    conn.commit()
    conn.close()