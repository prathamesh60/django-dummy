# Generated by Django 2.1.15 on 2020-05-31 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=20, null=True)),
                ('visit_date', models.DateField(blank=True, verbose_name='Conversation Date')),
                ('visit_time', models.TimeField(blank=True, verbose_name='Conversation Time')),
            ],
        ),
        migrations.CreateModel(
            name='FundsActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=20, null=True)),
                ('visit_date', models.DateField(blank=True, verbose_name='Conversation Date')),
                ('visit_time', models.TimeField(blank=True, verbose_name='Conversation Time')),
            ],
        ),
        migrations.CreateModel(
            name='LoanActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=20, null=True)),
                ('visit_date', models.DateField(blank=True, verbose_name='Conversation Date')),
                ('visit_time', models.TimeField(blank=True, verbose_name='Conversation Time')),
            ],
        ),
    ]
