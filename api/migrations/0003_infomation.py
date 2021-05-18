# Generated by Django 3.1.7 on 2021-04-30 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='classes',
            fields=[
                ('class_id',
                 models.AutoField(primary_key=True,
                                  null=False,
                                  editable=False,
                                  unique=True)),
                ('subject',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='api.subjects')),
                ('teacher',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='api.users'))
            ],
        ),
        migrations.CreateModel(
            name='dates_of_class',
            fields=[
                ('date_class_id',
                 models.AutoField(primary_key=True,
                                  null=False,
                                  editable=False,
                                  unique=True)),
                ('class',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='api.classes')),
                ('date', models.DateTimeField()),
                ('is_checking', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='student_attendances',
            fields=[
                ('student_attendance_id',
                 models.AutoField(primary_key=True,
                                  null=False,
                                  editable=False,
                                  unique=True)),
                ('is_attending', models.BooleanField()),
                ('date_class',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='api.dates_of_class')),
                ('student',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='api.users')),
            ],
        ),
        migrations.CreateModel(
            name='details_student_attend_class',
            fields=[
                ('detail_student_class_id',
                 models.AutoField(primary_key=True,
                                  null=False,
                                  editable=False,
                                  unique=True)),
                ('class',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='api.classes')),
                ('student',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='api.users')),
            ],
        )
    ]
