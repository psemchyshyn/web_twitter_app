'''
Palvo Semchyshyn
22.02.2020
'''

from flask import Flask, render_template, redirect, request, url_for
from map_building import map_builder
from twitter_users import check_user_name


APP = Flask(__name__)


@APP.route('/')
def index():
    """
    A function for responding root page
    by rendering index.html file
    """
    return render_template("index.html")


@APP.route("/error")
def error_input():
    """
    A function for rendering user's
    incorrect input
    """
    return render_template("failure.html")


@APP.route("/find/<name>")
def map_of_friends(name: str):
    """
    (str) -> html file
    A function for rendering a map,
    after user clicked post method
    """
    map_builder(name)
    return render_template("map.html")


@APP.route("/find", methods=['POST'])
def find():
    """
    () -> html flle
    A function for processing user's
    post method
    """
    if request.method == "POST":
        user = request.form.get("user")
        if not user or not check_user_name(user):
            return redirect(url_for("error_input"))
        return redirect(url_for("map_of_friends", name=user))


if __name__ == "__main__":
    APP.jinja_env.auto_reload = True
    APP.config['TEMPLATES_AUTO_RELOAD'] = True
    APP.run(debug=True)
