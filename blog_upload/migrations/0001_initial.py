# Generated by Django 3.2.8 on 2022-02-02 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('otp_user', models.CharField(max_length=4)),
            ],
        ),
    ]
