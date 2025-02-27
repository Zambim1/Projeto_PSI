import sqlite3
import os

def conectar():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, 'usuarios.db')
    return sqlite3.connect(db_path)