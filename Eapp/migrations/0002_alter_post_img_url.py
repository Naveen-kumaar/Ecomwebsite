# Generated by Django 5.0.7 on 2024-11-19 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img_url',
            field=models.URLField(null=True),
        ),
    ]
