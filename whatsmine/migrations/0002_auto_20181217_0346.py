# Generated by Django 2.1.3 on 2018-12-17 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsmine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownedproduct',
            name='purchased_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='ownedproduct',
            name='valid_until',
            field=models.DateTimeField(auto_now=True),
        ),
    ]