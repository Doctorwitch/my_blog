# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2019-02-16 08:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('pub_date', models.CharField(max_length=20)),
                ('editor', models.CharField(max_length=20)),
                ('summary', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=5000)),
                ('key_word1', models.CharField(max_length=20)),
                ('key_word2', models.CharField(max_length=20)),
                ('key_word3', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='article_column',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_blog.Column'),
        ),
    ]
