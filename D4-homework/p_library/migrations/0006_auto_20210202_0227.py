# Generated by Django 2.2.6 on 2021-02-01 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0005_auto_20210202_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Publisher'),
        ),
    ]
