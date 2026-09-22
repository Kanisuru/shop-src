import os
import time
from flask import Flask, jsonify

app = Flask(__name__)
VERSION = os.getenv("APP_VERSION", "dev")
START = time.time()
JOBS = [{"id": 1, "item": "widget"}, {"id": 2, "item": "gadget"}]

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/readyz")
def readyz():
    return {"ready": True}

@app.get("/api/info")
def info():
    return jsonify({
        "service": "api",
        "version": VERSION,
        "uptime": int(time.time() - START),
        "jobs": len(JOBS),
    })

@app.get("/api/jobs")
def jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
