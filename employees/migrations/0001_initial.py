# Generated by Django 4.0.4 on 2022-06-01 19:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addresses', '0001_initial'),
        ('contracts', '0001_initial'),
        ('personal_documents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(code=400, message='The phone number must follow the format: (xx) 9xxxx-xxxx', regex='^\\([1-9]{2}\\) 9[1-9][0-9]{3}-[0-9]{4}$')])),
                ('personal_code', models.CharField(max_length=6, unique=True, validators=[django.core.validators.RegexValidator(code=400, message='the personal code is a string with six numbers, format: xxxxxx', regex='^[0-9]{6}')])),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to='addresses.address')),
                ('contract', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contracts.contract')),
                ('personal_documents', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personal_documents.personal_document')),
            ],
        ),
    ]
