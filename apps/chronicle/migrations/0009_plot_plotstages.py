# Generated by Django 3.2.16 on 2023-01-08 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chronicle', '0008_vampirecc_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('chronicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chronicle.chronicle')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlotStages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chronicle.plot')),
            ],
        ),
    ]