from django.db import models


class Item(models.Model):
    item_name = models.CharField(max_length=25)
    description = models.TextField('Description')
    stock = models.IntegerField('Items remaining')

    def __str__(self):
        return self.item_name
