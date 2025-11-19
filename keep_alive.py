from sqlitecloud import SQLiteCloudConnection
import datetime

DB_URL = 'sqlitecloud://cz1dyazrhz.g4.sqlite.cloud:8860/auth.sqlitecloud?apikey=oHye0DO2njToIUEmIefnu3MJnPnUb4I7ZBOFJXuUhjw'

def mantener_viva():
    try:
        conn = SQLiteCloudConnection(DB_URL)
        cur = conn.cursor()

        # Crear tabla si no existe
        cur.execute("""
            CREATE TABLE IF NOT EXISTS time_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                time TEXT NOT NULL
            );
        """)

        # Insertar registro
        now = datetime.datetime.now().isoformat(sep=' ', timespec='seconds')
        cur.execute("INSERT INTO time_log (time) VALUES (?);", (now,))
        conn.commit()

        print(f"[{now}] 🕒 Registro insertado y conexión viva.")

    except Exception as e:
        print("❌ Error:", e)

    finally:
        try:
            conn.close()
        except:
            pass

if __name__ == "__main__":
    mantener_viva()
