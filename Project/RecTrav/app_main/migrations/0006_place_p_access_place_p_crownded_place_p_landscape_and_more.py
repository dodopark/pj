# Generated by Django 4.0.6 on 2022-09-06 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0005_alter_register_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='p_access',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='p_crownded',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='p_landscape',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='p_satisfaction',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='p_spacial',
            field=models.IntegerField(null=True),
        ),
    ]
