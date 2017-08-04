from django.db import models
import datetime

# Create your models here.
class RangeHome(models.Model):

  about = models.TextField()


class RangeShooting(models.Model):
  range_about = models.TextField()
  range_pistol = models.TextField()
  range_100_yard = models.TextField()
  range_200_300_yard = models.TextField()
  range_trap_skeet = models.TextField()
  creation_date = models.DateTimeField(auto_now_add=True, blank=False)


