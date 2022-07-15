# Generated by Django 4.0.6 on 2022-07-15 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=100)),
                ('is_completed', models.BooleanField(default=False)),
                ('last_modified', models.DateField(auto_now=True)),
            ],
        ),
    ]
