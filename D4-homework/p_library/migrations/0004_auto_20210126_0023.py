# Generated by Django 2.2.6 on 2021-01-25 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_auto_20210126_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
