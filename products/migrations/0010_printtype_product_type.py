# Generated by Django 4.2.20 on 2025-03-29 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_shipper_tracking_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='printtype',
            name='product_type',
            field=models.ForeignKey(blank=True, help_text='ProductType used to calculate shipping.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.producttype'),
        ),
    ]
