# Generated by Django 4.1 on 2022-10-06 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_category_subscribers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subscribers',
        ),
    ]
