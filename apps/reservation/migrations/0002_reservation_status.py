# Generated by Django 4.0 on 2023-06-02 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('S', 'Solicitada'), ('A', 'Aceptada'), ('R', 'Rechazada'), ('C', 'Cancelada')], default='S', max_length=1),
        ),
    ]
