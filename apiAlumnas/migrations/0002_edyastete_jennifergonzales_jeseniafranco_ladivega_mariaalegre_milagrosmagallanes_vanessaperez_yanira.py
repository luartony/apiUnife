# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-25 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiAlumnas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EdyAstete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('url_imagen', models.ImageField(default='default.png', upload_to='')),
                ('likes', models.CharField(blank=True, default='0', max_length=100)),
                ('Descripción', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='JenniferGonzales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('url_imagen', models.ImageField(default='default.png', upload_to='')),
                ('likes', models.CharField(blank=True, default='0', max_length=100)),
                ('Descripción', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='JeseniaFranco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('url_imagen', models.ImageField(default='default.png', upload_to='')),
                ('likes', models.CharField(blank=True, default='0', max_length=100)),
                ('Descripción', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LadiVega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('url_imagen', models.ImageField(default='default.png', upload_to='')),
                ('likes', models.CharField(blank=True, default='0', max_length=100)),
                ('Descripción', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MariaAlegre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('url_imagen', models.ImageField(default='default.png', upload_to='')),
                ('likes', models.CharField(blank=True, default='0', max_length=100)),
                ('Descripción', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MilagrosMagallanes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('url_imagen', models.ImageField(default='default.png', upload_to='')),
                ('likes', models.CharField(blank=True, default='0', max_length=100)),
                ('Descripción', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VanessaPerez',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('url_imagen', models.ImageField(default='default.png', upload_to='')),
                ('likes', models.CharField(blank=True, default='0', max_length=100)),
                ('Descripción', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='YaniraPeña',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('url_imagen', models.ImageField(default='default.png', upload_to='')),
                ('likes', models.CharField(blank=True, default='0', max_length=100)),
                ('Descripción', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='YaquelinHerrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('url_imagen', models.ImageField(default='default.png', upload_to='')),
                ('likes', models.CharField(blank=True, default='0', max_length=100)),
                ('Descripción', models.TextField()),
            ],
        ),
    ]