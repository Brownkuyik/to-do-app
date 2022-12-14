# Generated by Django 3.2.15 on 2022-08-17 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image', models.FileField(upload_to='files/')),
                ('description', models.TextField(default='')),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('isbn', models.CharField(max_length=120, unique=True)),
                ('is_published', models.BooleanField(default=True)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
