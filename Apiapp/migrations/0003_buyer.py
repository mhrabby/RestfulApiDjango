# Generated by Django 3.1.1 on 2020-09-17 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apiapp', '0002_authority'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Buyer_id', models.IntegerField(max_length=20)),
                ('Buyer_name', models.CharField(max_length=20)),
                ('Buyer_Address', models.CharField(max_length=50)),
                ('Iteam', models.CharField(max_length=50)),
                ('Purchased_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
