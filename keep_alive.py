import sqlite3
import datetime

DB_URL = 'sqlitecloud://cz1dyazrhz.g4.sqlite.cloud:8860/auth.sqlitecloud?apikey=oHye0DO2njToIUEmIefnu3MJnPnUb4I7ZBOFJXuUhjw'

def mantener_viva():
    conn = None  # ✅ Evita warning de Pylance
    try:
        conn = sqlite3.connect(DB_URL, uri=True)
        cur = conn.cursor()

        # Crear tabla si no existe
        cur.execute("""
            CREATE TABLE IF NOT EXISTS time_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                time TEXT NOT NULL
            );
        """)

        # Verificar conexión
        cur.execute("SELECT 1;")
        print(f"[{datetime.datetime.now()}] ✅ Ping OK: {cur.fetchone()}")

        # Insertar registro con fecha actual
        now = datetime.datetime.now().isoformat(sep=' ', timespec='seconds')
        cur.execute("INSERT INTO time_log (time) VALUES (?);", (now,))
        conn.commit()

        print(f"[{now}] 🕒 Registro insertado en time_log.")

    except Exception as e:
        print(f"[{datetime.datetime.now()}] ❌ Error: {e}")

    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    mantener_viva()
# keep_alive.py