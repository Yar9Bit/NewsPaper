# Generated by Django 4.1 on 2022-10-24 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_remove_category_subscribers'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorSubscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', through='news.AuthorSubscribers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='authorsubscribers',
            name='author_thru',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.author'),
        ),
        migrations.AddField(
            model_name='authorsubscribers',
            name='subscriber_thru',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
