# Generated by Django 4.0.5 on 2023-05-02 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='meta_description',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
