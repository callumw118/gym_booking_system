from flask import Blueprint, Flask, redirect, render_template, request
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository
from models.booking import Booking

booking_blueprint = Blueprint("bookings", __name__)


# NEW
@booking_blueprint.route("/bookings/new")
def new():
    members = member_repository.select_all()
    activities = activity_repository.select_all()
    return render_template("/bookings/new.html", members=members, activities=activities)