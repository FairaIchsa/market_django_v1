# Generated by Django 3.2.7 on 2021-10-08 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20211008_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menucategory',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]