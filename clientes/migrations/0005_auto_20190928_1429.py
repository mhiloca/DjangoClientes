# Generated by Django 2.2.5 on 2019-09-28 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_venda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='cliente',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='clientes.Cliente'),
        ),
    ]
