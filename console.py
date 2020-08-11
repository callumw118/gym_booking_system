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

member_2 = Member("James Mann", "Premium")
member_repository.save(member_2)

activity_1 = Activity("HIIT (High Intensity Training)", "Monday", "13:00", 10)
activity_repository.save(activity_1)

activity_2 = Activity("Indoor Cycling", "Monday", "15:00", 20)
activity_repository.save(activity_2)

activity_3 = Activity("Functional Strength", "Tuesday", "18:00", 12)
activity_repository.save(activity_3)

booking_1 = Booking(member_1, activity_1)
booking_repository.save(booking_1)

booking_2 = Booking(member_2, activity_1)
booking_repository.save(booking_2)

pdb.set_trace()