# Generated by Django 2.1.2 on 2018-11-08 08:13

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20181108_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='language_preference',
            field=models.CharField(max_length=500),
        ),
    ]