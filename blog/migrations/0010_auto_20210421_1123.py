# Generated by Django 3.1.7 on 2021-04-21 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210413_1354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcomment',
            options={'verbose_name_plural': 'Blog Comments'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Posts'},
        ),
    ]
