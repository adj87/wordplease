# Generated by Django 2.0.6 on 2018-06-17 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('PUB', 'Published'), ('DRA', 'Draft')], default='DRA', max_length=3),
        ),
    ]
