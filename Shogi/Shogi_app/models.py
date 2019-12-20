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

class GamePuzzle(models.Model):
    init_usi    = models.CharField(max_length = 200)
    puzzle_name = models.CharField(max_length = 200)

    objects = UserManager()

    def __unicode__(self):
        return self.id

class UserAccount(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)

    objects = UserManager()
    
    def __unicode__(self):
        return self.id

class UserSettings(models.Model):
    userId   = models.IntegerField()
    settings = models.TextField()

    objects = UserManager()
    
    def __unicode__(self):
        return self.id


