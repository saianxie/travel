# Generated by Django 2.1.1 on 2018-10-19 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20181019_0853'),
    ]

    operations = [
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('registdate', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
