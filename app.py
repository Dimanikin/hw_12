import logging

from flask import Flask, send_from_directory

from loader.views import loader_blueprint
from main.views import main_blueprint


# POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

logging.basicConfig(filename="basic.log", level=logging.INFO)

app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run(debug=True)
