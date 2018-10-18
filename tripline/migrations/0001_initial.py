# Generated by Django 2.1.1 on 2018-10-17 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('chau', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tripline.chau')),
            ],
        ),
        migrations.CreateModel(
            name='tripline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('acount', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
                ('label', models.CharField(max_length=10)),
                ('img', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='triptime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='tripline',
            name='times',
            field=models.ManyToManyField(to='tripline.triptime'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tripline.country'),
        ),
    ]