from django.db import models
from django.db.models.enums import Choices
from django.conf import settings
from django.contrib.auth.models import User

class GroceryItems(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    itemName = models.CharField(max_length=100)
    itemQuantity = models.IntegerField()
    itemStatus = (  ('PENDING','PENDING'),
                    ('BOUGHT','BOUGHT'),
                    ('NOTAVAILABLE','NOT AVAILABLE'),
                 )
    flag = models.CharField(max_length=20,choices=itemStatus,default='PENDING')
    dateAdded = models.DateField()

    def __str__(self):
        return self.itemName