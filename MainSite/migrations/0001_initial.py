# Generated by Django 3.1.2 on 2020-11-02 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConsortiumPricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200)),
                ('member_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('non_member_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('extra_cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('third_party_billing_time', models.CharField(max_length=200)),
                ('third_party_driver_number', models.CharField(max_length=200)),
                ('third_party_fee', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'verbose_name': 'Consortium Pricing',
                'verbose_name_plural': 'Consortium Pricing',
            },
        ),
    ]
