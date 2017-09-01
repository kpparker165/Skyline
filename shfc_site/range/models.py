from django.db import models

import datetime

# Create your models here.
class RangeHome(models.Model):

  about = models.TextField()


class ShootingRangeDetail(models.Model):
  #range_about = models.TextField()
  range_pistol = models.TextField()
  range_100_yard = models.TextField()
  range_200_300_yard = models.TextField()
  range_trap_skeet = models.TextField()
  creation_date = models.DateTimeField(auto_now_add=True, blank=False)


class RSOCalendar(models.Model):
  rso_person = models.ForeignKey("auth.User", limit_choices_to={'groups__name': "RSO"})
  rso_start_date = models.DateTimeField(blank=False)
  rso_end_date = models.DateTimeField(blank=False)
  creation_date = models.DateTimeField(auto_now_add=True, blank=False)
  def as_json(self):
    return dict(
      pk=self.pk, 
      rso_person_first=self.rso_person.first_name,
      rso_person_last=self.rso_person.last_name,
      rso_start_date=str(self.rso_start_date), 
      rso_end_date=str(self.rso_end_date),
      )