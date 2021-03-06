# Generated by Django 3.0.3 on 2020-02-03 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appable', '0006_auto_20181110_0136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainline',
            options={'ordering': ['product__name', 'name']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='product',
            name='separate_ownership_by_mainline',
            field=models.BooleanField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
