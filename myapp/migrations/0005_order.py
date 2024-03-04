# Generated by Django 5.0.2 on 2024-02-24 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_donation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('food_id', models.IntegerField()),
                ('door_number', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
    ]
