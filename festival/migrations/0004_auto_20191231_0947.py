# Generated by Django 2.2.8 on 2019-12-31 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0003_request_scene_slot'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sceneslot',
            options={'verbose_name': 'Сцена - временной слот', 'verbose_name_plural': 'Сцены и временные слоты'},
        ),
        migrations.AlterModelOptions(
            name='timeslot',
            options={'verbose_name': 'Временной слот', 'verbose_name_plural': 'Временные слоты'},
        ),
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.BooleanField(blank=True, null=True, verbose_name='Статус заявки'),
        ),
    ]
