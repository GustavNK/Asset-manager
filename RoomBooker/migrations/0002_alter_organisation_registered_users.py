# Generated by Django 4.1 on 2022-08-14 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoomBooker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='registered_users',
            field=models.ManyToManyField(null=True, to='RoomBooker.user'),
        ),
    ]
