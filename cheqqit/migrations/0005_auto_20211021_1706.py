# Generated by Django 3.2.8 on 2021-10-21 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheqqit', '0004_auto_20211015_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]