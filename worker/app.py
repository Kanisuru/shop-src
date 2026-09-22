import os
import threading
import time
import urllib.request

from flask import Flask

app = Flask(__name__)
API_URL = os.getenv("API_URL", "http://api:8080")
processed = 0

def loop():
    global processed
    while True:
        try:
            urllib.request.urlopen(f"{API_URL}/api/jobs", timeout=2)
            processed += 1
        except Exception:
            pass
        time.sleep(5)

threading.Thread(target=loop, daemon=True).start()

@app.get("/healthz")
def healthz():
    return {"status": "ok", "processed": processed}

@app.get("/readyz")
def readyz():
    return {"ready": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
