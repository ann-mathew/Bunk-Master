# Generated by Django 3.1.2 on 2020-10-07 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0011_auto_20201007_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.CharField(default='1f557e01bf', editable=False, max_length=6, primary_key=True, serialize=False),
        ),
    ]
