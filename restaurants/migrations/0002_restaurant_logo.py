# Generated by Django 2.1.5 on 2020-02-15 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
