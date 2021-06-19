# Generated by Django 3.2.3 on 2021-05-25 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.SmallIntegerField(default=1)),
                ('inventor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.inventory')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('inventorys', models.ManyToManyField(through='blog.Kit', to='blog.Inventory')),
            ],
        ),
        migrations.AddField(
            model_name='kit',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.room'),
        ),
    ]
