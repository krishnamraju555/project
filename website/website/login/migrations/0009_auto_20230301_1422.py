# Generated by Django 3.0.5 on 2023-03-01 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_rename_student_perfomance_student_performance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_performance',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
