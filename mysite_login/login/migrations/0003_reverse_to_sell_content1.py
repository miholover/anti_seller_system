# Generated by Django 2.2.5 on 2019-09-25 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_conventional_field_reverse_to_sell'),
    ]

    operations = [
        migrations.AddField(
            model_name='reverse_to_sell',
            name='content1',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
