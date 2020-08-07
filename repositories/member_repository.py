from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = 'INSERT INTO members (full_name) VALUES (%s) RETURNING id'
    values = [member.full_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id