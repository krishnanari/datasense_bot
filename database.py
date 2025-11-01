import mysql.connector
import datetime

def init_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="datasense"
    )
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp DATETIME NOT NULL,
        question TEXT NOT NULL,
        code TEXT NOT NULL,
        result TEXT NOT NULL
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()


def log_query(question, code, result):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="datasense"
        )
        cursor = conn.cursor()

        insert_query = """
        INSERT INTO logs (timestamp, question, code, result)
        VALUES (%s, %s, %s, %s);
        """

        cursor.execute(insert_query, (datetime.datetime.now(), question, code, result))

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        print("⚠️ Logging failed:", e)
