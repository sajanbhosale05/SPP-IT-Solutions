# Generated by Django 3.2.3 on 2022-06-09 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sppit', '0002_alter_contact_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phon',
            new_name='phone',
        ),
    ]