import sqlite3
from datetime import datetime


DATABASE_NAME = "internet_basics.db"


def connect_database():

    return sqlite3.connect(DATABASE_NAME)


def create_tables():

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS learners (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            course_started TEXT,
            created_at TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz_attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            learner_id INTEGER,
            score INTEGER,
            total_questions INTEGER,
            percentage REAL,
            result TEXT,
            attempt_date TEXT,
            FOREIGN KEY (learner_id) REFERENCES learners(id)
        )
    """)

    connection.commit()
    connection.close()


def add_learner(name, email):

    connection = connect_database()
    cursor = connection.cursor()

    current_time = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )

    try:

        cursor.execute("""
            INSERT INTO learners
            (name, email, course_started, created_at)
            VALUES (?, ?, ?, ?)
        """, (
            name,
            email,
            current_time,
            current_time
        ))

        connection.commit()

    except sqlite3.IntegrityError:

        pass

    connection.close()


def get_learner(name, email):

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, email
        FROM learners
        WHERE name = ? AND email = ?
    """, (
        name,
        email
    ))

    learner = cursor.fetchone()

    connection.close()

    return learner


def add_quiz_attempt(
    learner_id,
    score,
    total_questions,
    percentage,
    result
):

    connection = connect_database()
    cursor = connection.cursor()

    attempt_date = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )

    cursor.execute("""
        INSERT INTO quiz_attempts
        (
            learner_id,
            score,
            total_questions,
            percentage,
            result,
            attempt_date
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        learner_id,
        score,
        total_questions,
        percentage,
        result,
        attempt_date
    ))

    connection.commit()
    connection.close()


def get_all_learners():

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.email,
            COUNT(q.id) AS attempts,
            MAX(q.percentage) AS best_percentage,
            MAX(q.score) AS best_score
        FROM learners l
        LEFT JOIN quiz_attempts q
        ON l.id = q.learner_id
        GROUP BY l.id
        ORDER BY l.id DESC
    """)

    learners = cursor.fetchall()

    connection.close()

    return learners


# Create database tables automatically

create_tables()