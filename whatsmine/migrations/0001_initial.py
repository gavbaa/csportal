# Generated by Django 2.1.3 on 2018-11-10 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appable', '0001_initial'),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnedMainline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('mainline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appable.Mainline')),
            ],
        ),
        migrations.CreateModel(
            name='OwnedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appable.Product')),
            ],
        ),
        migrations.AddField(
            model_name='ownedmainline',
            name='owned_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whatsmine.OwnedProduct'),
        ),
    ]
