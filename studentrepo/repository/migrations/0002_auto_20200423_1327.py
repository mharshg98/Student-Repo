# Generated by Django 2.2.6 on 2020-04-23 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('title', models.CharField(default='', max_length=100)),
                ('subtitle', models.CharField(default='', max_length=100)),
                ('Class', models.CharField(default='', max_length=10)),
                ('stream', models.CharField(default='', max_length=50)),
                ('subject', models.CharField(default='', max_length=50)),
                ('url', models.CharField(max_length=300)),
                ('date', models.DateField(default='2020-04-01')),
            ],
        ),
        migrations.DeleteModel(
            name='Uploads',
        ),
    ]