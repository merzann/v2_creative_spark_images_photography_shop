# Generated by Django 4.2.20 on 2025-06-07 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newslettersignup',
            name='first_name',
            field=models.CharField(default='N/A', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newslettersignup',
            name='last_name',
            field=models.CharField(default='N/A', max_length=30),
            preserve_default=False,
        ),
    ]
