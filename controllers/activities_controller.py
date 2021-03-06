from flask import Blueprint, Flask, redirect, render_template, request

from models.activity import Activity
import repositories.activity_repository as activity_repository

activities_blueprint = Blueprint("activities", __name__)


# INDEX
@activities_blueprint.route("/activities")
def activities():
    activities = activity_repository.select_all()
    return render_template("/activities/index.html", activities=activities)


# NEW
@activities_blueprint.route("/activities/new")
def new_activity():
    return render_template("activities/new.html")


# CREATE
@activities_blueprint.route("/activities", methods=["POST"])
def create_activity():
    name = request.form["name"]
    day_of_week = request.form["day_of_week"]
    time = request.form["time"]
    capacity = request.form['capacity']
    new_activity = Activity(name, day_of_week, time, capacity)
    activity_repository.save(new_activity)
    return redirect("/activities")


# EDIT
@activities_blueprint.route("/activities/<id>/edit")
def edit_activity(id):
    activity = activity_repository.select(id)
    return render_template("/activities/edit.html", activity=activity)


# UPDATE
@activities_blueprint.route("/activities/<id>", methods=["POST"])
def update_activity(id):
    name = request.form["name"]
    day_of_week = request.form["day_of_week"]
    time = request.form["time"]
    capacity = request.form["capacity"]
    new_activity = Activity(name, day_of_week, time, capacity, id)
    activity_repository.update(new_activity)
    return redirect("/activities")


# DELETE
@activities_blueprint.route("/activities/<id>/delete", methods=["POST"])
def delete_activity(id):
    activity_repository.delete(id)
    return redirect("/activities")


