# Generated by Django 3.1.2 on 2020-11-16 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WaitlistEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('first_name', models.CharField(max_length=250, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=250, verbose_name='Second Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('notes', models.TextField(verbose_name='Notes')),
                ('level', models.CharField(choices=[('PRI', 'PRI'), ('SEC', 'SEC'), ('CAMPUS', 'CAMPUS')], default='SEC', max_length=255, verbose_name='Level')),
            ],
            options={
                'verbose_name_plural': 'Waitlist Entries',
            },
        ),
    ]
