from meetings.models import Meeting, TimeSlot, User


class UserService:

    @staticmethod
    def get_users_on_meeting(slot: TimeSlot):
        meetings = Meeting.objects.filter(timeSlot=slot)
        busy_users = [meeting.user for meeting in meetings]
        return [{"id": user.id, "name": user.name} for user in busy_users]

    @staticmethod
    def get_users_available(slot: TimeSlot):
        all_users = User.objects.all()
        busy_users = (
            Meeting.objects.filter(timeSlot=slot)
            .values_list("user", flat=True)
            .distinct()
        )

        available_users = all_users.exclude(id__in=busy_users)

        return [{"id": user.id, "name": user.name} for user in available_users]
