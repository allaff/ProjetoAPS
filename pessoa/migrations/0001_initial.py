# Generated by Django 4.1.1 on 2022-10-06 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('data_nascimento', models.DateField(null=True)),
                ('ativa', models.BooleanField(default=True)),
            ],
        ),
    ]
