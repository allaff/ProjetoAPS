# Generated by Django 4.1.2 on 2022-10-27 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_alter_usuario_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='endereco',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
