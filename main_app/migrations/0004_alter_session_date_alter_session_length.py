# Generated by Django 4.1.6 on 2023-02-10 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date',
            field=models.DateTimeField(verbose_name='Date of play session'),
        ),
        migrations.AlterField(
            model_name='session',
            name='length',
            field=models.CharField(choices=[('1', '1 hour'), ('2', '2 hours'), ('3', '3 hours'), ('4', '4 hours'), ('5', '5 hours'), ('6', '6 hours'), ('7', '7 hours'), ('8', '8 hours'), ('9', '9 hours')], default='1', max_length=1),
        ),
    ]