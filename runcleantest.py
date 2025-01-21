import sqlite3

DATABASE = 'bank_account.db'

try:
    conn = sqlite3.connect(DATABASE, timeout=10)  # Add timeout to handle locks
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT UNIQUE NOT NULL,
            address TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    print("Table created or already exists.")

    # Test insertion
    cursor.execute('''
        INSERT INTO accounts (name, email, phone, address, password)
        VALUES (?, ?, ?, ?, ?)
    ''', ('Test User', 'test@example.com', '1234567890', 'Test Address', 'password123'))
    conn.commit()
    print("Insert successful.")
except sqlite3.OperationalError as e:
    print(f"Database operational error: {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    if conn:
        conn.close()
