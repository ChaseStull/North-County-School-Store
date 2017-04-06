from django.db import models


class Item(models.Model):
    item_name = models.CharField(max_length=25)
    description = models.TextField('Description')
    stock = models.IntegerField('Items remaining')
    image = models.URLField('Image url')

    def __str__(self):
        return self.item_name
