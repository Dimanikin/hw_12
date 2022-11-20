import logging

from flask import render_template, Blueprint, request

from functions import load_file

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")


@loader_blueprint.route("/post_form/")
def upload_index():
    return render_template("post_form.html")


@loader_blueprint.route("/post_uploaded/", methods=["POST"])
def post_upload():
    try:
        picture = request.files.get("picture")
    except Exception as error:
        logging.error("File loads error")
        return error

    content = request.form.get("content")
    filename = picture.filename
    ext = filename.split(".")[-1]
    if ext in ["jpeg", "png", "jpg"]:
        picture.save(f"./uploads/images/{filename}")
        file = f"/uploads/images/{filename}"
        load_file(file, content)
        return render_template("post_uploaded.html", filename=filename, content=content)
    else:
        logging.info("File not image")
