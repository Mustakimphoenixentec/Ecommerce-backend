# Generated by Django 4.2.7 on 2023-11-24 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_mainmenu_alter_cartmst_user_ref_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rolemst',
            name='company_ref_id',
        ),
    ]
