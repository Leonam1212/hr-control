# Generated by Django 4.0.4 on 2022-05-24 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='contract',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='contracts.contract'),
        ),
    ]
