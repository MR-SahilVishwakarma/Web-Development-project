# Generated by Django 4.1.5 on 2023-01-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_login_signin'),
    ]

    operations = [
        migrations.AddField(
            model_name='signin',
            name='role',
            field=models.IntegerField(default=2),
        ),
    ]
