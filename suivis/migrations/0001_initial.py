# Generated by Django 3.1.3 on 2020-11-05 16:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ordres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suivi',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('libelle', models.CharField(default='', max_length=100)),
                ('status', models.CharField(choices=[('EN COURS', 'EN COURS'), ('BLOQUÉ', 'BLOQUÉ'), ('FINI', 'FINI')], default='EN COURS', max_length=20)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('ordre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordres.ordre')),
            ],
            options={
                'ordering': ['create_at'],
            },
        ),
    ]
