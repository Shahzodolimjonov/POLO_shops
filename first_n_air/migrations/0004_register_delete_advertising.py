# Generated by Django 4.2.9 on 2024-02-13 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_n_air', '0003_advertising'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('password', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=32)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Advertising',
        ),
    ]
