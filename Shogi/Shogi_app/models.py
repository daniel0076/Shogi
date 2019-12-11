from django.db import models
from django.contrib.auth.models import UserManager

class GameHistory(models.Model):
    user1_id = models.IntegerField() 
    user2_id = models.IntegerField() 
    date     = models.CharField(max_length = 50)
    duration = models.CharField(max_length = 50)
    init_usi = models.CharField(max_length = 200)
    moves    = models.TextField()

    objects = UserManager()

    def __unicode__(self):
        return self.id

