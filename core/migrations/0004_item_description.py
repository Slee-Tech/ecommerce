# Generated by Django 2.2.4 on 2019-09-25 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190925_0405'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='Test description of product'),
            preserve_default=False,
        ),
    ]
