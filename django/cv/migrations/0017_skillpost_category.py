# Generated by Django 2.2.12 on 2020-06-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0016_remove_achievementpost_sub_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillpost',
            name='category',
            field=models.CharField(choices=[('LANGUAGES', 'Languages'), ('PROGRAMMING_LANGUAGES', 'Programming Languages'), ('PROGRAMMING_TOOLS', 'Programming Tools')], default='PROGRAMMING_LANGUAGES', max_length=150),
        ),
    ]
