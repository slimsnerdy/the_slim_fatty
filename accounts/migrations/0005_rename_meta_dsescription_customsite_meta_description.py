# Generated by Django 4.0.5 on 2023-05-16 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_site_meta_description_customsite_meta_dsescription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customsite',
            old_name='meta_dsescription',
            new_name='meta_description',
        ),
    ]