# Generated by Django 2.2.12 on 2020-06-23 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0017_skillpost_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationpost',
            name='body',
            field=models.TextField(default="<p class='cv-post-text'> </p>"),
        ),
    ]