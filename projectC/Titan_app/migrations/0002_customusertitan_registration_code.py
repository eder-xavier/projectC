# Generated by Django 4.1.9 on 2023-11-21 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Titan_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusertitan',
            name='registration_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]