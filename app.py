from flask import Flask
import logging
import os

app = Flask(__name__)

# log folder (volume mount yaha hoga)
LOG_DIR = "/app/logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=f"{LOG_DIR}/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

@app.route("/")
def home():
    logging.info("Hello World request received")
    return "Hello World from Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
