# Generated by Django 3.2.4 on 2021-07-03 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20210703_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo1',
            field=models.ImageField(upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo4',
            field=models.ImageField(blank=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo5',
            field=models.ImageField(blank=True, upload_to='documents/'),
        ),
    ]
