# Generated by Django 5.0.7 on 2024-09-11 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_myformdata_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='myformdata',
            name='invoice_id',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
