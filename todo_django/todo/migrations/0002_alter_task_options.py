# Generated by Django 3.2.4 on 2021-06-15 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-expired_at']},
        ),
    ]
