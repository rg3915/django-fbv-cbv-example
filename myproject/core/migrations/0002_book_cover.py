# Generated by Django 2.0.4 on 2018-04-25 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.URLField(blank=True, null=True, verbose_name='capa'),
        ),
    ]
