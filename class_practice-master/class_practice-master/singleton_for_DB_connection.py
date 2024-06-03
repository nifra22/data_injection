import threading

class Database:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def query(self, sql):
        print(f"Executing query: {sql}")

class Application:
    def main(self):
        foo = Database()
        foo.query("SELECT ...")
        bar = Database()
        bar.query("SELECT ...")

if __name__ == "__main__":
    app = Application()
    app.main()
