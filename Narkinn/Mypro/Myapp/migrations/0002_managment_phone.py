# Generated by Django 3.2.8 on 2021-10-10 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='managment',
            name='phone',
            field=models.TextField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
