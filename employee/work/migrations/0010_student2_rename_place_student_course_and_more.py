# Generated by Django 4.2.7 on 2023-12-01 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0009_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('place', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=6)),
            ],
        ),
        migrations.RenameField(
            model_name='student',
            old_name='place',
            new_name='course',
        ),
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.RemoveField(
            model_name='student',
            name='gender',
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]