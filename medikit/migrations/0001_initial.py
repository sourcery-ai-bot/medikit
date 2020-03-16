# Generated by Django 3.0.4 on 2020-03-16 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('expiration_date', models.DateField()),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('kit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drugs', to='medikit.Kit')),
            ],
        ),
    ]