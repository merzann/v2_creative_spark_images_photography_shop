# Generated by Django 4.2.20 on 2025-05-25 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_specialoffer_offer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialoffer',
            name='offer_type',
            field=models.CharField(blank=True, choices=[('free_shipping', 'Free Shipping Over Amount'), ('percentage_discount', 'Percentage Discount on Theme'), ('buy_x_get_y', 'Buy X Get Y Free')], help_text='Type of offer being applied.', max_length=30, null=True),
        ),
    ]
