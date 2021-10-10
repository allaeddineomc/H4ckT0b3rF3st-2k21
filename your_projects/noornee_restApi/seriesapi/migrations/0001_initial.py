# Generated by Django 3.2.6 on 2021-10-10 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('duration', models.CharField(default='1hr', max_length=50)),
                ('genre', models.CharField(choices=[('Action', 'action'), ('Horror', 'horror'), ('Comedy', 'comedy'), ('Animation', 'animation'), ('Adventure', 'adventure')], max_length=50)),
                ('rating', models.FloatField()),
                ('number_of_episodes', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
