import sqlite3

def create_db():
  db_name = input("\n📦 What should the database be called? ")
  conn = sqlite3.connect(f'{db_name}.db')
  cursor = conn.cursor()
  
  cursor.execute("""
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date INTEGER,
    month TEXT,
    chapter TEXT,
    status TEXT
  );
  """)

  print("\n✅ Database and tasks table created successfully.")

  cursor.execute("""
  INSERT INTO tasks (date, month, chapter, status) VALUES
  (8, "April", 'Chapter 1', 'pending'),
  (9, "April", 'Chapter 2', 'completed'),
  (10, "April", 'Chapter 3', 'in progress'),
  (11, "April", 'Chapter 4', 'pending');
  """)

  print("\n✅ Data inserted into database successfully.\n")

  conn.commit()
  conn.close()