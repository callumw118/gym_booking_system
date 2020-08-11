import pdb

from models.member import Member
import repositories.member_repository as member_repository

from models.activity import Activity
import repositories.activity_repository as activity_repository

from models.booking import Booking
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
member_repository.delete_all()
activity_repository.delete_all()

member_1 = Member("Callum Wolfe", "Premium")
member_repository.save(member_1)

member_2 = Member("James Mann", "Standard")
member_repository.save(member_2)

member_3 = Member("Grant Hamilton", "Premium")
member_repository.save(member_3)

activity_1 = Activity("BoxFit", "Monday", "13:00", 10)
activity_repository.save(activity_1)

activity_2 = Activity("Indoor Cycling", "Monday", "15:00", 20)
activity_repository.save(activity_2)

activity_3 = Activity("Functional Strength", "Tuesday", "18:00", 12)
activity_repository.save(activity_3)

pdb.set_trace()