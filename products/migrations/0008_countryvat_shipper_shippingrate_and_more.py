# Generated by Django 4.2.20 on 2025-03-23 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_shippingoption'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryVAT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100, unique=True)),
                ('vat_rate', models.DecimalField(decimal_places=2, help_text='Set VAT as a decimal (e.g. 0.21 for 21%)', max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(choices=[('poster', 'Poster'), ('canvas', 'Canvas'), ('framed', 'Framed'), ('mug', 'Mug'), ('other', 'Other')], max_length=20)),
                ('country', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('shipper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.shipper')),
            ],
            options={
                'unique_together': {('product_type', 'shipper', 'country')},
            },
        ),
        migrations.DeleteModel(
            name='ShippingOption',
        ),
    ]
