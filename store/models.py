from django.db import models

# Create your models here.


ITEM_STATUS = (
	("PENDING", "PENDING"),
	("BOUGHT", "BOUGHT"),
	("NOT AVAILABLE","NOT AVAILABLE"),
)

class Item(models.Model):
	user = models.ForeignKey('core.User', on_delete=models.PROTECT)
	name = models.CharField(max_length=20)
	quantity = models.CharField(max_length=10)
	status = models.CharField(max_length=25, choices=ITEM_STATUS)
	date = models.DateField()
