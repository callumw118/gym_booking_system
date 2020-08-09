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

member_1 = Member("Callum Wolfe")
member_repository.save(member_1)

member_2 = Member("James Mann")
member_repository.save(member_2)

activity_1 = Activity("HIIT (High Intensity Training)", "Monday", "13:00", 1)
activity_repository.save(activity_1)

activity_2 = Activity("Indoor Cycling", "Monday", "15:00", 20)
activity_repository.save(activity_2)

booking_1 = Booking(member_1, activity_1)
# booking_1.activity.capacity -= 1
booking_repository.save(booking_1)
activity_repository.update(booking_1.activity)

booking_2 = Booking(member_2, activity_2)
booking_repository.save(booking_2)

pdb.set_trace()