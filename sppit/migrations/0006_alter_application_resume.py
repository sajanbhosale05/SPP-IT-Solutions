# Generated by Django 3.2.3 on 2022-06-09 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sppit', '0005_alter_application_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='resume',
            field=models.FileField(blank=True, upload_to='media'),
        ),
    ]
