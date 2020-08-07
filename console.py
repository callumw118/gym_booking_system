import pdb

from models.member import Member
import repositories.member_repository as member_repository

from models.activity import Activity
import repositories.activity_repository as activity_repository

member_repository.delete_all()
activity_repository.delete_all()

member_1 = Member("Callum Wolfe")
member_repository.save(member_1)

member_2 = Member("James Mann")
member_repository.save(member_2)

activity_1 = Activity("HIIT (High Intensity Training)", "Monday", "13:00")

pdb.set_trace()