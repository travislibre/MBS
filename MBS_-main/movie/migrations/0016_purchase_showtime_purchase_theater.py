# Generated by Django 4.2 on 2023-04-23 20:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0015_creditcardform_debitcardform_paypalform_purchase_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='showtime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='purchase',
            name='theater',
            field=models.CharField(default='Unknown Theater', max_length=20),
        ),
    ]
