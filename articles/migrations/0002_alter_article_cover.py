# Generated by Django 4.0 on 2021-12-25 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
