# Generated by Django 2.0.7 on 2018-07-25 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_auto_20180722_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='invco',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
    ]