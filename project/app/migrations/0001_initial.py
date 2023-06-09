# Generated by Django 4.2 on 2023-05-02 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ru_word', models.CharField(max_length=30)),
                ('en_word', models.CharField(max_length=30)),
                ('pic', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ru_word', models.CharField(max_length=30)),
                ('en_word', models.CharField(max_length=30)),
            ],
        ),
    ]
