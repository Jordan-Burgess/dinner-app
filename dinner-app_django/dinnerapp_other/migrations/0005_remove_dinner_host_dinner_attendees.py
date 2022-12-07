# Generated by Django 4.1.3 on 2022-12-07 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinnerapp_other', '0004_remove_dinner_location_dinner_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dinner',
            name='host',
        ),
        migrations.AddField(
            model_name='dinner',
            name='attendees',
            field=models.ManyToManyField(to='dinnerapp_other.profile'),
        ),
    ]
