# Generated by Django 5.0.2 on 2024-03-03 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_post_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ip',
            field=models.GenericIPAddressField(editable=False, null=True),
        ),
    ]
