# Generated by Django 2.2 on 2022-01-02 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220101_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='create',
            field=models.DateTimeField(auto_now=True, verbose_name='زمان ساخت'),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='update',
            field=models.DateTimeField(auto_now_add=True, verbose_name='بروزرسانی در'),
        ),
    ]
