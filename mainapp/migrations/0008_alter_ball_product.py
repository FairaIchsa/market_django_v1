# Generated by Django 3.2.7 on 2021-10-07 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20211007_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ball',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='child_product_data', to='mainapp.product', verbose_name='Товар'),
        ),
    ]
