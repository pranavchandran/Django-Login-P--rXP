# Generated by Django 3.1.4 on 2020-12-12 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_status_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('open', 'Open'), ('close', 'Close'), ('error', 'Error')], default='created', max_length=20),
        ),
    ]
