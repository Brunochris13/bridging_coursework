# Generated by Django 2.2.12 on 2020-06-15 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_auto_20200615_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='CVPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EducationPost',
            fields=[
                ('cvpost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cv.CVPost')),
                ('sub_title', models.CharField(max_length=100)),
            ],
            bases=('cv.cvpost',),
        ),
    ]