# Generated by Django 4.0.6 on 2022-07-14 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('surname', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('unapproved', 'Unapproved'), ('approved', 'Approved'), ('banned', 'Banned')], default='unapproved', max_length=15)),
            ],
        ),
    ]
