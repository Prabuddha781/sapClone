# Generated by Django 3.2.6 on 2021-09-09 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210909_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('taxCode', models.CharField(max_length=4)),
                ('taxJur', models.CharField(max_length=10)),
                ('busArea', models.CharField(max_length=10)),
                ('trdgPartBA', models.CharField(blank=True, max_length=4)),
                ('costCenter', models.CharField(blank=True, max_length=10)),
                ('order', models.CharField(blank=True, max_length=10)),
                ('profitCenter', models.CharField(blank=True, max_length=10)),
                ('wbsElement', models.CharField(blank=True, max_length=20)),
                ('network1', models.CharField(max_length=10)),
                ('purchasingDoc1', models.CharField(max_length=10)),
                ('quantity1', models.CharField(max_length=5)),
                ('assignment', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=200)),
                ('pstKey', models.CharField(max_length=2)),
                ('accountBottom', models.CharField(max_length=100)),
            ],
        ),
    ]
