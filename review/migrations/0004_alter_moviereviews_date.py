# Generated by Django 3.2.9 on 2021-11-21 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_moviereviews_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviereviews',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]