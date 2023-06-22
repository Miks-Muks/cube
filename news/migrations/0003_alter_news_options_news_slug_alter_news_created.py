# Generated by Django 4.1.7 on 2023-04-11 09:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_options_news_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новости', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(default='Slug', help_text='Заполняется автоматически'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 11, 9, 19, 12, 302627, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
    ]