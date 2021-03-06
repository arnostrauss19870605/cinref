# Generated by Django 3.1.1 on 2020-09-08 17:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=120, verbose_name='Name')),
                ('Surname', models.CharField(max_length=120, verbose_name='Surname')),
                ('PolicyNumber', models.CharField(max_length=10, verbose_name='Policy')),
                ('Email', models.CharField(max_length=150, verbose_name='Email')),
                ('BrokerName', models.CharField(max_length=10, verbose_name='Broker')),
                ('BrokerEmail', models.CharField(max_length=150, verbose_name='BrokerEmail')),
                ('PolicyPhone', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Referred',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=120, verbose_name='Name')),
                ('Surname', models.CharField(max_length=120, verbose_name='Surname')),
                ('Email', models.CharField(max_length=150, verbose_name='Email')),
                ('RefferedPhone', models.IntegerField()),
                ('Status', models.CharField(choices=[('PENDING', 'Pending'), ('ACTIVATED', 'Activated'), ('CLOSED', 'Closed')], max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('referral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_api.referral')),
            ],
        ),
    ]
