# Generated by Django 4.1.2 on 2022-10-27 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_alter_usuario_telefone_delete_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]