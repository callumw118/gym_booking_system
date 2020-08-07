from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = 'INSERT INTO members (full_name) VALUES (%s) RETURNING id'
    values = [member.full_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)


def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for result in results:
        member = Member(result['full_name'], result['id'])
        members.append(member)
    return members