# Generated by Django 3.1.2 on 2020-10-09 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0021_auto_20201009_1522'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='room_code',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='rooms.room'),
        ),
    ]
