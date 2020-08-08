from flask import Blueprint, Flask, redirect, render_template, request

from models.activity import Activity
import repositories.activity_repository as activity_repository

activities_blueprint = Blueprint("activities", __name__)


# INDEX
@activities_blueprint.route("/activities")
def activities():
    activities = activity_repository.select_all()
    return render_template("/activities/index.html", activities=activities)