# Generated by Django 3.2.9 on 2021-11-21 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_alter_moviereviews_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviereviews',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
