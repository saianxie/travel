# Generated by Django 2.1.1 on 2018-10-22 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripline', '0007_delete_hotelinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='hotelinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('englishname', models.CharField(max_length=50)),
            ],
        ),
    ]