# Generated by Django 4.0.3 on 2022-03-24 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0005_event_created_at_event_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='cover',
            field=models.ImageField(null=True, upload_to='events/'),
        ),
    ]