from datetime import time
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    def _str_(self):
        return f"{self.name}: room {self.room_number} on floor {self.floor}"

class Meetings(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.title} at {self.start_time} on {self.date}"



# Create your models here.
