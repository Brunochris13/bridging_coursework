# Generated by Django 2.2.12 on 2020-06-18 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0011_auto_20200618_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpost',
            name='image',
            field=models.ImageField(upload_to='cv/img/projects'),
        ),
    ]
