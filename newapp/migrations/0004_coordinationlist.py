# Generated by Django 4.0.5 on 2022-07-26 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_agriculturegoods_instok'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoordinationList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=200)),
                ('detail', models.TextField(default=True)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
    ]
