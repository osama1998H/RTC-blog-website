# Generated by Django 4.0.3 on 2022-03-22 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0002_alter_instructor_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='facebook',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='instagram',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='linkedin',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='twitter',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
