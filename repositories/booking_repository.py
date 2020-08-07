from db.run_sql import run_sql
from models.booking import Booking
from models.member import Member
from models.activity import Activity

import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository


def save(booking):
    sql = "INSERT INTO bookings (member_id, activity_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.activity.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)