# Generated by Django 3.1.5 on 2021-04-19 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0013_about_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_detail',
            name='heading',
            field=models.CharField(default='summa', max_length=255),
        ),
    ]
