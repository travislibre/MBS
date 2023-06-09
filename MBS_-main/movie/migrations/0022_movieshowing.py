# Generated by Django 4.2 on 2023-04-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0021_delete_paymentinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieShowing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theater', models.CharField(choices=[('AMC Theaters', 'Lubbock Theater'), ('Regal Cinemas', 'Amarillo Theater'), ('Cineplex Odeon', 'Levelland Theater'), ('Cinemark Theaters', 'Plainview Theater'), ('Landmark Theatres', 'Snyder Theater'), ('Alamo Drafthouse Cinema', 'Abilene Theater')], max_length=50)),
                ('showtime', models.CharField(choices=[('10:00 AM', '10:00 AM'), ('12:00 PM', '12:00 PM'), ('2:00 PM', '2:00 PM'), ('4:00 PM', '4:00 PM'), ('6:00 PM', '6:00 PM'), ('8:00 PM', '8:00 PM')], max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
