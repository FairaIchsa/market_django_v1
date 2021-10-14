# Generated by Django 3.2.7 on 2021-10-14 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_alter_tennistable_folded_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menucategory',
            name='url',
            field=models.URLField(unique=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_popular',
            field=models.BooleanField(default=False, verbose_name='Популярен'),
        ),
        migrations.AlterField(
            model_name='sliderinfo',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]
