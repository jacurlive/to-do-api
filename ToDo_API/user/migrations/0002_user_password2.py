# Generated by Django 4.2.8 on 2023-12-21 10:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password2',
            field=models.CharField(default=django.utils.timezone.now, max_length=155),
            preserve_default=False,
        ),
    ]