# Generated by Django 4.1.9 on 2023-11-21 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Titan_app', '0005_alter_customusertitan_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusertitan',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
