# Generated by Django 4.0.4 on 2022-05-31 02:51

from django.db import migrations
import datetime


def default_shifts(apps, schema_editor):
    Shift = apps.get_model("shifts", "Shift")

    mourning_checkin = datetime.time(8, 0, 0).strftime("%H:%M:%S")
    mourning_checkout = datetime.time(11, 50, 0).strftime("%H:%M:%S")
    afternoon_checkin = datetime.time(13, 0, 0).strftime("%H:%M:%S")
    afternoon_checkout = datetime.time(17, 0, 0).strftime("%H:%M:%S")
    nocturnal_checkin = datetime.time(22, 0, 0).strftime("%H:%M:%S")
    nocturnal_checkout = datetime.time(5, 0, 0).strftime("%H:%M:%S")

    shifts_list = [
        {
            "name": "matutino",
            "base_checkin": mourning_checkin,
            "base_checkout": mourning_checkout,
        },
        {
            "name": "vespertino",
            "base_checkin": afternoon_checkin,
            "base_checkout": afternoon_checkout,
        },
        {
            "name": "integral",
            "base_checkin": mourning_checkin,
            "base_checkout": afternoon_checkout,
        },
        {
            "name": "noturno",
            "base_checkin": nocturnal_checkin,
            "base_checkout": nocturnal_checkout,
        },
    ]

    for work_shift in shifts_list:
        Shift.objects.create(**work_shift)


class Migration(migrations.Migration):

    dependencies = [
        ("shifts", "0001_initial"),
    ]

    operations = [migrations.RunPython(default_shifts)]
