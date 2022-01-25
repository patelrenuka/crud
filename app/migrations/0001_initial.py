# Generated by Django 2.0 on 2022-01-03 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=220)),
                ('Email', models.EmailField(max_length=254, unique='True')),
                ('Password', models.CharField(default='', max_length=220)),
            ],
        ),
    ]