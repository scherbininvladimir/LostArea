# Generated by Django 2.2.8 on 2019-12-21 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('format', models.CharField(choices=[('S', 'Сольное выступление'), ('G', 'Группа')], max_length=1)),
                ('comment', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.PositiveSmallIntegerField()),
                ('time', models.CharField(choices=[('D', 'День'), ('E', 'Вечер'), ('LE', 'Поздний вечер')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Voice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voice', models.CharField(choices=[('YES', 'За'), ('NO', 'Против'), ('ABS', 'Воздержался')], max_length=2)),
                ('censor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='festival.Request')),
            ],
        ),
        migrations.CreateModel(
            name='SceneSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveSmallIntegerField()),
                ('scene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='festival.Scene')),
                ('timeslot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='festival.TimeSlot')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='desired_scene',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='festival.Scene'),
        ),
    ]