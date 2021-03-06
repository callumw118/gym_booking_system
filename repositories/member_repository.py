from db.run_sql import run_sql
from models.member import Member


def save(member):
    sql = 'INSERT INTO members (full_name, membership, status) VALUES (%s, %s, %s) RETURNING id'
    values = [member.full_name, member.membership, member.status]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)


def select_all():
    members = []
    sql = "SELECT * FROM members ORDER BY id"
    results = run_sql(sql)

    for result in results:
        member = Member(result['full_name'], result['membership'], result['status'], result['id'])
        members.append(member)
    return members


def select(id):
    sql = "SELECT * FROM members WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = Member(result['full_name'], result['membership'], result['status'], result['id'])
    return member


def update(member):
    sql = "UPDATE members SET (full_name, membership, status) = (%s, %s, %s) WHERE id = %s"
    values = [member.full_name, member.membership, member.status, member.id]
    run_sql(sql, values)