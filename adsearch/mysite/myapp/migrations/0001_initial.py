# Generated by Django 4.0.4 on 2022-05-13 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('ad_url', models.CharField(max_length=255)),
                ('tags', models.ManyToManyField(to='myapp.tag')),
            ],
        ),
    ]
