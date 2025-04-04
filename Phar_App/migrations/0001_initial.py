# Generated by Django 4.2.20 on 2025-04-04 06:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CMS_App', '0002_doctor_is_active_labtechnician_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicineStock',
            fields=[
                ('stock_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('restock_threshold', models.PositiveIntegerField(default=10, help_text='Minimum stock before restock alert')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('medicine', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='CMS_App.medicine')),
            ],
        ),
    ]
