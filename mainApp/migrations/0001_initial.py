# Generated by Django 3.0.3 on 2020-11-07 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.URLField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.URLField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='BrowseBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('photo', models.URLField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='CupCakes_and_Brownie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('Description', models.CharField(max_length=512)),
                ('cake_photo', models.URLField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='CustomizeOrderTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=128)),
                ('Phone', models.CharField(max_length=128)),
                ('Details', models.CharField(max_length=1024, null=True)),
                ('Email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DesignerCakes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cake_title', models.CharField(max_length=128)),
                ('Description', models.CharField(max_length=512)),
                ('cake_photo', models.URLField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='DryCakes_and_Cookie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('Description', models.CharField(max_length=512)),
                ('cake_photo', models.URLField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Flavours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Flavour_title', models.CharField(max_length=128)),
                ('Description', models.CharField(max_length=512)),
                ('cake_photo', models.URLField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoCakes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cake_title', models.CharField(max_length=128)),
                ('Description', models.CharField(max_length=512)),
                ('cake_photo', models.URLField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='PremiumTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cake_title', models.CharField(max_length=128)),
                ('Description', models.CharField(max_length=512)),
                ('cake_photo', models.URLField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='shakes_and_Smoothie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('Description', models.CharField(max_length=512)),
                ('cake_photo', models.URLField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.URLField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='SomethingElse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('photo', models.URLField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='FlavouredCake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('Description', models.CharField(max_length=155)),
                ('cake_photo', models.URLField(max_length=10000)),
                ('price', models.CharField(max_length=50)),
                ('cut_price', models.CharField(max_length=50)),
                ('flavour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Flavours')),
            ],
        ),
    ]
