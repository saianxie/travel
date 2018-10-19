from django.db import models

# Create your models here.

class state(models.Model):
    state = models.CharField(max_length=10)
    # icon = models.CharField(max_length=100)
    # uploadtime = models.DateField()
    # user = models.ForeignKey("user", to_field="id", on_delete=models.CASCADE)

class supplier(models.Model):
    supply = models.CharField(max_length=20)
    kefutelephone= models.CharField(max_length=20)

class order(models.Model):
    number = models.CharField(max_length=10)
    totalprice = models.CharField(max_length=10)
    user = models.ForeignKey("user.user", to_field="id", on_delete=models.CASCADE)
    line = models.ForeignKey("tripline.tripline", to_field="id", on_delete=models.CASCADE)
    state = models.ForeignKey("state", to_field="id", on_delete=models.CASCADE)
    supply = models.ForeignKey("supplier", to_field="id", on_delete=models.CASCADE)
