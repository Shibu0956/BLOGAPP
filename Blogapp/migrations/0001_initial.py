# Generated by Django 5.0.1 on 2024-06-22 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myblog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=250)),
                ('Image', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'db_table': 'Myblog',
            },
        ),
    ]
