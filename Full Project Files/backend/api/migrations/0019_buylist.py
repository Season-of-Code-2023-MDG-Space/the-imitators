# Generated by Django 4.1.7 on 2023-03-28 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_newslist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('q', models.FloatField()),
            ],
        ),
    ]
