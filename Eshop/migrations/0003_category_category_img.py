# Generated by Django 4.1.1 on 2022-09-29 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_img',
            field=models.ImageField(null=True, upload_to='upload/'),
        ),
    ]