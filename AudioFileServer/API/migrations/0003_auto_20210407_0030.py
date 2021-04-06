# Generated by Django 3.2 on 2021-04-06 19:00

import API.forms
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20210407_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='UploadTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 0, 30, 6, 444786), validators=[API.forms.validate_date]),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='UploadTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 0, 30, 6, 444786), validators=[API.forms.validate_date]),
        ),
        migrations.AlterField(
            model_name='song',
            name='UploadTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 0, 30, 6, 429165), validators=[API.forms.validate_date]),
        ),
    ]
