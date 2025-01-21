def drop_accounts_table():
    try:
        conn = sqlite3.connect('bank_account.db')
        cursor = conn.cursor()
        
        # Drop the accounts table
        cursor.execute('DROP TABLE IF EXISTS accounts')
        
        conn.commit()
        conn.close()
        print("Accounts table dropped successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")


