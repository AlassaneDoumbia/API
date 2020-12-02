# Generated by Django 3.1.3 on 2020-11-05 16:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partenaires', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('MsgId', models.CharField(default='', max_length=100)),
                ('creDtTm', models.DateTimeField(auto_now_add=True)),
                ('NbOfTxs', models.IntegerField()),
                ('ctrlSum', models.BigIntegerField()),
                ('flwInd', models.CharField(blank=True, default='SIMULATOR', max_length=100)),
                ('prvtDtInf', models.CharField(blank=True, default='CANALABBA1', max_length=100)),
                ('cdOrPrtry', models.CharField(blank=True, default='CHANNEL', max_length=100)),
                ('pmtInfId', models.CharField(default='', max_length=100)),
                ('pmtMtd', models.CharField(default='', max_length=100)),
                ('btchBookg', models.IntegerField()),
                ('pmtInf_NbOfTxs', models.BigIntegerField()),
                ('pmtInf_ctrlSum', models.BigIntegerField()),
                ('ordrPrties_Tp', models.CharField(default='', max_length=100)),
                ('ordrPrties_Md', models.CharField(default='', max_length=100)),
                ('reqdExctnDt', models.DateField()),
                ('pmtId_InstrId', models.CharField(default='', max_length=100)),
                ('pmtId_EndToEndId', models.CharField(default='', max_length=100)),
                ('pmtTpInf_InstrPrty', models.CharField(default='', max_length=100)),
                ('pmtTpInf_Prtry', models.CharField(default='', max_length=100)),
                ('InstdAmt', models.BigIntegerField()),
                ('cdtr_Nm', models.CharField(default='', max_length=100)),
                ('cdtrAcct_id', models.BigIntegerField()),
                ('cdtrAcct_SchmeNm', models.CharField(default='', max_length=100)),
                ('rmtInf', models.CharField(default='', max_length=100)),
                ('status', models.CharField(choices=[('PAS TRAITER', 'PAS TRAITER'), ('TRAITER', 'TRAITER')], default='PAS TRAITER', max_length=20)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('partenaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partenaires.partenaire')),
            ],
            options={
                'ordering': ['create_at'],
            },
        ),
    ]