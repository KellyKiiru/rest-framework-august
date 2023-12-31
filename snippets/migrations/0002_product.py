# Generated by Django 4.2.4 on 2023-08-17 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('brand', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField()),
                ('specs', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
    ]
