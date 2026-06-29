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
from datetime import date


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


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(default=date.today)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class CaptchaCaptcha(models.Model):
    solution = models.CharField(max_length=32)
    date_generated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'captcha_captcha'


class CommunicationAnnouncement(models.Model):
    content = models.CharField(max_length=150, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    display_status = models.IntegerField(blank=True, null=True)
    created_by_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communication_announcement'


class CommunicationMailinbox(models.Model):
    date = models.DateField(blank=True, null=True)
    subject = models.CharField(max_length=400, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    files_any = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField()
    user_from_id = models.IntegerField()
    user_to_id = models.IntegerField()
    parent_status = models.IntegerField()
    staff_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'communication_mailinbox'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type_id = models.IntegerField(blank=True, null=True)
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


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


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ExamDays(models.Model):
    name = models.CharField(max_length=15, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_days'


class ExamExamOld(models.Model):
    name = models.CharField(unique=True, max_length=50)
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_exam_old'


class ExamExamattendanceassign(models.Model):
    attendance_head_id = models.IntegerField()
    exam_child_id = models.IntegerField()
    grade_section_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'exam_examattendanceassign'
        unique_together = (('attendance_head_id', 'grade_section_id', 'exam_child_id'),)


class ExamExamchild(models.Model):
    exam_head_id = models.IntegerField()
    name = models.CharField(unique=True, max_length=50)
    sequence = models.IntegerField()
    denotes_head = models.IntegerField()
    type = models.CharField(max_length=10)
    print_as = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'exam_examchild'


class ExamExamhead(models.Model):
    name = models.CharField(unique=True, max_length=50)
    sequence = models.IntegerField(blank=True, null=True)
    print_as = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'exam_examhead'


class ExamExammarkentry(models.Model):
    exam_subject_id = models.IntegerField()
    student_detail_id = models.IntegerField()
    mark = models.FloatField(blank=True, null=True)
    practical_mark = models.FloatField(blank=True, null=True)
    remark = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'exam_exammarkentry'


class ExamExamremark(models.Model):
    grade_section_id = models.IntegerField()
    exam_child_id = models.IntegerField()
    student_detail_id = models.IntegerField()
    teacher_remark = models.CharField(max_length=255, blank=True, null=True)
    principal_remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_examremark'


class ExamExamsubject(models.Model):
    exam_child_id = models.IntegerField()
    subject_grade_section_id = models.IntegerField()
    weightage = models.IntegerField()
    pass_mark = models.IntegerField(blank=True, null=True)
    reportcard_weightage = models.IntegerField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    mark_type = models.CharField(max_length=20)
    status = models.IntegerField()
    has_practical = models.IntegerField()
    practical_weightage = models.IntegerField(blank=True, null=True)
    practical_pass_mark = models.IntegerField(blank=True, null=True)
    has_descriptive_indicators = models.IntegerField()
    block_mark_entry = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'exam_examsubject'


class ExamGradeexam(models.Model):
    grade_id = models.IntegerField()
    exam_child_id = models.IntegerField()
    sequence = models.IntegerField(blank=True, null=True)
    academic_year_id = models.IntegerField()
    active_exam = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'exam_gradeexam'
        unique_together = (('grade_id', 'exam_child_id', 'academic_year_id'),)


class ExamGradepointaverage(models.Model):
    grade_section_id = models.IntegerField()
    mark_range = models.CharField(max_length=15)
    gpa = models.CharField(max_length=5)
    lower_range = models.FloatField()
    upper_range = models.FloatField()
    direct_grade = models.IntegerField()
    grade_point = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'exam_gradepointaverage'


class ExamGradesubjectindicator(models.Model):
    indicator_id = models.IntegerField()
    grade_subject_id = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'exam_gradesubjectindicator'
        unique_together = (('indicator_id', 'grade_subject_id'),)


class ExamIndicator(models.Model):
    name = models.CharField(max_length=300)
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_indicator'


class ExamPeriod(models.Model):
    name = models.CharField(max_length=15, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_period'


class ExamReportcardchoice(models.Model):
    reportcard_name = models.CharField(max_length=255)
    grade_id = models.IntegerField()
    exam_head_id = models.IntegerField(blank=True, null=True)
    exam_child_id = models.IntegerField(blank=True, null=True)
    academic_year_id = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'exam_reportcardchoice'
        unique_together = (('grade_id', 'exam_head_id', 'academic_year_id'),)


class ExamStudentmarkindicator(models.Model):
    exam_mark_id = models.IntegerField()
    indicator_id = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'exam_studentmarkindicator'


class ExamSubjectcategory(models.Model):
    subject_part_id = models.IntegerField()
    name_id = models.IntegerField()
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_subjectcategory'


class ExamSubjectchild(models.Model):
    subject_head_id = models.IntegerField()
    name_id = models.IntegerField()
    print_as = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_subjectchild'


class ExamSubjectgrade(models.Model):
    subject_child_id = models.IntegerField()
    grade_section_id = models.IntegerField()
    sequence = models.IntegerField(blank=True, null=True)
    mark_type = models.CharField(max_length=20)
    remark_subject = models.IntegerField()
    flag = models.IntegerField()
    is_main_subject = models.IntegerField()
    is_upgrading_subject = models.IntegerField()
    code = models.CharField(max_length=20, blank=True, null=True)
    has_practical = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'exam_subjectgrade'
        unique_together = (('subject_child_id', 'grade_section_id'),)


class ExamSubjecthead(models.Model):
    subject_category_id = models.IntegerField()
    name_id = models.IntegerField()
    print_as = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_subjecthead'


class ExamSubjectindicator(models.Model):
    indicator_id = models.IntegerField()
    subject_child_id = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'exam_subjectindicator'


class ExamSubjectmaster(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'exam_subjectmaster'


class ExamSubjectpart(models.Model):
    name_id = models.IntegerField()
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_subjectpart'


class ExamTimetable(models.Model):
    day = models.ForeignKey(ExamDays)
    grde_subject_id = models.IntegerField(blank=True, null=True)
    period_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'exam_timetable'
        unique_together = (('day', 'period_id', 'grde_subject_id'),)


class FeesCcavenuehdfc(models.Model):
    student_detail_id = models.IntegerField()
    order_detail = models.CharField(max_length=300, blank=True, null=True)
    invoice_details = models.CharField(max_length=300, blank=True, null=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    student_request = models.CharField(max_length=5000, blank=True, null=True)
    student_response = models.CharField(max_length=5000, blank=True, null=True)
    order_status = models.CharField(max_length=300, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fees_ccavenuehdfc'


class FeesFeecalender(models.Model):
    name = models.CharField(max_length=25)
    is_working = models.IntegerField()
    academic_year_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fees_feecalender'


class FeesFeecertificatenumberpattern(models.Model):
    prefix = models.CharField(max_length=255, blank=True, null=True)
    suffix = models.CharField(max_length=255, blank=True, null=True)
    numbertobegin = models.CharField(max_length=255)
    status = models.IntegerField()
    next_fee_certificate_number = models.CharField(max_length=255)
    academic_year_id = models.IntegerField()
    unit_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fees_feecertificatenumberpattern'


class FeesFeedefinition(models.Model):
    fee_description = models.CharField(max_length=25)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateField()
    fees_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fees_feedefinition'
        unique_together = (('fees_id', 'date', 'amount'),)


class FeesFeedetails(models.Model):
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateField()
    fee_definition_id = models.IntegerField()
    fees_id = models.IntegerField()
    grade_section_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fees_feedetails'
        unique_together = (('fees_id', 'grade_section_id', 'date'),)


class FeesFees(models.Model):
    print_as = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    is_optional = models.IntegerField()
    apply_for = models.CharField(max_length=20)
    fees_master_id = models.IntegerField()
    fees_type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fees_fees'


class FeesFeescertificatechoice(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True, null=True)
    academic_year_id = models.IntegerField(blank=True, null=True)
    grade_section_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fees_feescertificatechoice'


class FeesFeesmaster(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'fees_feesmaster'


class FeesFeestype(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'fees_feestype'


class FeesInvoice(models.Model):
    invoice_number = models.CharField(unique=True, max_length=25)
    invoice_date = models.DateField()
    invoice_amount = models.DecimalField(max_digits=9, decimal_places=2)
    total_due = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=9, decimal_places=2)
    concession = models.DecimalField(max_digits=9, decimal_places=2)
    amount_received = models.DecimalField(max_digits=9, decimal_places=2)
    paid_status = models.CharField(max_length=20)
    remarks = models.CharField(max_length=255)
    status = models.IntegerField()
    online_order_number = models.CharField(max_length=50, blank=True, null=True)
    canceled_reason = models.CharField(max_length=2000)
    canceled_date = models.DateField(blank=True, null=True)
    updated_date_time = models.DateTimeField(blank=True, null=True)
    academic_year_id = models.IntegerField()
    account_id = models.IntegerField(blank=True, null=True)
    grade_section_id = models.IntegerField()
    student_master_id = models.IntegerField()
    term_id = models.IntegerField()
    updated_by_id = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fees_invoice'


class FeesInvoicedetail(models.Model):
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.DecimalField(max_digits=9, decimal_places=2)
    concession = models.DecimalField(max_digits=9, decimal_places=2)
    account_id = models.IntegerField(blank=True, null=True)
    fees_id = models.IntegerField()
    invoice_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fees_invoicedetail'
        unique_together = (('fees_id', 'invoice_id'),)


class FeesInvoicenumberpattern(models.Model):
    prefix = models.CharField(max_length=255, blank=True, null=True)
    suffix = models.CharField(max_length=255, blank=True, null=True)
    numbertobegin = models.CharField(max_length=255)
    status = models.IntegerField()
    next_invoice_number = models.CharField(max_length=255)
    academic_year_id = models.IntegerField()
    account_id = models.IntegerField(blank=True, null=True)
    unit_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fees_invoicenumberpattern'


class FeesLatefine(models.Model):
    type = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    initial_month_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    academic_year_id = models.IntegerField()
    grade_id = models.IntegerField(blank=True, null=True)
    unit_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fees_latefine'


class FeesPaymentmaster(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'fees_paymentmaster'


class FeesPaymentterm(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    close_date = models.DateField()
    search_date1 = models.DateField()
    search_date2 = models.DateField()
    description = models.CharField(max_length=250)
    no_of_transport_month = models.IntegerField(blank=True, null=True)
    academic_year_id = models.IntegerField()
    payment_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fees_paymentterm'


class FeesPrintsettings(models.Model):
    page_size = models.CharField(max_length=10)
    invoice_copy = models.CharField(max_length=10)
    receipt_copy = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'fees_printsettings'


class FeesReceipt(models.Model):
    receipt_number = models.CharField(unique=True, max_length=25)
    receipt_date = models.DateField()
    cheque_number = models.CharField(max_length=255, blank=True, null=True)
    cheque_date = models.DateField(blank=True, null=True)
    cheque_status = models.CharField(max_length=20)
    dd_number = models.CharField(max_length=255, blank=True, null=True)
    dd_date = models.DateField(blank=True, null=True)
    online_transaction_number = models.CharField(max_length=255, blank=True, null=True)
    receipt_amount = models.DecimalField(max_digits=9, decimal_places=2)
    actual_paid = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.DecimalField(max_digits=9, decimal_places=2)
    concession = models.DecimalField(max_digits=9, decimal_places=2)
    paid_status = models.CharField(max_length=20)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    canceled_reason = models.CharField(max_length=2000, blank=True, null=True)
    reason = models.CharField(max_length=2000, blank=True, null=True)
    canceled_date = models.DateField(blank=True, null=True)
    updated_date_time = models.DateTimeField(blank=True, null=True)
    late_fine = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    amount_by_cash = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    amount_by_cheque = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    amount_by_dd = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    amount_by_online = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    print_status = models.IntegerField()
    account_id = models.IntegerField(blank=True, null=True)
    cheque_bank_id = models.IntegerField(blank=True, null=True)
    dd_bank_id = models.IntegerField(blank=True, null=True)
    online_order_number = models.CharField(max_length=250, blank=True, null=True)
    online_payment_status = models.CharField(max_length=250, blank=True, null=True)
    online_payment_status_message = models.CharField(max_length=250, blank=True, null=True)
    online_bank_ref_no = models.CharField(max_length=250, blank=True, null=True)
    invoice_id = models.IntegerField()
    online_bank_id = models.IntegerField(blank=True, null=True)
    updated_by_id = models.IntegerField(unique=True, blank=True, null=True)
    cancel_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fees_receipt'


class FeesReceiptdetail(models.Model):
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    online_order_number = models.CharField(max_length=50, blank=True, null=True)
    discount = models.DecimalField(max_digits=9, decimal_places=2)
    concession = models.DecimalField(max_digits=9, decimal_places=2)
    status = models.IntegerField()
    account_id = models.IntegerField(blank=True, null=True)
    fees_id = models.IntegerField()
    invoice_detail_id = models.IntegerField()
    receipt_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fees_receiptdetail'
        unique_together = (('fees_id', 'invoice_detail_id', 'receipt_id'),)


class FeesReceiptnumberpattern(models.Model):
    prefix = models.CharField(max_length=255, blank=True, null=True)
    suffix = models.CharField(max_length=255, blank=True, null=True)
    numbertobegin = models.CharField(max_length=255)
    status = models.IntegerField()
    next_receipt_number = models.CharField(max_length=255)
    academic_year_id = models.IntegerField()
    account_id = models.IntegerField(blank=True, null=True)
    unit_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fees_receiptnumberpattern'


class FeesStudentfeescertificate(models.Model):
    prefix = models.CharField(max_length=255, blank=True, null=True)
    suffix = models.CharField(max_length=255, blank=True, null=True)
    certificate_number = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    status = models.IntegerField()
    print_status = models.IntegerField()
    academic_year_id = models.IntegerField()
    student_detail_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fees_studentfeescertificate'


class FeesStudentfeescertificatechoice(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True, null=True)
    academic_year_id = models.IntegerField(blank=True, null=True)
    grade_section_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fees_studentfeescertificatechoice'


class FeesStudentfeescertificatedetail(models.Model):
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    receipt_detail_id = models.IntegerField()
    student_fees_certificate_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fees_studentfeescertificatedetail'


class FeesStudentoptionalfees(models.Model):
    fees_id = models.IntegerField()
    grade_section_id = models.IntegerField()
    student_master_id = models.IntegerField()
    term_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fees_studentoptionalfees'


class FeesTermconcessiondetails(models.Model):
    amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    percentage = models.IntegerField(blank=True, null=True)
    concession_id = models.IntegerField()
    fees_id = models.IntegerField()
    term_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fees_termconcessiondetails'
        unique_together = (('term_id', 'concession_id', 'fees_id'),)


class FeesUnitaccount(models.Model):
    academic_year_id = models.IntegerField()
    account_id = models.IntegerField()
    unit_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fees_unitaccount'
        unique_together = (('unit_id', 'account_id', 'academic_year_id'),)


class FeesUnitaccountfees(models.Model):
    fees_master_id = models.IntegerField()
    unit_account_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fees_unitaccountfees'
        unique_together = (('unit_account_id', 'fees_master_id'),)


class LibraryAuthor(models.Model):
    name = models.CharField(unique=True, max_length=250)

    class Meta:
        managed = False
        db_table = 'library_author'


class LibraryIssue(models.Model):
    resource_id = models.IntegerField()
    user_id = models.IntegerField()
    student_id = models.IntegerField(blank=True, null=True)
    staff_id = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField()
    reservation_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=25)
    due_date = models.DateField()
    fineamount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    finepaidstatus = models.IntegerField()
    paid_date = models.DateTimeField(blank=True, null=True)
    returned_date = models.DateTimeField(blank=True, null=True)
    issue_date = models.DateField()
    academic_year_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'library_issue'


class LibraryMediatype(models.Model):
    name = models.CharField(unique=True, max_length=25)

    class Meta:
        managed = False
        db_table = 'library_mediatype'


class LibraryPublisher(models.Model):
    name = models.CharField(unique=True, max_length=250)

    class Meta:
        managed = False
        db_table = 'library_publisher'


class LibraryRenewal(models.Model):
    issue_id = models.IntegerField()
    due_date = models.DateTimeField()
    renewal_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'library_renewal'


class LibraryReservation(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    staff_id = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    resource_id = models.IntegerField()
    status = models.CharField(max_length=25)
    academic_year_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'library_reservation'


class LibraryResource(models.Model):
    barcode = models.CharField(unique=True, max_length=100)
    media_id = models.IntegerField()
    title = models.CharField(max_length=255)
    author_id = models.IntegerField()
    subject_id = models.IntegerField()
    isbn_no = models.CharField(max_length=100, blank=True, null=True)
    call_no = models.CharField(max_length=25, blank=True, null=True)
    publisher_id = models.IntegerField()
    edition = models.IntegerField(blank=True, null=True)
    year_published = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_purchased = models.DateField(blank=True, null=True)
    supplier_id = models.IntegerField(blank=True, null=True)
    no_of_copies = models.IntegerField()
    pages = models.IntegerField()
    status = models.CharField(max_length=25)
    status_remark = models.CharField(max_length=25, blank=True, null=True)
    resource_no = models.IntegerField(unique=True)
    language_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'library_resource'


class LibraryResourceNew(models.Model):
    id = models.IntegerField(primary_key=True)
    barcode = models.CharField(max_length=100)
    media_id = models.IntegerField()
    title = models.CharField(max_length=255)
    author_id = models.IntegerField()
    subject_id = models.IntegerField()
    isbn_no = models.CharField(max_length=100, blank=True, null=True)
    call_no = models.CharField(max_length=25, blank=True, null=True)
    publisher_id = models.IntegerField()
    edition = models.IntegerField(blank=True, null=True)
    year_published = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_purchased = models.DateField(blank=True, null=True)
    supplier_id = models.IntegerField(blank=True, null=True)
    no_of_copies = models.IntegerField()
    pages = models.IntegerField()
    status = models.CharField(max_length=25)
    status_remark = models.CharField(max_length=25, blank=True, null=True)
    resource_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'library_resource_new'


class LibraryResourcebarcode(models.Model):
    barcode = models.CharField(unique=True, max_length=25)
    filename = models.CharField(max_length=100)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'library_resourcebarcode'


class LibrarySettings(models.Model):
    no_of_non_due_days = models.IntegerField()
    fine_type = models.CharField(max_length=25)
    fineamount = models.IntegerField()
    reservation_limit_for_staff = models.IntegerField()
    reservation_limit_for_student = models.IntegerField()
    issue_limit_for_staff = models.IntegerField()
    issue_limit_for_student = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'library_settings'


class LibrarySubject(models.Model):
    subject_category_id = models.IntegerField()
    name = models.CharField(unique=True, max_length=250)

    class Meta:
        managed = False
        db_table = 'library_subject'


class LibrarySubjectcategory(models.Model):
    name = models.CharField(unique=True, max_length=250)

    class Meta:
        managed = False
        db_table = 'library_subjectcategory'


class LibrarySupplier(models.Model):
    short_code = models.CharField(unique=True, max_length=10)
    name = models.CharField(unique=True, max_length=250)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    state = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    postalcode = models.CharField(max_length=10)
    mobile_no = models.CharField(unique=True, max_length=15)
    telephone = models.CharField(unique=True, max_length=255)
    account_no = models.CharField(unique=True, max_length=15)

    class Meta:
        managed = False
        db_table = 'library_supplier'


class LibraryTemp(models.Model):
    s_no = models.CharField(max_length=255)
    acc_no = models.CharField(max_length=255)
    media = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255)
    code_no = models.CharField(max_length=255)
    copy = models.CharField(max_length=255)
    book_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    pub_year = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    pages = models.CharField(max_length=255)
    call_no = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'library_temp'


class LibraryUsersusertype(models.Model):
    user_id = models.IntegerField()
    user_type = models.CharField(max_length=25)
    student_id = models.IntegerField(blank=True, null=True)
    staff_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'library_usersusertype'


class SchoolConfigurationAcademicyear(models.Model):
    academic_year = models.CharField(unique=True, max_length=15)
    start_year = models.CharField(unique=True, max_length=5)
    end_year = models.CharField(unique=True, max_length=5)
    first_workday = models.DateField()
    last_workday = models.DateField()
    academic_first_day = models.DateField()
    academic_last_day = models.DateField()
    current_year = models.IntegerField()
    mobapp_current_year = models.IntegerField()
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_configuration_academicyear'


class SchoolConfigurationAccount(models.Model):
    name = models.CharField(unique=True, max_length=100)
    account_number = models.CharField(max_length=25, blank=True, null=True)
    payment_account_id = models.CharField(max_length=500, blank=True, null=True)
    payment_secret_key = models.CharField(max_length=500, blank=True, null=True)
    payment_merchant_id = models.CharField(max_length=500, blank=True, null=True)
    payment_salt = models.CharField(max_length=500, blank=True, null=True)
    payment_key = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_configuration_account'


class SchoolConfigurationBank(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'school_configuration_bank'


class SchoolConfigurationBloodgroup(models.Model):
    name = models.CharField(unique=True, max_length=5)

    class Meta:
        managed = False
        db_table = 'school_configuration_bloodgroup'


class SchoolConfigurationBranch(models.Model):
    organization_id = models.IntegerField()
    name = models.CharField(unique=True, max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'school_configuration_branch'


class SchoolConfigurationCategory(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'school_configuration_category'


class SchoolConfigurationCity(models.Model):
    state_id = models.IntegerField()
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'school_configuration_city'


class SchoolConfigurationCommunity(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'school_configuration_community'


class SchoolConfigurationConcession(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'school_configuration_concession'


class SchoolConfigurationCountry(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'school_configuration_country'


class SchoolConfigurationDefault(models.Model):
    nationality_id = models.IntegerField(blank=True, null=True)
    language_id = models.IntegerField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    zipcode = models.CharField(max_length=20, blank=True, null=True)
    quota_id = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_configuration_default'


class SchoolConfigurationDesignation(models.Model):
    name = models.CharField(unique=True, max_length=5)

    class Meta:
        managed = False
        db_table = 'school_configuration_designation'


class SchoolConfigurationGrade(models.Model):
    name = models.CharField(unique=True, max_length=10)
    sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'school_configuration_grade'


class SchoolConfigurationGradeBk(models.Model):
    name = models.CharField(unique=True, max_length=10)
    sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'school_configuration_grade_bk'


class SchoolConfigurationHouse(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'school_configuration_house'


class SchoolConfigurationLanguage(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'school_configuration_language'


class SchoolConfigurationNationality(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'school_configuration_nationality'


class SchoolConfigurationOrganization(models.Model):
    name = models.CharField(unique=True, max_length=100)
    board = models.CharField(max_length=15)
    school_logo = models.CharField(max_length=100, blank=True, null=True)
    board_logo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_configuration_organization'


class SchoolConfigurationPaymentgateway(models.Model):
    payment_name = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    merchant_id = models.CharField(max_length=250)
    tid = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    access_code = models.CharField(max_length=250)
    working_key = models.CharField(max_length=250)
    dashboard_login_url = models.CharField(max_length=250)
    post_action_url = models.CharField(max_length=250)
    redirect_url = models.CharField(max_length=250, blank=True, null=True)
    cancel_url = models.CharField(max_length=250, blank=True, null=True)
    status = models.IntegerField()
    delete_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'school_configuration_paymentgateway'


class SchoolConfigurationProfession(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'school_configuration_profession'


class SchoolConfigurationQuota(models.Model):
    name = models.CharField(unique=True, max_length=15)

    class Meta:
        managed = False
        db_table = 'school_configuration_quota'


class SchoolConfigurationReligion(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'school_configuration_religion'


class SchoolConfigurationSalutation(models.Model):
    name = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'school_configuration_salutation'


class SchoolConfigurationSection(models.Model):
    name = models.CharField(unique=True, max_length=10)
    sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'school_configuration_section'


class SchoolConfigurationSmssettings(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    sid = models.CharField(max_length=250, blank=True, null=True)
    status = models.IntegerField()
    datecreated = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'school_configuration_smssettings'


class SchoolConfigurationSmstemplate(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    message = models.CharField(max_length=250, blank=True, null=True)
    status = models.IntegerField()
    datecreated = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_configuration_smstemplate'


class SchoolConfigurationState(models.Model):
    country_id = models.IntegerField()
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'school_configuration_state'


class SchoolConfigurationUnit(models.Model):
    branch_id = models.IntegerField()
    name = models.CharField(max_length=100)
    school_number = models.CharField(max_length=100, blank=True, null=True)
    affiliation_number = models.CharField(max_length=100, blank=True, null=True)
    board = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    fax_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=50, blank=True, null=True)
    tag_line = models.CharField(max_length=100, blank=True, null=True)
    school_history = models.CharField(max_length=2000, blank=True, null=True)
    contact_person = models.CharField(max_length=50, blank=True, null=True)
    school_renewed_date = models.DateField()
    school_renewal_expiry = models.DateField()

    class Meta:
        managed = False
        db_table = 'school_configuration_unit'
        unique_together = (('branch_id', 'name'),)


class SchoolConfigurationUnitgradesection(models.Model):
    unit_id = models.IntegerField()
    grade_id = models.IntegerField()
    section_id = models.IntegerField()
    academic_year_id = models.IntegerField()
    available_seats = models.IntegerField()
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_configuration_unitgradesection'
        unique_together = (('unit_id', 'grade_id', 'section_id', 'academic_year_id'),)


class SchoolConfigurationUnitgradesectionBk(models.Model):
    unit_id = models.IntegerField()
    grade_id = models.IntegerField()
    section_id = models.IntegerField()
    academic_year_id = models.IntegerField()
    available_seats = models.IntegerField()
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_configuration_unitgradesection_bk'
        unique_together = (('unit_id', 'grade_id', 'section_id', 'academic_year_id'),)


class SettingsAttendancesetting(models.Model):
    attendance_type = models.CharField(max_length=10)
    academic_year_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'settings_attendancesetting'


class SettingsExamsettings(models.Model):
    academic_year_id = models.IntegerField(unique=True)
    has_exam_child_wise_report_card = models.IntegerField()
    has_exam_head_wise_report_card = models.IntegerField()
    has_subject_part = models.IntegerField()
    has_subject_category = models.IntegerField()
    has_subject_head = models.IntegerField()
    has_reportcard_weightage = models.IntegerField()
    has_practical = models.IntegerField()
    has_descriptive_indicators = models.IntegerField()
    indicators_for = models.CharField(max_length=100, blank=True, null=True)
    has_grade_upscaling_concept = models.IntegerField()
    reportcard_folder = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'settings_examsettings'


class SettingsFeessettings(models.Model):
    academic_year_id = models.IntegerField()
    has_on_fly_invoice_generation = models.IntegerField()
    has_discount = models.IntegerField()
    has_concession = models.IntegerField()
    discount_applied_at = models.CharField(max_length=100)
    concession_applied_at = models.CharField(max_length=100)
    discount_applied_to = models.CharField(max_length=100)
    concession_applied_to = models.CharField(max_length=100)
    allow_partial_payment = models.IntegerField()
    number_pattern_on = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'settings_feessettings'


class SettingsLibrarysettings(models.Model):
    academic_year_id = models.IntegerField()
    no_of_non_due_days = models.IntegerField()
    fine_type = models.CharField(max_length=25)
    fineamount = models.IntegerField()
    reservation_limit_for_staff = models.IntegerField()
    reservation_limit_for_student = models.IntegerField()
    issue_limit_for_staff = models.IntegerField()
    issue_limit_for_student = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'settings_librarysettings'


class SettingsReportcardsettings(models.Model):
    academic_year_id = models.IntegerField(unique=True)
    unit_id = models.IntegerField(blank=True, null=True)
    grade_id = models.IntegerField(blank=True, null=True)
    treat_main_exam_as = models.CharField(max_length=100, blank=True, null=True)
    include_pervious_main_exam = models.IntegerField()
    include_pervious_sub_exam = models.IntegerField()
    main_exam_includes_only = models.CharField(max_length=100, blank=True, null=True)
    sub_exam_includes_only = models.CharField(max_length=100, blank=True, null=True)
    is_default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'settings_reportcardsettings'
        unique_together = (('academic_year_id', 'unit_id', 'grade_id'),)


class SettingsStudentsettings(models.Model):
    academic_year_id = models.IntegerField()
    has_readmission = models.IntegerField()
    tc_folder = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settings_studentsettings'


class SouthMigrationhistory(models.Model):
    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'south_migrationhistory'


class StaffClassteacher(models.Model):
    staff_id = models.IntegerField()
    grade_section_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'staff_classteacher'


class StaffContractormaster(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_contractormaster'


class StaffIdcardchoice(models.Model):
    idcard_name = models.CharField(max_length=50, blank=True, null=True)
    staff_id = models.IntegerField(blank=True, null=True)
    academic_year_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_idcardchoice'
        unique_together = (('staff_id', 'academic_year_id'),)


class StaffStaffidcardprintoption(models.Model):
    label_name = models.CharField(max_length=300, blank=True, null=True)
    units = models.CharField(max_length=300, blank=True, null=True)
    label_width = models.CharField(max_length=300, blank=True, null=True)
    label_height = models.CharField(max_length=300, blank=True, null=True)
    columns = models.IntegerField(blank=True, null=True)
    rows = models.IntegerField(blank=True, null=True)
    font = models.CharField(max_length=300, blank=True, null=True)
    font_size = models.IntegerField(blank=True, null=True)
    top_margine = models.FloatField(blank=True, null=True)
    side_margine = models.FloatField(blank=True, null=True)
    vertical_space = models.FloatField(blank=True, null=True)
    horizontal_space = models.FloatField(blank=True, null=True)
    paper_size = models.CharField(max_length=300, blank=True, null=True)
    id_card_layout = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'staff_staffidcardprintoption'


class StaffStaffprofile(models.Model):
    user_id = models.IntegerField(unique=True, blank=True, null=True)
    staff_id = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    photo = models.CharField(max_length=100, blank=True, null=True)
    employee_type = models.IntegerField(blank=True, null=True)
    designation_id = models.IntegerField(blank=True, null=True)
    salutation_id = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=35, blank=True, null=True)
    pan_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=35, blank=True, null=True)
    post_code = models.CharField(max_length=7, blank=True, null=True)
    parent_spouse = models.CharField(max_length=75, blank=True, null=True)
    emergency_contact = models.CharField(max_length=75, blank=True, null=True)
    blood_group_id = models.IntegerField(blank=True, null=True)
    academic_10th = models.CharField(max_length=50, blank=True, null=True)
    academic_12th = models.CharField(max_length=50, blank=True, null=True)
    academic_grad = models.CharField(max_length=50, blank=True, null=True)
    academic_postgrad = models.CharField(max_length=50, blank=True, null=True)
    academic_other = models.CharField(max_length=150, blank=True, null=True)
    previous_employment = models.CharField(max_length=50, blank=True, null=True)
    reason_leaving = models.CharField(max_length=50, blank=True, null=True)
    experience_summary = models.CharField(max_length=150, blank=True, null=True)
    join_date = models.DateField(blank=True, null=True)
    left_date = models.DateField(blank=True, null=True)
    status = models.IntegerField()
    branch_id = models.IntegerField(blank=True, null=True)
    unit_id = models.IntegerField(blank=True, null=True)
    is_teaching_staff = models.IntegerField()
    is_driver = models.IntegerField()
    is_conductor = models.IntegerField()
    is_transport_coordinator = models.IntegerField()
    is_principal = models.IntegerField()
    driver_license_number = models.CharField(max_length=100, blank=True, null=True)
    driving_license_expire_date = models.DateField(blank=True, null=True)
    contractor_master_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_staffprofile'


class StaffSubjectstaffassign(models.Model):
    staff_id = models.IntegerField()
    subjectgrade_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'staff_subjectstaffassign'


class StudentAppstudentconfirmation(models.Model):
    parent_email = models.CharField(max_length=35, blank=True, null=True)
    parent_mobile_number = models.CharField(max_length=20, blank=True, null=True)
    student_admission_number = models.CharField(max_length=25)
    confirm_status = models.CharField(max_length=20)
    student_detail_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'student_appstudentconfirmation'


class StudentHealthmaster(models.Model):
    name = models.CharField(max_length=50)
    academic_year_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_healthmaster'


class StudentIdcardchoice(models.Model):
    idcard_name = models.CharField(max_length=50, blank=True, null=True)
    grade_id = models.IntegerField(blank=True, null=True)
    academic_year_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_idcardchoice'
        unique_together = (('grade_id', 'academic_year_id'),)


class StudentMedicaldetails(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    student_detail_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'student_medicaldetails'


class StudentPromotion(models.Model):
    student_detail_id = models.IntegerField()
    academic_year_id = models.IntegerField()
    grade_section_id = models.IntegerField()
    next_grade_section_id = models.IntegerField(blank=True, null=True)
    rank = models.CharField(max_length=50, blank=True, null=True)
    percentage = models.CharField(max_length=50, blank=True, null=True)
    result = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField()
    remarks = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_promotion'


class StudentStatushistory(models.Model):
    student_detail_id = models.IntegerField()
    from_status = models.CharField(max_length=100)
    to_status = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'student_statushistory'


class StudentStudentaddresslabelprintoption(models.Model):
    label_name = models.CharField(max_length=300, blank=True, null=True)
    units = models.CharField(max_length=300, blank=True, null=True)
    label_width = models.CharField(max_length=300, blank=True, null=True)
    label_height = models.CharField(max_length=300, blank=True, null=True)
    columns = models.IntegerField(blank=True, null=True)
    rows = models.IntegerField(blank=True, null=True)
    font = models.CharField(max_length=300, blank=True, null=True)
    font_size = models.IntegerField(blank=True, null=True)
    top_margine = models.FloatField(blank=True, null=True)
    side_margine = models.FloatField(blank=True, null=True)
    vertical_space = models.FloatField(blank=True, null=True)
    horizontal_space = models.FloatField(blank=True, null=True)
    paper_size = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_studentaddresslabelprintoption'


class StudentStudentapplication(models.Model):
    academic_year_id = models.IntegerField()
    grade_id = models.IntegerField()
    application_no = models.CharField(unique=True, max_length=20)
    quota_id = models.IntegerField(blank=True, null=True)
    application_date = models.DateField()
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    religion_id = models.IntegerField()
    category_id = models.IntegerField()
    community_id = models.IntegerField(blank=True, null=True)
    nationality_id = models.IntegerField()
    language_id = models.IntegerField(blank=True, null=True)
    second_language_id = models.IntegerField(blank=True, null=True)
    third_language_id = models.IntegerField(blank=True, null=True)
    photo = models.CharField(max_length=100, blank=True, null=True)
    last_studied = models.CharField(max_length=10, blank=True, null=True)
    last_school = models.CharField(max_length=250, blank=True, null=True)
    qualified_for_promotion = models.IntegerField()
    medium_studied = models.CharField(max_length=100, blank=True, null=True)
    identification_marks = models.CharField(max_length=250, blank=True, null=True)
    health_problems = models.CharField(max_length=250, blank=True, null=True)
    physically_challenged = models.CharField(max_length=250, blank=True, null=True)
    learning_disability = models.CharField(max_length=250, blank=True, null=True)
    specific_ailment = models.CharField(max_length=250, blank=True, null=True)
    blood_group_id = models.IntegerField(blank=True, null=True)
    comm_address = models.CharField(max_length=500, blank=True, null=True)
    comm_country_id = models.IntegerField(blank=True, null=True)
    comm_state_id = models.IntegerField(blank=True, null=True)
    comm_city_id = models.IntegerField(blank=True, null=True)
    comm_zipcode = models.CharField(max_length=10, blank=True, null=True)
    comm_phone_number = models.CharField(max_length=20, blank=True, null=True)
    permanent_address = models.CharField(max_length=500)
    permanent_country_id = models.IntegerField()
    permanent_state_id = models.IntegerField()
    permanent_city_id = models.IntegerField()
    permanent_zipcode = models.CharField(max_length=10)
    permanent_phone_number = models.CharField(max_length=20)
    father_salutation_id = models.IntegerField(blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    father_profession_id = models.IntegerField(blank=True, null=True)
    father_email = models.CharField(max_length=50, blank=True, null=True)
    father_mobile_no = models.CharField(max_length=20, blank=True, null=True)
    father_work_address = models.CharField(max_length=250, blank=True, null=True)
    mother_salutation_id = models.IntegerField(blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    mother_profession_id = models.IntegerField(blank=True, null=True)
    mother_email = models.CharField(max_length=50, blank=True, null=True)
    mother_mobile_no = models.CharField(max_length=20, blank=True, null=True)
    mother_work_address = models.CharField(max_length=250, blank=True, null=True)
    living_with = models.CharField(max_length=10, blank=True, null=True)
    guardian_name = models.CharField(max_length=100, blank=True, null=True)
    guardian_salutation_id = models.IntegerField(blank=True, null=True)
    guardian_relationship = models.CharField(max_length=50, blank=True, null=True)
    guardian_address = models.CharField(max_length=500, blank=True, null=True)
    guardian_phone_number = models.CharField(max_length=20, blank=True, null=True)
    guardian_mobile_number = models.CharField(max_length=20, blank=True, null=True)
    total_annual_income = models.IntegerField(blank=True, null=True)
    eligible_for_concession = models.IntegerField()
    reason_for_concession = models.CharField(max_length=200, blank=True, null=True)
    bus_required = models.IntegerField()
    hostel_required = models.IntegerField()
    status = models.CharField(max_length=20)
    aadhaar_number = models.CharField(max_length=50, blank=True, null=True)
    father_aadhaar_number = models.CharField(max_length=12, blank=True, null=True)
    mother_aadhaar_number = models.CharField(max_length=12, blank=True, null=True)
    guardian_aadhaar_number = models.CharField(max_length=12, blank=True, null=True)
    habitation_or_locality = models.CharField(max_length=100, blank=True, null=True)
    belong_to_bpl = models.CharField(max_length=10, blank=True, null=True)
    disadvantaged_group = models.CharField(max_length=10, blank=True, null=True)
    free_education = models.CharField(max_length=10, blank=True, null=True)
    status_of_previous_year_for_class_one = models.CharField(max_length=100, blank=True, null=True)
    attendance_for_previous_year = models.IntegerField(blank=True, null=True)
    type_of_disability = models.CharField(max_length=100, blank=True, null=True)
    facilities_received_by_cwsn = models.CharField(max_length=200, blank=True, null=True)
    no_of_uniform_sets = models.CharField(max_length=10, blank=True, null=True)
    set_of_free_text_books = models.CharField(max_length=10, blank=True, null=True)
    free_transport = models.CharField(max_length=10, blank=True, null=True)
    free_escort_facility = models.CharField(max_length=10, blank=True, null=True)
    mdm_beneficiary = models.CharField(db_column='MDM_beneficiary', max_length=10, blank=True, null=True)  # Field name made lowercase.
    free_hostel_facility = models.CharField(max_length=100, blank=True, null=True)
    attended_special_training = models.CharField(max_length=200, blank=True, null=True)
    whether_homeless = models.CharField(max_length=10, blank=True, null=True)
    last_examination_appeared = models.CharField(max_length=10, blank=True, null=True)
    last_examination_passed = models.CharField(max_length=10, blank=True, null=True)
    percentage_of_marks_obtained = models.CharField(max_length=10, blank=True, null=True)
    stream = models.CharField(max_length=50, blank=True, null=True)
    trade_or_sector = models.CharField(max_length=50, blank=True, null=True)
    iron_folic_acid_tablets = models.CharField(max_length=10, blank=True, null=True)
    deworming_tablets = models.CharField(max_length=10, blank=True, null=True)
    vitamin_a_supplement = models.CharField(db_column='vitamin_A_supplement', max_length=10, blank=True, null=True)  # Field name made lowercase.
    student_bank_account_number = models.CharField(max_length=100, blank=True, null=True)
    ifsc_code_of_bank_branch = models.CharField(max_length=100, blank=True, null=True)
    student_email = models.CharField(max_length=50, blank=True, null=True)
    student_mobile_number = models.CharField(max_length=20, blank=True, null=True)
    concession_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_studentapplication'


class StudentStudentapplicationsiblingdetail(models.Model):
    student_application_id = models.IntegerField(blank=True, null=True)
    sibling_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_studentapplicationsiblingdetail'
        unique_together = (('student_application_id', 'sibling_id'),)


class StudentStudentdetail(models.Model):
    academic_year_id = models.IntegerField()
    grade_section_id = models.IntegerField(blank=True, null=True)
    grade_section_joined_id = models.IntegerField(blank=True, null=True)
    student_application_id = models.IntegerField()
    admission_number = models.CharField(max_length=15)
    admission_date = models.DateField(blank=True, null=True)
    quota_id = models.IntegerField(blank=True, null=True)
    date_of_issue = models.DateField(blank=True, null=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateField()
    gender = models.CharField(max_length=6)
    religion_id = models.IntegerField(blank=True, null=True)
    community_id = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField()
    nationality_id = models.IntegerField()
    language_id = models.IntegerField(blank=True, null=True)
    second_language_id = models.IntegerField(blank=True, null=True)
    third_language_id = models.IntegerField(blank=True, null=True)
    photo = models.CharField(max_length=100, blank=True, null=True)
    last_studied = models.CharField(max_length=10, blank=True, null=True)
    last_school = models.CharField(max_length=70, blank=True, null=True)
    qualified_for_promotion = models.IntegerField()
    medium_studied = models.CharField(max_length=30, blank=True, null=True)
    identification_marks = models.CharField(max_length=250, blank=True, null=True)
    health_problems = models.CharField(max_length=250, blank=True, null=True)
    physically_challenged = models.CharField(max_length=250, blank=True, null=True)
    learning_disability = models.CharField(max_length=250, blank=True, null=True)
    blood_group_id = models.IntegerField(blank=True, null=True)
    comm_address = models.CharField(max_length=550, blank=True, null=True)
    comm_country_id = models.IntegerField(blank=True, null=True)
    comm_state_id = models.IntegerField(blank=True, null=True)
    comm_city_id = models.IntegerField(blank=True, null=True)
    comm_zipcode = models.CharField(max_length=10, blank=True, null=True)
    comm_phone_number = models.CharField(max_length=20, blank=True, null=True)
    permanent_address = models.CharField(max_length=500)
    permanent_country_id = models.IntegerField()
    permanent_state_id = models.IntegerField()
    permanent_city_id = models.IntegerField()
    permanent_zipcode = models.CharField(max_length=10)
    permanent_phone_number = models.CharField(max_length=20)
    father_salutation_id = models.IntegerField(blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    father_profession_id = models.IntegerField(blank=True, null=True)
    father_email = models.CharField(max_length=50, blank=True, null=True)
    father_mobile_no = models.CharField(max_length=20, blank=True, null=True)
    father_work_address = models.CharField(max_length=250, blank=True, null=True)
    mother_salutation_id = models.IntegerField(blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    mother_profession_id = models.IntegerField(blank=True, null=True)
    mother_email = models.CharField(max_length=50, blank=True, null=True)
    mother_mobile_no = models.CharField(max_length=20, blank=True, null=True)
    mother_work_address = models.CharField(max_length=250, blank=True, null=True)
    living_with = models.CharField(max_length=10, blank=True, null=True)
    guardian_name = models.CharField(max_length=100, blank=True, null=True)
    guardian_salutation_id = models.IntegerField(blank=True, null=True)
    guardian_relationship = models.CharField(max_length=50, blank=True, null=True)
    guardian_address = models.CharField(max_length=500, blank=True, null=True)
    guardian_phone_number = models.CharField(max_length=20, blank=True, null=True)
    guardian_mobile_number = models.CharField(max_length=20, blank=True, null=True)
    total_annual_income = models.IntegerField(blank=True, null=True)
    whom_to_contact = models.CharField(max_length=50, blank=True, null=True)
    eligible_for_concession = models.IntegerField()
    reason_for_concession = models.CharField(max_length=250, blank=True, null=True)
    bus_required = models.IntegerField()
    hostel_required = models.IntegerField()
    tc_issue_status = models.IntegerField()
    student_status = models.CharField(max_length=15)
    user_id = models.IntegerField(blank=True, null=True)
    is_old_student = models.IntegerField()
    old_student_id = models.IntegerField(blank=True, null=True)
    aadhaar_number = models.CharField(max_length=50, blank=True, null=True)
    father_aadhaar_number = models.CharField(max_length=12, blank=True, null=True)
    mother_aadhaar_number = models.CharField(max_length=12, blank=True, null=True)
    guardian_aadhaar_number = models.CharField(max_length=12, blank=True, null=True)
    habitation_or_locality = models.CharField(max_length=100, blank=True, null=True)
    belong_to_bpl = models.CharField(max_length=10, blank=True, null=True)
    disadvantaged_group = models.CharField(max_length=10, blank=True, null=True)
    free_education = models.CharField(max_length=10, blank=True, null=True)
    status_of_previous_year_for_class_one = models.CharField(max_length=100, blank=True, null=True)
    attendance_for_previous_year = models.IntegerField(blank=True, null=True)
    type_of_disability = models.CharField(max_length=100, blank=True, null=True)
    facilities_received_by_cwsn = models.CharField(max_length=200, blank=True, null=True)
    no_of_uniform_sets = models.CharField(max_length=10, blank=True, null=True)
    set_of_free_text_books = models.CharField(max_length=10, blank=True, null=True)
    free_transport = models.CharField(max_length=10, blank=True, null=True)
    free_escort_facility = models.CharField(max_length=10, blank=True, null=True)
    mdm_beneficiary = models.CharField(db_column='MDM_beneficiary', max_length=10, blank=True, null=True)  # Field name made lowercase.
    free_hostel_facility = models.CharField(max_length=100, blank=True, null=True)
    attended_special_training = models.CharField(max_length=200, blank=True, null=True)
    whether_homeless = models.CharField(max_length=10, blank=True, null=True)
    last_examination_appeared = models.CharField(max_length=10, blank=True, null=True)
    last_examination_passed = models.CharField(max_length=10, blank=True, null=True)
    percentage_of_marks_obtained = models.CharField(max_length=10, blank=True, null=True)
    stream = models.CharField(max_length=50, blank=True, null=True)
    trade_or_sector = models.CharField(max_length=50, blank=True, null=True)
    iron_folic_acid_tablets = models.CharField(max_length=10, blank=True, null=True)
    deworming_tablets = models.CharField(max_length=10, blank=True, null=True)
    vitamin_a_supplement = models.CharField(db_column='vitamin_A_supplement', max_length=10, blank=True, null=True)  # Field name made lowercase.
    student_bank_account_number = models.CharField(max_length=100, blank=True, null=True)
    ifsc_code_of_bank_branch = models.CharField(max_length=100, blank=True, null=True)
    student_email = models.CharField(max_length=50, blank=True, null=True)
    student_mobile_number = models.CharField(max_length=20, blank=True, null=True)
    concession_id = models.IntegerField(blank=True, null=True)
    pen_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_studentdetail'


class StudentStudentdetailsiblingdetail(models.Model):
    student_detail_id = models.IntegerField(blank=True, null=True)
    sibling_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_studentdetailsiblingdetail'
        unique_together = (('student_detail_id', 'sibling_id'),)


class StudentStudentfeescertificate(models.Model):
    student_id = models.IntegerField(blank=True, null=True)
    gradesection_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_studentfeescertificate'


class StudentStudentfeescertificatedetails(models.Model):
    studentfeescertificate_id = models.IntegerField(blank=True, null=True)
    feeshead_name = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_studentfeescertificatedetails'


class StudentStudenthealth(models.Model):
    student_detail_id = models.IntegerField()
    student_healthmaster_id = models.IntegerField()
    grade_section_id = models.IntegerField()
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    vision_left = models.CharField(max_length=50)
    vision_right = models.CharField(max_length=50)
    identification_marks = models.CharField(max_length=250)
    health_problems = models.CharField(max_length=250)
    family_doctor = models.CharField(max_length=100)
    family_doctor_phone = models.CharField(max_length=20)
    physically_challenged = models.CharField(max_length=250)
    blood_pressure = models.CharField(max_length=250)
    temperature = models.CharField(max_length=250)
    bmi = models.CharField(max_length=250)
    ton = models.CharField(max_length=250)
    ff_kk = models.CharField(max_length=250)
    adb = models.CharField(max_length=250)
    rs = models.CharField(max_length=250)
    cvs = models.CharField(max_length=250)
    iq = models.CharField(max_length=250)
    general_examination = models.CharField(max_length=250)
    oral_hygiene = models.CharField(max_length=250)
    hb = models.CharField(max_length=250)
    tlc = models.CharField(max_length=250)
    dlc = models.CharField(max_length=250)
    dental = models.CharField(max_length=250)
    pervious_medical_history = models.CharField(max_length=250)
    ophthal = models.CharField(max_length=250)
    vac_status = models.CharField(max_length=250)
    hemoglobin = models.CharField(max_length=250)
    blood_group = models.CharField(max_length=250, blank=True, null=True)
    learning_disability = models.CharField(max_length=250)
    puls_rate = models.CharField(max_length=250)
    examined_by = models.CharField(max_length=200)
    exam_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_studenthealth'


class StudentStudentidcardprintoption(models.Model):
    label_name = models.CharField(max_length=300, blank=True, null=True)
    units = models.CharField(max_length=300, blank=True, null=True)
    label_width = models.CharField(max_length=300, blank=True, null=True)
    label_height = models.CharField(max_length=300, blank=True, null=True)
    columns = models.IntegerField(blank=True, null=True)
    rows = models.IntegerField(blank=True, null=True)
    font = models.CharField(max_length=300, blank=True, null=True)
    font_size = models.IntegerField(blank=True, null=True)
    top_margine = models.FloatField(blank=True, null=True)
    side_margine = models.FloatField(blank=True, null=True)
    vertical_space = models.FloatField(blank=True, null=True)
    horizontal_space = models.FloatField(blank=True, null=True)
    paper_size = models.CharField(max_length=300, blank=True, null=True)
    id_card_layout = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'student_studentidcardprintoption'


class StudentStudentperformance(models.Model):
    date = models.DateField(blank=True, null=True)
    venue = models.CharField(max_length=250, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    grade_section_id = models.IntegerField()
    student_activity_id = models.IntegerField()
    student_detail_id = models.IntegerField()
    student_subactivity_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'student_studentperformance'
        unique_together = (('student_activity_id', 'student_subactivity_id', 'date', 'venue', 'remarks'),)


class StudentStudentremarks(models.Model):
    remarks = models.CharField(max_length=150, blank=True, null=True)
    academic_year_id = models.IntegerField()
    student_detail_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'student_studentremarks'


class StudentStudentsactivity(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'student_studentsactivity'


class StudentStudentsection(models.Model):
    student_detail_id = models.IntegerField()
    grade_section_id = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    roll_number = models.IntegerField(blank=True, null=True)
    house_id = models.IntegerField(blank=True, null=True)
    reg_number = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_studentsection'


class StudentStudentsubactivity(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    activity_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'student_studentsubactivity'


class StudentStudenttc(models.Model):
    student_detail_id = models.IntegerField()
    tc_prefix = models.CharField(max_length=10, blank=True, null=True)
    tc_number = models.CharField(max_length=10, blank=True, null=True)
    tc_suffix = models.CharField(max_length=10, blank=True, null=True)
    book_number = models.CharField(max_length=250, blank=True, null=True)
    academic_year_id = models.IntegerField()
    first_grade_id = models.IntegerField(blank=True, null=True)
    last_grade_id = models.IntegerField(blank=True, null=True)
    promoted_grade_id = models.IntegerField(blank=True, null=True)
    last_exam_result = models.CharField(max_length=50, blank=True, null=True)
    failed_in_grade = models.CharField(max_length=50, blank=True, null=True)
    subjects_studied = models.CharField(max_length=500, blank=True, null=True)
    qualified_to_next_grade = models.CharField(max_length=50, blank=True, null=True)
    dues_paid_month = models.CharField(max_length=500, blank=True, null=True)
    working_days = models.CharField(max_length=50, blank=True, null=True)
    present_days = models.CharField(max_length=50, blank=True, null=True)
    extra_curricular = models.CharField(max_length=500, blank=True, null=True)
    conduct = models.CharField(max_length=200, blank=True, null=True)
    date_of_application = models.DateField(blank=True, null=True)
    date_of_issue = models.DateField(blank=True, null=True)
    paid_dues = models.CharField(max_length=50, blank=True, null=True)
    renewed_upto = models.CharField(max_length=100, blank=True, null=True)
    registration_no = models.CharField(max_length=50, blank=True, null=True)
    community = models.CharField(max_length=200, blank=True, null=True)
    community1 = models.CharField(max_length=200, blank=True, null=True)
    community2 = models.CharField(max_length=200, blank=True, null=True)
    community3 = models.CharField(max_length=200, blank=True, null=True)
    community4 = models.CharField(max_length=200, blank=True, null=True)
    community5 = models.CharField(max_length=200, blank=True, null=True)
    personalised_marks1 = models.CharField(max_length=200, blank=True, null=True)
    personalised_marks2 = models.CharField(max_length=200, blank=True, null=True)
    personalised_marks3 = models.CharField(max_length=200, blank=True, null=True)
    personalised_marks4 = models.CharField(max_length=200, blank=True, null=True)
    vocational_subject = models.CharField(max_length=200, blank=True, null=True)
    vocation_subject_groupii = models.CharField(db_column='vocation_subject_groupII', max_length=200, blank=True, null=True)  # Field name made lowercase.
    language_offered = models.CharField(max_length=200, blank=True, null=True)
    medium = models.CharField(max_length=50, blank=True, null=True)
    qualified_exam = models.CharField(max_length=50, blank=True, null=True)
    qualify_class = models.CharField(max_length=250, blank=True, null=True)
    qualify_class_words = models.CharField(max_length=250, blank=True, null=True)
    concession = models.CharField(max_length=500, blank=True, null=True)
    scholarship = models.CharField(max_length=50, blank=True, null=True)
    medical_inspection = models.CharField(max_length=300, blank=True, null=True)
    date_left = models.DateField(blank=True, null=True)
    course_studied = models.CharField(max_length=300, blank=True, null=True)
    first_language = models.CharField(max_length=300, blank=True, null=True)
    academic_year_left = models.CharField(max_length=300, blank=True, null=True)
    standard_studied = models.CharField(max_length=300, blank=True, null=True)
    ncc_scout = models.CharField(max_length=300, blank=True, null=True)
    roll_number_struck = models.CharField(max_length=300, blank=True, null=True)
    meeting = models.CharField(max_length=300, blank=True, null=True)
    tmr_code = models.CharField(max_length=250, blank=True, null=True)
    tmr_code_xii = models.CharField(max_length=250, blank=True, null=True)
    reasons = models.CharField(max_length=400, blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    dob_proof = models.CharField(max_length=200, blank=True, null=True)
    school_category = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_studenttc'


class StudentStudentvaccination(models.Model):
    taken_date = models.DateField(blank=True, null=True)
    next_vaccination_date = models.DateField(blank=True, null=True)
    gradesection_id = models.IntegerField()
    student_detail_id = models.IntegerField()
    vaccination_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'student_studentvaccination'
        unique_together = (('vaccination_id', 'taken_date', 'next_vaccination_date'),)


class StudentTaskbox(models.Model):
    taskname = models.CharField(max_length=200, blank=True, null=True)
    priority = models.CharField(db_column='Priority', max_length=50, blank=True, null=True)  # Field name made lowercase.
    task_date = models.DateField(blank=True, null=True)
    task_close_date = models.DateField(blank=True, null=True)
    task_data = models.CharField(max_length=500, blank=True, null=True)
    given_by_id = models.IntegerField(blank=True, null=True)
    grade_section_id = models.IntegerField(blank=True, null=True)
    upload = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_taskbox'


class StudentTcnumberpattern(models.Model):
    prefix = models.CharField(max_length=255, blank=True, null=True)
    suffix = models.CharField(max_length=255, blank=True, null=True)
    numbertobegin = models.CharField(max_length=255)
    status = models.IntegerField()
    next_tc_number = models.CharField(max_length=255)
    academic_year_id = models.IntegerField()
    unit_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_tcnumberpattern'


class StudentTransfercertificatechoice(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    academic_year_id = models.IntegerField(blank=True, null=True)
    grade_section_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_transfercertificatechoice'


class StudentVaccinemaster(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'student_vaccinemaster'


class TransportRoute(models.Model):
    name = models.CharField(unique=True, max_length=50)
    start_time = models.TimeField(blank=True, null=True)
    distance = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    bus_conductor_id = models.IntegerField(blank=True, null=True)
    bus_coordinator_id = models.IntegerField()
    bus_driver_id = models.IntegerField(blank=True, null=True)
    end_point_id = models.IntegerField()
    vehicle_master_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transport_route'


class TransportRoutedetails(models.Model):
    arrives_at_am = models.TimeField(blank=True, null=True)
    arrives_at_pm = models.TimeField(blank=True, null=True)
    sequence_number = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    distance = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.IntegerField()
    route_id = models.IntegerField()
    stopping_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'transport_routedetails'


class TransportStaffroute(models.Model):
    route_type = models.CharField(max_length=10, blank=True, null=True)
    paid_status = models.CharField(max_length=10, blank=True, null=True)
    status = models.IntegerField()
    route_details_id = models.IntegerField(blank=True, null=True)
    staff_detail_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'transport_staffroute'


class TransportStopping(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'transport_stopping'


class TransportStudentroute(models.Model):
    route_type = models.CharField(max_length=10, blank=True, null=True)
    paid_status = models.CharField(max_length=10, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    close_date = models.DateField(blank=True, null=True)
    status = models.IntegerField()
    route_details_id = models.IntegerField(blank=True, null=True)
    studentdetail_id = models.IntegerField()
    staff_id = models.IntegerField(blank=True, null=True)
    student_section_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transport_studentroute'


class TransportVehiclemaster(models.Model):
    name = models.CharField(unique=True, max_length=50)
    registration = models.CharField(unique=True, max_length=50)
    date_acquired = models.DateField(blank=True, null=True)
    last_service = models.DateField(blank=True, null=True)
    next_service = models.DateField(blank=True, null=True)
    last_fc = models.DateField(blank=True, null=True)
    next_fc = models.DateField(blank=True, null=True)
    last_pollution = models.DateField(blank=True, null=True)
    next_pollution = models.DateField(blank=True, null=True)
    stepney = models.IntegerField()
    first_aid = models.IntegerField()
    gps = models.IntegerField()
    seats = models.IntegerField()
    type = models.CharField(max_length=10, blank=True, null=True)
    remarks = models.CharField(max_length=50)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'transport_vehiclemaster'
