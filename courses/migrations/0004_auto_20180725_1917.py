# Generated by Django 2.0.7 on 2018-07-25 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20180725_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='load',
            field=models.CharField(max_length=256),
        ),
    ]