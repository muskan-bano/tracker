
import sqlite3
import pandas as pd

def get_db_path():
    import os
    from pathlib import Path
    if os.path.exists('/mount/data'):
        Path('/mount/data').mkdir(exist_ok=True)
        return '/mount/data/expense_tracker.db'
    else:
        return 'expense_tracker.db'

def get_transactions(user_id):
    conn = sqlite3.connect(get_db_path())
    df = pd.read_sql_query("SELECT * FROM transactions WHERE user_id = ?", conn, params=(user_id,))
    conn.close()
    return df

def get_budget(user_id):
    conn = sqlite3.connect(get_db_path())
    cur = conn.cursor()
    cur.execute("SELECT amount FROM budgets WHERE user_id = ?", (user_id,))
    result = cur.fetchone()
    conn.close()
    return result[0] if result else 0
