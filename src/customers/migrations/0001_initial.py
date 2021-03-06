# Generated by Django 2.0.7 on 2018-07-21 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=50)),
                ('postcode', models.CharField(max_length=50)),
                ('country', models.CharField(default='UK', max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('notes', models.TextField()),
            ],
        ),
    ]
