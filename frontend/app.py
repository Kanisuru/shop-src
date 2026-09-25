import os
import time
import urllib.request
from flask import Flask, Response

app = Flask(__name__)
API_URL = os.getenv("API_URL", "http://api:8080")
START = time.time()

@app.get("/")
def index():
    try:
        with urllib.request.urlopen(f"{API_URL}/api/info", timeout=2) as r:
            body = r.read().decode()
        status = "ok"
    except Exception as e:
        body = str(e)
        status = "degraded"
    html = f"""<!doctype html>
    <html><body>
      <h1>Shop Frontend v4 - CI Pipeline Live</h1>
      <p>status: {status}</p>
      <pre>{body}</pre>
    </body></html>"""
    return Response(html, mimetype="text/html")

@app.get("/healthz")
def healthz():
    return {"status": "ok", "uptime": int(time.time() - START)}

@app.get("/readyz")
def readyz():
    try:
        urllib.request.urlopen(f"{API_URL}/healthz", timeout=1)
        return {"ready": True}
    except Exception:
        return {"ready": False}, 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
