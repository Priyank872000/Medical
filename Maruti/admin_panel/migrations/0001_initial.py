# Generated by Django 3.2.5 on 2021-07-20 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='partyDetails',
            fields=[
                ('party_id', models.AutoField(primary_key=True, serialize=False)),
                ('party_name', models.CharField(max_length=40)),
                ('area', models.CharField(blank=True, max_length=40, null=True)),
                ('GST_No', models.CharField(blank=True, max_length=50, null=True)),
                ('party_type', models.CharField(max_length=15)),
                ('mobile_no', models.IntegerField()),
            ],
            options={
                'db_table': 'Party_details',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('pro_id', models.AutoField(primary_key=True, serialize=False)),
                ('pro_name', models.CharField(max_length=50)),
                ('MRP', models.IntegerField()),
            ],
            options={
                'db_table': 'Products_details',
            },
        ),
    ]
