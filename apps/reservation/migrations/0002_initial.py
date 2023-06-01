# Generated by Django 4.0 on 2023-05-31 17:45

import apps.reservation.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apps_usermanagement', '0001_initial'),
        ('apps_reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_reservations', to='apps_usermanagement.customuser', validators=[apps.reservation.models.validate_owner]),
        ),
        migrations.AddField(
            model_name='reservation',
            name='sitter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sitter_reservations', to='apps_usermanagement.customuser', validators=[apps.reservation.models.validate_sitter]),
        ),
    ]
