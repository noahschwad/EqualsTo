# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer_text',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='votes',
        ),
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_10',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_6',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_8',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_9',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_1',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='answer_2',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='question_String',
            field=models.CharField(default='teststring', max_length=200),
            preserve_default=False,
        ),
    ]
