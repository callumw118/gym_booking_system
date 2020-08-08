from flask import Blueprint, Flask, redirect, render_template, request
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository
from models.booking import Booking

bookings_blueprint = Blueprint("bookings", __name__)


# INDEX
@bookings_blueprint.route("/bookings")
def index():
    bookings = booking_repository.select_all()
    activities = activity_repository.select_all()
    members = member_repository.select_all()
    return render_template("/bookings/index.html", bookings=bookings, activities=activities, members=members)


# NEW
@bookings_blueprint.route("/bookings/new")
def new():
    members = member_repository.select_all()
    activities = activity_repository.select_all()
    return render_template("/bookings/new.html", members=members, activities=activities)


# CREATE
@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
    member_id = request.form['member_id']
    activity_id = request.form['activity_id']

    member = member_repository.select(member_id)
    activity = activity_repository.select(activity_id)

    booking = Booking(member, activity)
    booking_repository.save(booking)
    return redirect("/bookings")