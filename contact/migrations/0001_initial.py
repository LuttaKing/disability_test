# Generated by Django 2.2.10 on 2021-03-01 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=80)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('date_sent', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('viewed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-date_sent'],
            },
        ),
    ]
