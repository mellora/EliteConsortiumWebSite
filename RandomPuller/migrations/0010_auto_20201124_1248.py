# Generated by Django 3.1.2 on 2020-11-24 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RandomPuller', '0009_auto_20201120_1017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pulledrandoms',
            options={'ordering': ['pulled_company', 'date_pulled'], 'verbose_name': 'Pulled Random List', 'verbose_name_plural': 'Pulled Random Lists'},
        ),
    ]
