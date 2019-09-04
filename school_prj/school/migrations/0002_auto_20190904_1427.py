# Generated by Django 2.2.2 on 2019-09-04 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citymodel',
            name='school',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='schools', to='school.SchoolModel'),
        ),
        migrations.AlterField(
            model_name='citymodel',
            name='student',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='school.StudentModel'),
        ),
    ]
