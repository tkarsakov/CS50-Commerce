# Generated by Django 4.2 on 2023-06-18 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_alter_auctionlisting_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlisting',
            name='category',
        ),
        migrations.RemoveField(
            model_name='auctionlisting',
            name='is_closed',
        ),
    ]