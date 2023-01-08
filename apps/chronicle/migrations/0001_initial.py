# Generated by Django 3.2.16 on 2023-01-08 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('pc', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Chronicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('current_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='VampireClan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='VampireCC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('embrace_date', models.DateTimeField()),
                ('character', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chronicle.character')),
                ('clan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chronicle.vampireclan')),
                ('sire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vampire_sire', to='chronicle.character')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HumanCC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateTimeField()),
                ('character', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chronicle.character')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CharacterRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feeling', models.CharField(choices=[('Love', (('lover', 'Lover'), ('married', 'Married'))), ('enemy', 'Enemy'), ('friend', 'Friend')], max_length=10)),
                ('character1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relationship_character1', to='chronicle.character')),
                ('character2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relationship_character2', to='chronicle.character')),
            ],
            options={
                'unique_together': {('character1', 'character2')},
            },
        ),
        migrations.AddField(
            model_name='character',
            name='relationships',
            field=models.ManyToManyField(through='chronicle.CharacterRelationship', to='chronicle.Character'),
        ),
    ]
