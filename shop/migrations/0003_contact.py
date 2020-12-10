# Generated by Django 3.1 on 2020-08-24 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200820_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=70)),
                ('message', models.CharField(default='', max_length=800)),
            ],
        ),
    ]
