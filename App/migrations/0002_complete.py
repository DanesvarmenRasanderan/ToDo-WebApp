# Generated by Django 3.1.2 on 2020-10-06 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='complete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete_date', models.DateTimeField()),
                ('text1', models.CharField(max_length=200)),
            ],
        ),
    ]
