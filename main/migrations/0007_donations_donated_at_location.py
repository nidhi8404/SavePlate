# Generated by Django 4.1.5 on 2023-01-20 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_donations_applied_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donations',
            name='donated_at_location',
            field=models.TextField(blank=True, null=True),
        ),
    ]
