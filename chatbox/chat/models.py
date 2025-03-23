from django.db import models
from django import forms

class Room(models.Model):
    name = models.CharField(max_length=255)
    hash = models.CharField(max_length=255,default="0000")

    def __str__(self):
        return self.name
    
class Message(models.Model):
    text = models.TextField()
    room =  models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.TextField(default="Anonymous")

    def __str__(self):
        return str(self.room)
    
    