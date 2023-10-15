# Generated by Django 4.2.5 on 2023-10-15 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('guardian_name', models.CharField(blank=True, max_length=255)),
                ('class_10_marks', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('class_12_marks', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
    ]
