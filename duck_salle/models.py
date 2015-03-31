from django.db import models
from duck_utils.models import Salle


class Reservation(models.Model):
    salle = models.ForeignKey(Salle)
    label = models.CharField(max_length=128, null=True, blank=True)
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return "{} ({} {} - {})".format(" ".join([self.salle.label, self.label]),
                                        self.date, self.start, self.end)