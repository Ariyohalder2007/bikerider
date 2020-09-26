# Generated by Django 3.1.1 on 2020-09-24 09:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='shop/images')),
                ('publish_date', models.DateField(default=django.utils.timezone.now)),
                ('event_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
