# Generated by Django 2.0 on 2018-02-15 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('code', models.CharField(max_length=8)),
                ('pre_req1', models.CharField(max_length=32)),
                ('pre_req2', models.CharField(max_length=32)),
                ('pre_req3', models.CharField(max_length=32)),
                ('taken', models.BooleanField()),
                ('elig', models.BooleanField()),
            ],
        ),
    ]
