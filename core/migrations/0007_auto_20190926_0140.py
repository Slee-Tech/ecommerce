# Generated by Django 2.2.4 on 2019-09-26 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190926_0029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='items',
            new_name='item',
        ),
    ]
