# Generated by Django 3.1.2 on 2020-10-07 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0009_auto_20201005_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.UUIDField(default='AD83F4', editable=False, primary_key=True, serialize=False),
        ),
    ]