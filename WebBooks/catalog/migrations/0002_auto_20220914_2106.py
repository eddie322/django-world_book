# Generated by Django 3.0.8 on 2022-09-14 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(help_text='Выберите автора книги', to='catalog.Author', verbose_name='Aвтop книги'),
        ),
    ]
