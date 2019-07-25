# Generated by Django 2.2.3 on 2019-07-19 11:06

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190719_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='anonymous', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='lnglat',
            field=models.CharField(blank=True, help_text='경도/위도 포맷으로 입력', max_length=50, validators=[blog.models.lnglat_validator]),
        ),
    ]
