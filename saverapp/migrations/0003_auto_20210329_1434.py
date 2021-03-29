# Generated by Django 3.1.3 on 2021-03-29 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saverapp', '0002_report_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='status',
            field=models.CharField(choices=[('Submitted', 'sub'), ('Approved', 'app'), ('Action Taken', 'act')], max_length=15),
        ),
    ]
