# Generated by Django 4.1 on 2022-09-23 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='regform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('disc', models.CharField(max_length=50)),
                ('date', models.DateField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
    ]