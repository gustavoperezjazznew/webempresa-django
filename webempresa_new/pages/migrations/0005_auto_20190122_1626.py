# Generated by Django 2.0.2 on 2019-01-22 19:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20190122_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]
