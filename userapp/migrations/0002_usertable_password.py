# Generated by Django 4.1.2 on 2022-10-19 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertable',
            name='password',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]