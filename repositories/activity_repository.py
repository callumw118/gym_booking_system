from db.run_sql import run_sql
from models.activity import Activity

def save(activity):
    sql = "INSERT INTO activities (name, day_of_week, time) VALUES (%s, %s, %s) RETURNING id"
    values = [activity.name, activity.day_of_week, activity.time]
    results = run_sql(sql, values)
    id = results[0]['id']
    activity.id = id