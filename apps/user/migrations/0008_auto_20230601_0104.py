from django.db import migrations

PROVINCIAS_ARGENTINA = [
    'Buenos Aires',
    'Catamarca',
    'Chaco',
    'Chubut',
    'Córdoba',
    'Corrientes',
    'Entre Ríos',
    'Formosa',
    'Jujuy',
    'La Pampa',
    'La Rioja',
    'Mendoza',
    'Misiones',
    'Neuquén',
    'Río Negro',
    'Salta',
    'San Juan',
    'San Luis',
    'Santa Cruz',
    'Santa Fe',
    'Santiago del Estero',
    'Tierra del Fuego',
    'Tucumán',
    'Ciudad Autónoma de Buenos Aires'
]

def create_locations(apps, schema_editor):
    Location = apps.get_model('user', 'Location')
    for provincia in PROVINCIAS_ARGENTINA:
        Location.objects.create(name=provincia)

class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_location_alter_user_location'),
    ]

    operations = [
        migrations.RunPython(create_locations),
    ]
