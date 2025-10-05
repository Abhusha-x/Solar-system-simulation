from flask import Blueprint, jsonify, send_from_directory, redirect, request, render_template
from helpers import get_palermo_leaderboard


sites = Blueprint('main', __name__)
# note the lack of a url_prefix parameter

@sites.route("/api/hello")
def hello_world():
    return jsonify({'message': "Hello World"})

@sites.route('/index')
@sites.route('')
def main_page():
    # Route for the main index page, which we'll assume is a static file if not redirected
    path = 'index.html'
    print(path)
    return send_from_directory('static', path=path)

@sites.route('/')
def base():
    # Redirect the root path to the main application view (the leaderboard)
    return redirect('/leaderboard')

@sites.route('/leaderboard')
def leaderboard():
    """
    Fetches the Palermo Leaderboard data and renders the leaderboard template.
    This function was previously blocked by the impact_map route.
    """
    data = get_palermo_leaderboard(limit=10)
    return render_template("leaderboard.html", data=data)

@sites.route('/impact-map')
def impact_map_static():
    """
    Serves the static 'impact.html' file, previously incorrectly routed to '/leaderboard'.
    """
    path = 'impact.html'
    print(path)
    return send_from_directory('static', path=path)

@sites.route("/impact_map")
def legacy_redirect():
    # This seems like a legacy route redirecting to a simulation, keeping it as is.
    return redirect("/sim/asteroid-launcher", code=302)
