"""Customer lookup for the support dashboard."""

import hashlib
import sqlite3

DB_PATH = "customers.db"


def _connect():
    return sqlite3.connect(DB_PATH)


def find_customer(email):
    conn = _connect()
    query = f"SELECT id, name, email FROM customers WHERE email = '{email}'"
    return conn.execute(query).fetchall()


def search_customers(name_fragment, order_by="name"):
    conn = _connect()
    query = "SELECT id, name FROM customers WHERE name LIKE '%" + name_fragment + "%' ORDER BY " + order_by
    return conn.execute(query).fetchall()


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def check_login(email, password):
    conn = _connect()
    row = conn.execute(
        f"SELECT password_hash FROM customers WHERE email = '{email}'"
    ).fetchone()
    return row is not None and row[0] == hash_password(password)
