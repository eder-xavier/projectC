# Generated by Django 4.1.9 on 2023-11-16 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OutVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kic', models.IntegerField()),
                ('Period', models.CharField(max_length=100)),
                ('epoch', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WithVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kic', models.IntegerField()),
                ('Period', models.CharField(max_length=100)),
                ('epoch', models.CharField(max_length=100)),
                ('Period_td', models.CharField(max_length=100)),
                ('epoch_td', models.CharField(max_length=100)),
                ('e', models.CharField(max_length=100)),
                ('a', models.CharField(max_length=100)),
                ('omega', models.CharField(max_length=100)),
                ('Aa', models.CharField(max_length=100)),
                ('Bb', models.CharField(max_length=100)),
            ],
        ),
    ]
