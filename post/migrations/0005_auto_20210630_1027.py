# Generated by Django 3.2.4 on 2021-06-30 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20210629_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo1',
            field=models.ImageField(default='defo/', upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo2',
            field=models.ImageField(blank=True, default='defo/', null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo3',
            field=models.ImageField(blank=True, default='defo/', null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo4',
            field=models.ImageField(blank=True, default='defo/', null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo5',
            field=models.ImageField(blank=True, default='defo/', null=True, upload_to='documents/'),
        ),
    ]