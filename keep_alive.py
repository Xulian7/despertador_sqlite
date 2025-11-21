from sqlitecloud import SQLiteCloudConnection
import datetime

DB_URL = 'sqlitecloud://cz1dyazrhz.g4.sqlite.cloud:8860/auth.sqlitecloud?apikey=oHye0DO2njToIUEmIefnu3MJnPnUb4I7ZBOFJXuUhjw'

def mantener_viva():
    try:
        with SQLiteCloudConnection(DB_URL) as conn:
            cur = conn.cursor()

            now = datetime.datetime.now().isoformat(sep=' ', timespec='seconds')
            cur.execute("INSERT INTO time_log (time) VALUES (?);", (now,))
            conn.commit()

            print(f"[{now}] 🕒 Registro insertado y conexión viva.")

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    mantener_viva()
