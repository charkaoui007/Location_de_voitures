# Generated by Django 4.0.3 on 2022-03-11 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_alter_comment_create_date'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='book',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='cars.booking'),
        ),
    ]