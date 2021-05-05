# Generated by Django 3.1.6 on 2021-05-04 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0004_auto_20210502_0555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vulnerabilityscan',
            name='host',
        ),
        migrations.AddField(
            model_name='vulnerabilityscan',
            name='matched_url',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='startScan.waybackendpoint'),
        ),
    ]
