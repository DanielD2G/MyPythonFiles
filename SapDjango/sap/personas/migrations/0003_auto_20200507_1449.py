# Generated by Django 3.0.6 on 2020-05-07 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_auto_20200507_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='domiclio',
            new_name='domicilio',
        ),
    ]
