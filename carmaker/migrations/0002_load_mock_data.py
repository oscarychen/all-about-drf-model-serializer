# Generated by Django 4.1 on 2022-12-16 04:04

from django.db import migrations


def make_data(apps, schema_editor):
    Manufacturer = apps.get_model('carmaker', 'Manufacturer')
    buick = Manufacturer.objects.create(name="Buick")

    Engine = apps.get_model('carmaker', 'Engine')
    engine_27 = Engine.objects.create(name='Model D Inline-4', displacement=2.7)
    engine_28 = Engine.objects.create(name='Chevrolet Inline-4', displacement=2.8)

    Project = apps.get_model('carmaker', 'Project')
    project = Project.objects.create(code_name="project-d-35-roadster")

    VehicleModel = apps.get_model('carmaker', 'VehicleModel')
    vm_d_35 = VehicleModel.objects.create(model='Buick D-35 Roadster', year=1917, project=project, maker=buick,
                                          predecessor=None)
    vm_d_35.engine_options.add(engine_27, engine_28)

    Vehicle = apps.get_model('carmaker', 'Vehicle')
    Vehicle.objects.create(VIN="A123456789", model=vm_d_35)

    Engineer = apps.get_model('carmaker', 'Engineer')
    engineer = Engineer.objects.create(name='Yoshida')
    engineer.works_on.add(vm_d_35)


class Migration(migrations.Migration):
    dependencies = [
        ('carmaker', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(make_data)
    ]