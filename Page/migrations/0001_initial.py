# Generated by Django 4.0.4 on 2022-05-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FristName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Subject', models.CharField(max_length=200)),
                ('Massage', models.TextField()),
            ],
        ),
    ]
