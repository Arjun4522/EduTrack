# Generated by Django 4.2.5 on 2023-10-15 21:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_attendance'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attendance',
            new_name='StudentAttendance',
        ),
    ]