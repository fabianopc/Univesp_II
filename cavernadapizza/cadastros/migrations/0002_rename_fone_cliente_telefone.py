# Generated by Django 4.2.6 on 2023-10-12 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='fone',
            new_name='telefone',
        ),
    ]
