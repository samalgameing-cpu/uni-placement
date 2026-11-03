
import sqlite3
import hashlib
import re
from pathlib import Path

DB_PATH = Path(__file__).parent / "uniplace.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_table():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                university_email TEXT UNIQUE NOT NULL,
                student_id TEXT UNIQUE NOT NULL,
                course TEXT NOT NULL,
                semester TEXT NOT NULL,
                phone TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def register_student(full_name, email, student_id,
                     course, semester, phone, password):

    full_name = full_name.strip()
    email = email.strip().lower()
    student_id = student_id.strip().upper()
    phone = phone.strip()

    if not full_name:
        return False, "Please enter your full name."

    if not email.endswith("@semedun.in"):
        return False, "Use your university email ending in @semedun.in."

    if not re.fullmatch(r"\d{4}-B-[A-Z0-9]{9}", student_id):
        return False, "Invalid Student ID. Example: 2000-B-45982554C"

    if len(password) < 8:
        return False, "Password must contain at least 8 characters."

    password_hash = hash_password(password)

    try:
        with get_connection() as conn:
            conn.execute("""
                INSERT INTO students
                (full_name, university_email, student_id,
                 course, semester, phone, password_hash)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                full_name, email, student_id,
                course, semester, phone, password_hash
            ))

        return True, "Registration successful!"

    except sqlite3.IntegrityError:
        return False, "Email or Student ID is already registered."


def login_student(email, password):
    email = email.strip().lower()
    password_hash = hash_password(password)

    with get_connection() as conn:
        student = conn.execute("""
            SELECT id, full_name, university_email, student_id,
                   course, semester, phone
            FROM students
            WHERE university_email = ? AND password_hash = ?
        """, (email, password_hash)).fetchone()

    return student

