from django.contrib.auth.models import User
from django.db import models


ACTIVITY = (
    ('Clown1 - Balloon Sorting', 'Clown1 - Balloon Sorting'),
    ('Clown2 - Clown Collar', 'Clown2 - Clown Collar'),
    ('Clown3 - Clown Face Paint', 'Clown3 - Clown Face Paint'),
    ('Clown4 - Hula Hoops', 'Clown4 - Hula Hoops'),
    ('Clown5 - Balloon Toss', 'Clown5 - Balloon Toss'),
)


class Clown(models.Model):
    clown = models.CharField(max_length=30, blank=True)
    price = models.FloatField(max_length=5, blank=True)
    activity = models.CharField(max_length=30, choices=ACTIVITY)

    def __str__(self):
        return self.clown


STATUS = (
    ('Upcoming', 'Upcoming'),
    ('Incipient', 'Incipient'),
    ('Completed', 'Completed'),
    ('Cancelled', 'Cancelled'),
)


class Appointment(models.Model):
    clown = models.ForeignKey(Clown, on_delete=models.CASCADE, default=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS, null=True)

    def __str__(self):
        return self.status





