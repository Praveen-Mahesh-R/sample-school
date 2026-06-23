# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AttendanceAttendanceassign(models.Model):
    attendance_head_id = models.IntegerField()
    exam_child_id = models.IntegerField()
    grade_section_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'attendance_attendanceassign'
        unique_together = (('attendance_head_id', 'grade_section_id', 'exam_child_id'),)


class AttendanceAttendanceassignBk(models.Model):
    attendance_head_id = models.IntegerField()
    grade_section_id = models.IntegerField()
    exam_child_id = models.IntegerField()
    working_day = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance_attendanceassign_bk'


class AttendanceAttendanceentryBk(models.Model):
    attendance_assign_id = models.IntegerField()
    student_detail_id = models.IntegerField()
    present_day = models.FloatField(blank=True, null=True)
    total_working_days = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance_attendanceentry_bk'


class AttendanceAttendancehead(models.Model):
    name = models.CharField(unique=True, max_length=50)
    sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'attendance_attendancehead'


class AttendanceAttendanceheadBk(models.Model):
    name = models.CharField(unique=True, max_length=25)

    class Meta:
        managed = False
        db_table = 'attendance_attendancehead_bk'


class AttendanceBiometricattendance(models.Model):
    in_time = models.TimeField(blank=True, null=True)
    out_time = models.TimeField(blank=True, null=True)
    work_duration = models.TimeField(blank=True, null=True)
    over_time = models.TimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=15)
    grade_section_id = models.IntegerField(blank=True, null=True)
    staff_detail_id = models.IntegerField(blank=True, null=True)
    student_detail_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance_biometricattendance'


class AttendanceHolidaydetails(models.Model):
    date = models.DateField(blank=True, null=True)
    is_working = models.IntegerField()
    reason = models.CharField(max_length=1000, blank=True, null=True)
    full_day = models.IntegerField()
    morning_status = models.IntegerField()
    afternoon_status = models.IntegerField()
    academic_year_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance_holidaydetails'


class AttendanceHolidaydetailsGradeSection(models.Model):
    holidaydetails_id = models.IntegerField()
    unitgradesection_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'attendance_holidaydetails_grade_section'
        unique_together = (('holidaydetails_id', 'unitgradesection_id'),)


class AttendanceLeavedetails(models.Model):
    date1 = models.DateField()
    reason = models.CharField(max_length=500, blank=True, null=True)
    leave_date = models.DateField(blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField()
    leave_type_id = models.IntegerField(blank=True, null=True)
    user_from_id = models.IntegerField()
    user_to_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'attendance_leavedetails'
        unique_together = (('user_from_id', 'user_to_id', 'leave_date'),)


class AttendanceLeavehead(models.Model):
    name = models.CharField(unique=True, max_length=25)
    leave_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'attendance_leavehead'


class AttendanceMonthlyattendanceentry(models.Model):
    working_days = models.DecimalField(max_digits=5, decimal_places=2)
    present_days = models.DecimalField(max_digits=5, decimal_places=2)
    attendance_head_id = models.IntegerField()
    grade_section_id = models.IntegerField()
    student_detail_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'attendance_monthlyattendanceentry'


class AttendanceSchoolholidays(models.Model):
    date = models.DateField(blank=True, null=True)
    is_working = models.IntegerField()
    reason = models.CharField(max_length=1000, blank=True, null=True)
    full_day = models.IntegerField()
    morning_status = models.IntegerField()
    afternoon_status = models.IntegerField()
    second_saturday_leave = models.IntegerField()
    fourth_saturday_leave = models.IntegerField()
    academic_year_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance_schoolholidays'


class AttendanceStaffdailyattendance(models.Model):
    date = models.DateField()
    absent_detail = models.CharField(max_length=255)
    reason = models.CharField(max_length=500)
    leave_head_id = models.IntegerField(blank=True, null=True)
    staff_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'attendance_staffdailyattendance'
        unique_together = (('date', 'staff_id'),)


class AttendanceStaffholidaydetails(models.Model):
    date = models.DateField(blank=True, null=True)
    is_working = models.IntegerField()
    reason = models.CharField(max_length=1000, blank=True, null=True)
    full_day = models.IntegerField()
    morning_status = models.IntegerField()
    afternoon_status = models.IntegerField()
    academic_year_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance_staffholidaydetails'


class AttendanceStaffleavehead(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    sleave_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'attendance_staffleavehead'


class AttendanceStudentattendanceentry(models.Model):
    date = models.DateField()
    absent_detail = models.CharField(max_length=15)
    reason = models.CharField(max_length=1000)
    grade_section_id = models.IntegerField()
    leave_head_id = models.IntegerField(blank=True, null=True)
    student_detail_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'attendance_studentattendanceentry'
        unique_together = (('date', 'student_detail_id'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
