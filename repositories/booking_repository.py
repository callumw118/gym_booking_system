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


def select(id):
    sql = "SELECT * FROM bookings where id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    member = member_repository.select(result['member_id'])
    activity = activity_repository.select(result['activity_id'])
    booking = Booking(member, activity, result['id'])
    return booking

def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        activity = activity_repository.select(row['activity_id'])
        booking = Booking(member, activity, row['id'])
        bookings.append(booking)
    return bookings