import pdb

from models.member import Member
import repositories.member_repository as member_repository

member_repository.delete_all()

member_1 = Member("Callum Wolfe")
member_repository.save(member_1)

member_2 = Member("James Mann")
member_repository.save(member_2)

pdb.set_trace()