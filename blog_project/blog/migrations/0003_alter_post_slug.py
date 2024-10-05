# Generated by Django 5.1 on 2024-09-04 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=100, unique=True),
        ),
    ]