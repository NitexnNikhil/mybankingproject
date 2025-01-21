# import sqlite3
# conn = sqlite3.connect('bank_account.db')
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM accounts")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
# conn.close()


'''check the table creation'''
# import sqlite3

# conn = sqlite3.connect('bank_account.db')
# cursor = conn.cursor()
# cursor.execute("PRAGMA table_info(accounts)")
# print(cursor.fetchall())
# conn.close()




''' Test the Insert Query Independently'''
# import sqlite3

# DATABASE = 'bank_account.db'

# def test_insert():
#     try:
#         conn = sqlite3.connect(DATABASE)
#         cursor = conn.cursor()
#         cursor.execute('''
#             INSERT INTO accounts (name, email, phone, address, password)
#             VALUES (?, ?, ?, ?, ?)
#         ''', ('Test User', 'test@example.com', '1234567890', 'Test Address', 'password123'))
#         conn.commit()
#         print("Insert successful")
#         conn.close()
#     except Exception as e:
#         print(f"Error: {e}")
# test_insert()



# '''Change SQLite Locking Behavior (Optional)'''
# import sqlite3
# conn = sqlite3.connect("'bank_account.db'")
# cursor = conn.cursor()
# cursor.execute("PRAGMA journal_mode=DELETE;")
# conn.commit()
# conn.close()
