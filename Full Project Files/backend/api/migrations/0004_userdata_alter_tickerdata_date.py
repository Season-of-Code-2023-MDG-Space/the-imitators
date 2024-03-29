# Generated by Django 4.1.7 on 2023-03-25 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_tickerdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('age', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='tickerdata',
            name='Date',
            field=models.CharField(max_length=200),
        ),
    ]
