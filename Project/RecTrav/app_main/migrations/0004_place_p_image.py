# Generated by Django 4.0.6 on 2022-08-07 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0003_register_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='p_image',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
