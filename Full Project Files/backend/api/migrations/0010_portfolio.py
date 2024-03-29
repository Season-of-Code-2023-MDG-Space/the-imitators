# Generated by Django 4.1.7 on 2023-03-28 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_pricelist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('profit', models.FloatField()),
                ('loss', models.FloatField()),
                ('balance', models.FloatField()),
            ],
        ),
    ]
