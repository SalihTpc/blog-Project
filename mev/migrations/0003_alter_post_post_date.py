# Generated by Django 4.0.2 on 2022-02-23 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mev', '0002_alter_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
