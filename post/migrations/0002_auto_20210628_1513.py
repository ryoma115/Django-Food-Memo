# Generated by Django 3.2.4 on 2021-06-28 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, default='defo', null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image3',
            field=models.ImageField(blank=True, default='defo', null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image4',
            field=models.ImageField(blank=True, default='defo', null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image5',
            field=models.ImageField(blank=True, default='defo', null=True, upload_to='documents/'),
        ),
    ]
