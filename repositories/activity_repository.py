from db.run_sql import run_sql
from models.activity import Activity

def save(activity):
    sql = "INSERT INTO activities (name, day_of_week, time) VALUES (%s, %s, %s) RETURNING id"
    values = [activity.name, activity.day_of_week, activity.time]
    results = run_sql(sql, values)
    id = results[0]['id']
    activity.id = id
    

def delete_all():
    sql = "DELETE FROM activities"
    run_sql(sql)


def select_all():
    activities = []
    sql = "SELECT * FROM activities"
    results = run_sql(sql)

    for result in results:
        activity = Activity(result['name'], result['day_of_week'], result['time'], result['id'])
        activities.append(activity)
    return activities