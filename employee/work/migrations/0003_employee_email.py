# Generated by Django 4.2.7 on 2023-11-24 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_student_alter_employee_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]