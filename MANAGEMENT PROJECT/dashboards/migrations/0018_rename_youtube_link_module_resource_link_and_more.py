# Generated by Django 5.1.4 on 2024-12-26 04:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('dashboards', '0017_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='youtube_link',
            new_name='resource_link',
        ),
        migrations.RemoveField(
            model_name='course',
            name='resource_link',
        ),
        migrations.AlterField(
            model_name='course',
            name='created_by',
            field=models.ForeignKey(limit_choices_to={'role__role_name': 'Admin'}, on_delete=django.db.models.deletion.CASCADE, related_name='created_courses', to='authentication.user'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name='EmployeeCourseProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress_percentage', models.FloatField(default=0.0)),
                ('completed_on', models.DateTimeField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress', to='dashboards.course')),
                ('employee', models.ForeignKey(limit_choices_to={'role__role_name': 'Employee'}, on_delete=django.db.models.deletion.CASCADE, related_name='course_progress', to='authentication.user')),
            ],
            options={
                'unique_together': {('employee', 'course')},
            },
        ),
        migrations.DeleteModel(
            name='Progress',
        ),
    ]
