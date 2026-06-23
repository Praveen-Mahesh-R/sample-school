# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceAttendanceassign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attendance_head_id', models.IntegerField()),
                ('exam_child_id', models.IntegerField()),
                ('grade_section_id', models.IntegerField()),
            ],
            options={
                'db_table': 'attendance_attendanceassign',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttendanceAttendanceassignBk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attendance_head_id', models.IntegerField()),
                ('grade_section_id', models.IntegerField()),
                ('exam_child_id', models.IntegerField()),
                ('working_day', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'attendance_attendanceassign_bk',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttendanceAttendanceentryBk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attendance_assign_id', models.IntegerField()),
                ('student_detail_id', models.IntegerField()),
                ('present_day', models.FloatField(null=True, blank=True)),
                ('total_working_days', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'attendance_attendanceentry_bk',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttendanceAttendancehead',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('sequence', models.IntegerField()),
            ],
            options={
                'db_table': 'attendance_attendancehead',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttendanceAttendanceheadBk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=25)),
            ],
            options={
                'db_table': 'attendance_attendancehead_bk',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttendanceBiometricattendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('in_time', models.TimeField(null=True, blank=True)),
                ('out_time', models.TimeField(null=True, blank=True)),
                ('work_duration', models.TimeField(null=True, blank=True)),
                ('over_time', models.TimeField(null=True, blank=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('status', models.CharField(max_length=15)),
                ('grade_section_id', models.IntegerField(null=True, blank=True)),
                ('staff_detail_id', models.IntegerField(null=True, blank=True)),
                ('student_detail_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'attendance_biometricattendance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttendanceHolidaydetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('is_working', models.IntegerField()),
                ('reason', models.CharField(max_length=1000, null=True, blank=True)),
                ('full_day', models.IntegerField()),
                ('morning_status', models.IntegerField()),
                ('afternoon_status', models.IntegerField()),
                ('academic_year_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'attendance_holidaydetails',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttendanceHolidaydetailsGradeSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('holidaydetails_id', models.IntegerField()),
                ('unitgradesection_id', models.IntegerField()),
            ],
            options={
                'db_table': 'attendance_holidaydetails_grade_section',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttendanceLeavedetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date1', models.DateField()),
                ('reason', models.CharField(max_length=500, null=True, blank=True)),
                ('leave_date', models.DateField(null=True, blank=True)),
                ('remark', models.CharField(max_length=500, null=True, blank=True)),
                ('status', models.IntegerField()),
                ('leave_type_id', models.IntegerField(null=True, blank=True)),
                ('user_from_id', models.IntegerField()),
                ('user_to_id', models.IntegerField()),
            ],
            options={
                'db_table': 'attendance_leavedetails',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttendanceLeavehead',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=25)),
                ('leave_status', models.IntegerField()),
            ],
            options={
                'db_table': 'attendance_leavehead',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttendanceMonthlyattendanceentry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('working_days', models.DecimalField(max_digits=5, decimal_places=2)),
                ('present_days', models.DecimalField(max_digits=5, decimal_places=2)),
                ('attendance_head_id', models.IntegerField()),
                ('grade_section_id', models.IntegerField()),
                ('student_detail_id', models.IntegerField()),
            ],
            options={
                'db_table': 'attendance_monthlyattendanceentry',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttendanceSchoolholidays',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('is_working', models.IntegerField()),
                ('reason', models.CharField(max_length=1000, null=True, blank=True)),
                ('full_day', models.IntegerField()),
                ('morning_status', models.IntegerField()),
                ('afternoon_status', models.IntegerField()),
                ('second_saturday_leave', models.IntegerField()),
                ('fourth_saturday_leave', models.IntegerField()),
                ('academic_year_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'attendance_schoolholidays',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttendanceStaffdailyattendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('absent_detail', models.CharField(max_length=255)),
                ('reason', models.CharField(max_length=500)),
                ('leave_head_id', models.IntegerField(null=True, blank=True)),
                ('staff_id', models.IntegerField()),
            ],
            options={
                'db_table': 'attendance_staffdailyattendance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttendanceStaffholidaydetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('is_working', models.IntegerField()),
                ('reason', models.CharField(max_length=1000, null=True, blank=True)),
                ('full_day', models.IntegerField()),
                ('morning_status', models.IntegerField()),
                ('afternoon_status', models.IntegerField()),
                ('academic_year_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'attendance_staffholidaydetails',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttendanceStaffleavehead',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('sleave_status', models.IntegerField()),
            ],
            options={
                'db_table': 'attendance_staffleavehead',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttendanceStudentattendanceentry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('absent_detail', models.CharField(max_length=15)),
                ('reason', models.CharField(max_length=1000)),
                ('grade_section_id', models.IntegerField()),
                ('leave_head_id', models.IntegerField(null=True, blank=True)),
                ('student_detail_id', models.IntegerField()),
            ],
            options={
                'db_table': 'attendance_studentattendanceentry',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_id', models.IntegerField()),
                ('permission_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('content_type_id', models.IntegerField()),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
    ]
