# Generated by Django 2.1.2, hand modified to use relative paths
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioproject',
            name='updated',
            field=models.DateField(null=True),
        ),
    ]
