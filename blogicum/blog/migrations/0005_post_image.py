# Generated by Django 5.1.7 on 2025-03-07 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Фото'),
        ),
    ]
