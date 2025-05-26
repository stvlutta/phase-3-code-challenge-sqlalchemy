#!/usr/bin/env python3
import os
import sqlite3

# Get the parent directory of this script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA_PATH = os.path.join(BASE_DIR, 'lib', 'db', 'schema.sql')
DB_PATH = os.path.join(BASE_DIR, 'articles.db')

def setup_database():
    """Set up the database by executing the schema SQL file"""
    print(f"Setting up database at {DB_PATH}")
    
    # Remove existing database if it exists
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"Removed existing database at {DB_PATH}")
    
    # Create a new database connection
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Read and execute the schema SQL
    with open(SCHEMA_PATH, 'r') as f:
        schema_sql = f.read()
        cursor.executescript(schema_sql)
    
    conn.commit()
    conn.close()
    
    print("Database setup complete!")

if __name__ == "__main__":
    setup_database()