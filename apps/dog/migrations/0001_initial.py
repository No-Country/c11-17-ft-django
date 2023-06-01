# Generated by Django 4.0 on 2023-06-01 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0008_auto_20230601_0104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('age', models.IntegerField()),
                ('breed', models.CharField(choices=[('CHIHUAHUA', 'CHIHUAHUA'), ('DOBERMAN', 'DOBERMAN'), ('BORDER COLLIE', 'BORDER COLLIE'), ('GOLDEN RETRIVER', 'GOLDEN RETRIVER'), ('FRENCH POOL', 'FRENCH POOL'), ('FOX TERRIER', 'FOX TERRIER'), ('DALMATA', 'DALMATA'), ('COMÚN', 'COMÚN')], default='CHIHUAHUA', max_length=30)),
                ('photo', models.ImageField(blank=True, default='/dog/dog_avatar.png', null=True, upload_to='')),
                ('dog_owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
    ]
