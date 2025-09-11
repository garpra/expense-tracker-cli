import sqlite3

def get_connection():
  conn = sqlite3.connect("expenses.db")
  conn.row_factory = sqlite3.Row
  return conn

def init_db():
  conn = get_connection()
  cursor = conn.cursor()

  cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
      id       INTEGER PRIMARY KEY AUTOINCREMENT,
      amount   REAL NOT NULL,
      category TEXT NOT NULL,
      note     TEXT,
      date     TEXT NOT NULL
    )
  """)
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS budgets (
      category  TEXT NOT NULL,
      month     TEXT NOT NULL,
      amount    REAL NOT NULL,
      PRIMARY KEY (category, month)
    )
  """)

  conn.commit()
  conn.close()