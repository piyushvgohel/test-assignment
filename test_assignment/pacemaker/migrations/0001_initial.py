# Generated by Django 3.0.2 on 2020-01-26 06:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacemaker',
            fields=[
                ('uuid', models.UUIDField(default=uuid.UUID('2d738756-f698-4acd-adf2-1d838b37fe62'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('model_number', models.TextField()),
                ('dimensions_description', models.TextField()),
            ],
        ),
    ]
