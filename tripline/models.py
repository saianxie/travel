from django.db import models


# Create your models here.



class chau(models.Model):
    name = models.CharField(max_length=10)


class country(models.Model):
    name = models.CharField(max_length=20)
    chau = models.ForeignKey("chau", to_field="id", default=1, on_delete=models.CASCADE)


class city(models.Model):
    name = models.CharField(max_length=20)
    country = models.ForeignKey("country", to_field="id", default=1, on_delete=models.CASCADE)

#
# class hotel(models.Model):
#     name = models.CharField(max_length=50)
#     englishname = models.CharField(max_length=100)

# 多对多自动生成中间表
# class Person(models.Model):
#     name = models.CharField(max_length=16)
#     birthday = models.DateField()
# class Group(models.Model):
#     name = models.CharField(max_length=16)
#     members = models.ManyToManyField(Person)
class triptime(models.Model):
    time = models.CharField(max_length=10)

class triptype(models.Model):
    name= models.CharField(max_length=10)

class tripline(models.Model):
    title = models.CharField(max_length=200)
    acount = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    label = models.CharField(max_length=10)
    img = models.CharField(max_length=100)
    times = models.ManyToManyField(triptime)
    types = models.ManyToManyField(triptype)

# class view(models.Model):
#     viewimage = models.CharField(max_length=50)




