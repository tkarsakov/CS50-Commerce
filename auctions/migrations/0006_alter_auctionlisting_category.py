# Generated by Django 4.2 on 2023-06-18 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auctionlisting_category_auctionlisting_is_closed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='category',
            field=models.CharField(default='Goods', max_length=30),
        ),
    ]