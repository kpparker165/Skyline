from django.db import models
import datetime

class Home(models.Model):

  about = models.TextField()
  facilities = models.TextField()
  presidents_word = models.TextField()
  general = models.TextField()
  creation_date = models.DateTimeField(auto_now_add=True, blank=False)