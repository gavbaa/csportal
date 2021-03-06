# Generated by Django 2.1.3 on 2018-11-10 01:00

import appable.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appable', '0003_auto_20181110_0053'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReleaseFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to=appable.models.release_file_path)),
                ('notes', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='releasefiles',
            name='release',
        ),
        migrations.AlterModelOptions(
            name='release',
            options={'ordering': ['mainline__product__name', 'mainline__name', '-version_number']},
        ),
        migrations.AlterField(
            model_name='mainline',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='release',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='ReleaseFiles',
        ),
        migrations.AddField(
            model_name='releasefile',
            name='release',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appable.Release'),
        ),
    ]
