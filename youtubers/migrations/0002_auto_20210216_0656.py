# Generated by Django 3.1.5 on 2021-02-16 01:26

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ytuber',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ytuber',
            name='camera_type',
            field=models.CharField(choices=[['cannon', 'cannon'], ['nikon', 'nikon'], ['sony', 'sony'], ['panasonic', 'panasonic'], ['nokia', 'nokia']], max_length=255),
        ),
        migrations.AlterField(
            model_name='ytuber',
            name='category',
            field=models.CharField(choices=[['coding', 'coding'], ['comedy', 'comedy'], ['short_film', 'short-film'], ['mobile_review', 'mobile_review'], ['others', 'others']], max_length=255),
        ),
        migrations.AlterField(
            model_name='ytuber',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 16, 6, 56, 53, 688126)),
        ),
        migrations.AlterField(
            model_name='ytuber',
            name='crew',
            field=models.CharField(choices=[['solo', 'solo'], ['small', 'small'], ['large', 'large']], max_length=255),
        ),
        migrations.AlterField(
            model_name='ytuber',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
