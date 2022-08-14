from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Organisation(models.Model):
    name = models.CharField(max_length=100)
    registered_users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    nickname = models.CharField(max_length=100)
    floor = models.IntegerField(null=True)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booker = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    comments = models.TextField(null=True)

    def __str__(self):
        return f"{self.room.nickname} - {self.start_time.strftime('%Y/%m/%d')}"
