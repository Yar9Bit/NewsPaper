# Generated by Django 4.1 on 2022-10-26 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0005_remove_author_subscribers_delete_authorsubscribers'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategorySubscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(through='news.CategorySubscribe', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='categorysubscribe',
            name='category_thru',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category'),
        ),
        migrations.AddField(
            model_name='categorysubscribe',
            name='subscriber_thru',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]