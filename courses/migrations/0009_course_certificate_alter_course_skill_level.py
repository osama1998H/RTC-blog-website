# Generated by Django 4.0 on 2021-12-25 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_course_skill_level_alter_course_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='certificate',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default=1, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='skill_level',
            field=models.CharField(blank=True, choices=[('Beginner', 'Beginner'), ('Advance', 'Advance')], default=1, max_length=50, null=True),
        ),
    ]
