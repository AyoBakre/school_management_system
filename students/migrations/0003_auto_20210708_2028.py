# Generated by Django 3.2.2 on 2021-07-08 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_classname_class_in_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_teachers', models.CharField(choices=[('Mr Kesh', 'Mr Kesh'), ('Miss Moyo', 'Miss Moyo'), ('Mr Bukky', 'Mr Bukky'), ('Mr NathDare', 'Mr NathDare'), ('Mr Dare', 'Mr Dare'), ('Miss Magaret', 'Miss Magaret'), ('Mrs Onodare', 'Mrs Onodare')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('SCIENCE', 'Science'), ('ART', 'Art'), ('COMMERCIAL', 'Commercial')], max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='biodata',
            name='class_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='students.classname'),
        ),
        migrations.AddField(
            model_name='biodata',
            name='class_teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='students.classteacher'),
        ),
        migrations.AddField(
            model_name='biodata',
            name='dept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='students.department'),
        ),
    ]
