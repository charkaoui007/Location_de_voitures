# Generated by Django 4.0.3 on 2023-05-06 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0025_alter_comment_create_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
