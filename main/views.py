from flask import render_template, Blueprint, request

from functions import search_post

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route("/")
def index():
    return render_template("index.html")


@main_blueprint.route("/search/")
def search():
    s = request.args.get("s", "")
    posts = search_post(s)
    return render_template("post_list.html", posts=posts, s=s)
