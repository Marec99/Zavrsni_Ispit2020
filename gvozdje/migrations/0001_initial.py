# Generated by Django 3.1.4 on 2020-12-31 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gvozdje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=50)),
                ('jedinicaMere', models.CharField(max_length=4)),
                ('cena_DIN', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password1', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mreza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100)),
                ('dimenzijeKocke', models.CharField(max_length=50)),
                ('dimenzije', models.CharField(max_length=50)),
                ('jedinicaMere', models.CharField(max_length=4)),
                ('cena_DIN', models.IntegerField(default=0)),
                ('proizvedeno_Od', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gvozdje.gvozdje')),
            ],
        ),
    ]