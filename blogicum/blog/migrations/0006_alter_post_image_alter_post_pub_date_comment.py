# Generated by Django 5.1.7 on 2025-03-07 11:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts_images', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, help_text='Если установить дату и время в будущем — можно делать отложенные публикации.', verbose_name='Дата и время публикации'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, help_text='Снимите галочку, чтобы скрыть публикацию.', verbose_name='Опубликовано')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('text', models.TextField(verbose_name='Текст')),
                ('pub_date', models.DateTimeField(auto_now_add=True, help_text='Если установить дату и время в будущем — можно делать отложенные публикации.', verbose_name='Дата и время публикации')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор публикации')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['pub_date'],
            },
        ),
    ]
