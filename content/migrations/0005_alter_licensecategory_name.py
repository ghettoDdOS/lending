# Generated by Django 3.2.13 on 2022-06-17 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_license_licensecategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licensecategory',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название категории'),
        ),
    ]