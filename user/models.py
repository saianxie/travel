from django.db import models

# Create your models here.

class user(models.Model):
    telephone = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=64)
    name=models.CharField(max_length=20)

# class log(models.Model):
#     user_id = models.CharField(unique=True, max_length=50)
#     password = models.CharField(max_length=64)
#     name = models.CharField(max_length=20)
#
#     country = models.ForeignKey("country", to_field="id", default=1, on_delete=models.CASCADE)

class lineevaluate(models.Model):
    evaluation = models.CharField(max_length=64)
    trip = models.CharField(max_length=64)
    evaluatetime = models.DateField()
    user = models.ForeignKey("user", to_field="id", on_delete=models.CASCADE)
    line = models.ForeignKey("tripline.tripline", to_field="id", on_delete=models.CASCADE)

class userinfo(models.Model):
    name = models.CharField(max_length=20)
    telephone = models.CharField(unique=True, max_length=50)
    address = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    birthday = models.DateField()
    registdate = models.DateField()
    user = models.ForeignKey("user", to_field="id", on_delete=models.CASCADE)
    icon = models.ForeignKey("usericon", to_field="id", default=1, on_delete=models.CASCADE)


class usericon(models.Model):
    icon = models.CharField(max_length=100)
    uploadtime = models.DateField()
    user = models.ForeignKey("user", to_field="id", on_delete=models.CASCADE)


