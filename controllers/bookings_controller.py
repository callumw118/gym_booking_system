from flask import Blueprint, Flask, redirect, render_template, request
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository
from models.booking import Booking
from datetime import datetime 

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

    # Converts the string activity time to a time
    datetime_string = activity.time
    datetime_of_activity = datetime.strptime(datetime_string,'%H:%M').time()

    # Off-Peak Hours between 09:00 and 17:00, converts them to a time
    minimum_time = "09:00"
    datetime_minimum_time = datetime.strptime(minimum_time,'%H:%M').time()
    maximum_time = "17:00"
    datetime_maximum_time = datetime.strptime(maximum_time, '%H:%M').time()

    # Checks if capacity in class in greater than 1, if so adds member to class an
    # Won't allow member to be added if the capacity is 0
    if activity.capacity > activity.members_booked:
        if member.membership == "Premium":
            booking_repository.save(booking)
            # Save standard membership member to booking if the time of the activity is between the off-peak hours
        if member.membership == "Standard" and datetime_of_activity > datetime_minimum_time and datetime_of_activity < datetime_maximum_time:
            booking_repository.save(booking)
    else:
        print("Class full")
    return redirect("/bookings/new")
   