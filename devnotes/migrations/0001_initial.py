# Generated by Django 2.2 on 2019-10-09 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devnote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
