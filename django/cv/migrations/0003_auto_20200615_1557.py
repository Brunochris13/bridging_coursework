# Generated by Django 2.2.12 on 2020-06-15 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_category_cvpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cvpost',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='CVPost',
        ),
    ]