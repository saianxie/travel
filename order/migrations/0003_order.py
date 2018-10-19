# Generated by Django 2.1.1 on 2018-10-19 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tripline', '0003_tripline_types'),
        ('user', '0007_userinfo_icon'),
        ('order', '0002_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('totalprice', models.CharField(max_length=10)),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tripline.tripline')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.state')),
                ('supply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.supplier')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
