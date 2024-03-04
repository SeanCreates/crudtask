# Generated by Django 5.0.2 on 2024-02-28 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Description', models.TextField()),
                ('DueDate', models.DateField()),
                ('Completed', models.BooleanField(default=False)),
            ],
        ),
    ]
