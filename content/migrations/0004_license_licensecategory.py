# Generated by Django 3.2.13 on 2022-06-17 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_news_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='LicenseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория лицензии',
                'verbose_name_plural': 'Категории лицензий',
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='licenses', verbose_name='Фото')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.licensecategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Лицензия',
                'verbose_name_plural': 'Лицензии',
            },
        ),
    ]
