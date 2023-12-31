# Generated by Django 4.2.1 on 2023-06-27 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirlineTicketReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline_name', models.CharField(max_length=200)),
                ('departure_date', models.DateTimeField()),
                ('arrival_date', models.DateTimeField()),
                ('destination', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CarHire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=200)),
                ('hire_start_date', models.DateField()),
                ('hire_end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='EmbassyBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('embassy_name', models.CharField(max_length=200)),
                ('booking_date', models.DateField()),
                ('preparation_notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PassportVisaConsultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultation_date', models.DateField()),
                ('consultation_notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TravelTour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='HotelBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=200)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('travel_tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.traveltour')),
            ],
        ),
    ]
