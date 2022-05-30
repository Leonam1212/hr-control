# Generated by Django 4.0.4 on 2022-05-30 15:22

from django.db import migrations
from dotenv import load_dotenv
from os import getenv

from accounts.serializers import AccountSerializer

load_dotenv()


def default_account(apps, schema_editor):
    Account = apps.get_model("accounts", "Account")

    default_data = {
        "email": getenv("DEFAULT_ADM_EMAIL"),
        "password": getenv("DEFAULT_ADM_PASSWORD"),
    }

    serialized = AccountSerializer(data=default_data)
    serialized.is_valid(True)

    account = Account.objects.create(**serialized.validated_data)
    account.set_password(serialized.validated_data["password"])
    account.save()

class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [migrations.RunPython(default_account)]
