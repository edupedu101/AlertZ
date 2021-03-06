# Generated by Django 4.0.4 on 2022-04-26 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('registro', models.OneToOneField(default=True, on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.registro')),
                ('imagen', models.ImageField(default=False, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=100)),
                ('desc', models.TextField(blank=True, default=None, null=True)),
                ('tipo_sensor', models.CharField(max_length=20)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='registro',
            name='sensor',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.sensor'),
        ),
    ]
