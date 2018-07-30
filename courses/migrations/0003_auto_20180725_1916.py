# Generated by Django 2.0.7 on 2018-07-25 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20180725_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/courses/'),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
