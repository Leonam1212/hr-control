# Generated by Django 4.0.4 on 2022-06-01 19:27

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_document',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('cpf', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(code=400, message='The cpf must follow the format: xxx.xxx.xxx-xx', regex='[0-9]{3}[\\.][0-9]{3}[\\.][0-9]{3}[-][0-9]{2}$')])),
                ('nit', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(code=400, message='The nit must follow the format: xxx.xxxxx.xx-x', regex='[0-9]{3}[\\.][0-9]{5}[\\.][0-9]{2}[-][0-9]{1}$')])),
                ('rg', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(code=400, message='The rg must follow the format: xx.xxx.xxx-x', regex='[0-9]{2}[\\.][0-9]{3}[\\.][0-9]{3}[-][0-9]{1}$')])),
                ('ctps', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(code=400, message='The cpts must follow the format: xxxxxxx-xxxx', regex='[0-9]{7}[-][0-9]{4}$')])),
                ('cnpj', models.CharField(max_length=20, null=True, unique=True, validators=[django.core.validators.RegexValidator(code=400, message='The cnpj must follow the format: xx.xxx.xxx/xxxx-xx', regex='[0-9]{2}[\\.][0-9]{3}[\\.][0-9]{3}[\\/][0-9]{4}[-][0-9]{2}$')])),
            ],
        ),
    ]
