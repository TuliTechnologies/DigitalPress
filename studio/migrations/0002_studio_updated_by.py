# Generated by Django 3.0.6 on 2023-06-27 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studio',
            name='updated_by',
            field=models.CharField(default=False, max_length=255),
        ),
    ]