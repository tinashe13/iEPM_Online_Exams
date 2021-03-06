# Generated by Django 2.2.2 on 2019-07-08 08:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20190704_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='ch1',
            new_name='op1',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='ch2',
            new_name='op2',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='ch3',
            new_name='op3',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='ch4',
            new_name='op4',
        ),
        migrations.AlterField(
            model_name='exam',
            name='exam_creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 8, 11, 20, 2, 970618)),
        ),
        migrations.AlterField(
            model_name='takenexam',
            name='done_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 8, 11, 20, 2, 972636)),
        ),
    ]
