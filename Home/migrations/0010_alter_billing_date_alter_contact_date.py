# Generated by Django 4.1.3 on 2023-01-25 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_merge_0002_alter_contact_phone_0008_billing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
