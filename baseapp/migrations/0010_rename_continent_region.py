# Generated by Django 4.1.3 on 2023-07-01 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0009_continent_about_continent_area_continent_beliefs_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Continent',
            new_name='Region',
        ),
    ]