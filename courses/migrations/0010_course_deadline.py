# Generated by Django 4.0 on 2021-12-25 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_course_certificate_alter_course_skill_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]
