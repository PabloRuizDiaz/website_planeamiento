# Generated by Django 3.2.2 on 2022-10-08 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reporteTxModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('tipo', models.CharField(choices=[('TAB', 'Tableau'), ('PBI', 'Power BI')], default='TAB', max_length=3)),
                ('url_pwbi', models.CharField(blank=True, max_length=500, null=True)),
                ('site', models.CharField(blank=True, default='PlaneacindeRed', max_length=30, null=True)),
                ('user_auth', models.CharField(blank=True, max_length=8, null=True)),
                ('view_id', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.TextField()),
                ('visitas', models.IntegerField(default=0)),
                ('publicar', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'WEB_REPORTETX',
            },
        ),
    ]
