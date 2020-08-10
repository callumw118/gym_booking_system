from db.run_sql import run_sql
from models.activity import Activity


def save(activity):
    sql = "INSERT INTO activities (name, day_of_week, time, capacity) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [activity.name, activity.day_of_week, activity.time, activity.capacity]
    results = run_sql(sql, values)
    id = results[0]['id']
    activity.id = id


def delete_all():
    sql = "DELETE FROM activities"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM activities WHERE id=%s"
    values = [id]
    run_sql(sql, values)


def select_all():
    activities = []
    sql = "SELECT * FROM activities ORDER BY id"
    results = run_sql(sql)

    for result in results:
        activity = Activity(result['name'], result['day_of_week'], result['time'], result['capacity'], result['id'])
        activity.members_booked = bookings(activity)
        activities.append(activity)
    return activities


def select(id):
    sql = "SELECT * FROM activities WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    activity = Activity(result['name'], result['day_of_week'], result['time'], result['capacity'], result['id'])
    activity.members_booked = bookings(activity)
    return activity


def update(activity):
    sql = "UPDATE activities SET (name, day_of_week, time, capacity) = (%s, %s, %s, %s) WHERE id = %s"
    values = [activity.name, activity.day_of_week, activity.time, activity.capacity, activity.id]
    run_sql(sql, values)
    activity.members_booked = bookings(activity)


# Counts how many times the same activity_id appears in the booking
def bookings(activity):
    sql = "SELECT COUNT(*) FROM bookings WHERE activity_id = %s"
    values = [activity.id]
    result = run_sql(sql, values)[0]
    
    return result["count"]

