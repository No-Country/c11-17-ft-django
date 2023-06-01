# Generated by Django 4.0 on 2023-05-31 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apps_dog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dog_reservations', to='apps_dog.dog')),
            ],
        ),
    ]
