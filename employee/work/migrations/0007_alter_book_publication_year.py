# Generated by Django 4.2.7 on 2023-11-28 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0006_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.PositiveIntegerField(),
        ),
    ]
