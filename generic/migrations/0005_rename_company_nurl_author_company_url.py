# Generated by Django 3.2.4 on 2021-06-08 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0004_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='company_nurl',
            new_name='company_url',
        ),
    ]
