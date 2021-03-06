# Generated by Django 3.0.8 on 2020-07-13 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=20, null=True)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
                ('group', models.CharField(choices=[('SA', 'Super Admin'), ('AD', 'Admin'), ('US', 'User')], max_length=2)),
                ('status', models.CharField(choices=[('AC', 'Active'), ('SU', 'Suspended'), ('NV', 'Not Verified')], max_length=2)),
            ],
        ),
    ]
