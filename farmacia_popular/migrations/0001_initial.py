# Generated by Django 3.2.19 on 2023-05-20 17:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmacia_popular',
            fields=[
                ('id_client', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Numero_COO', models.IntegerField()),
                ('Data_Vendas', models.CharField(max_length=255)),
                ('CPF', models.IntegerField()),
                ('Auto_MS', models.IntegerField()),
            ],
        ),
    ]
