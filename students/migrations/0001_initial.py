# Generated by Django 3.2.2 on 2021-07-08 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_in_school', models.CharField(choices=[('J1', 'Junior1'), ('J2', 'Junior2'), ('J3', 'Junior3'), ('S1', 'Senior1'), ('S2', 'Senior2'), ('S3', 'Senior3')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='BioData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('middle_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('parent_phone_number', models.IntegerField()),
                ('parent_email', models.EmailField(max_length=254)),
                ('home_address', models.CharField(max_length=50)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='students.classname')),
            ],
        ),
    ]