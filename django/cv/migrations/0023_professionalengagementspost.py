# Generated by Django 5.0.1 on 2024-02-04 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0022_auto_20200713_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessionalEngagementsPost',
            fields=[
                ('cvpost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cv.cvpost')),
            ],
            bases=('cv.cvpost',),
        ),
    ]