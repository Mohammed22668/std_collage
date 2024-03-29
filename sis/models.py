from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name="القسم")
    
    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = "القسم"
        verbose_name_plural = "الأقسام"

class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم المقرر الدراسي")
    description = models.TextField(verbose_name="الوصف")
    credit_hours = models.IntegerField(verbose_name="عدد ساعات الائتمان")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="القسم")

    def __str__(self) -> str:
        return str(self.name)
    
    class Meta:
        verbose_name = "المقرر الدراسي"
        verbose_name_plural = "المقررات الدراسية"

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="القسم")

    def __str__(self) -> str:
        return str(self.user)
    
    class Meta:
        verbose_name = "الأستاذ"
        verbose_name_plural = "الأساتذة"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preparatory_school_rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="معدل المرحلة الاعدادية")
    preparatory_study_branch = models.CharField(max_length=200, verbose_name="فرع الدراسة الاعدادية")
    sex = models.CharField(max_length=10, verbose_name="الجنس")
    year_of_admission = models.PositiveSmallIntegerField(verbose_name="سنة الالتحاق")
    school_name = models.CharField(max_length=200, verbose_name="اسم المدرسة")
    phone_number = models.CharField(max_length=15, verbose_name="رقم الهاتف")
    parent_phone_number = models.CharField(max_length=15, verbose_name="رقم هاتف ولي الامر")
    email = models.EmailField(verbose_name="البريد الالكتروني")
    section = models.CharField(max_length=100, verbose_name="القسم")
    photograph = models.ImageField(upload_to='student_photos/', verbose_name="الصورة")
    student_file = models.FileField(upload_to='student_files/', verbose_name="الملف الطلابي")

    def __str__(self) -> str:
        return str(self.user)
    
    class Meta:
        verbose_name = "الطالب"
        verbose_name_plural = "الطلاب"

class ClassSchedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="المقرر الدراسي")
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, verbose_name="الأستاذ")
    day_of_week = models.CharField(max_length=20, verbose_name="يوم الأسبوع")
    time_start = models.TimeField(verbose_name="وقت البدء")
    time_end = models.TimeField(verbose_name="وقت الانتهاء")
    room_number = models.CharField(max_length=20, verbose_name="رقم الغرفة")

    def __str__(self) -> str:
        return str(self.course)
    class Meta:
        verbose_name = "جدول الحصص"
        verbose_name_plural = "جداول الحصص"

class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="المقرر الدراسي")
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, verbose_name="الأستاذ")
    exam_date = models.DateField(verbose_name="تاريخ الامتحان")
    exam_time = models.TimeField(verbose_name="وقت الامتحان")
    room_number = models.CharField(max_length=20, verbose_name="رقم الغرفة")

    def __str__(self) -> str:
        return str(self.course)
    class Meta:
        verbose_name = "الامتحان"
        verbose_name_plural = "الامتحانات"

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="الطالب")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="المقرر الدراسي")
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, verbose_name="الأستاذ")
    grade = models.FloatField(verbose_name="الدرجة")

    def __str__(self) -> str:
        return str(self.student)
    class Meta:
        verbose_name = "الدرجة"
        verbose_name_plural = "الدرجات"

class Notification(models.Model):
    sender = models.ForeignKey(User, related_name='sent_notifications', on_delete=models.CASCADE, verbose_name="المرسل")
    receiver = models.ForeignKey(User, related_name='received_notifications', on_delete=models.CASCADE, verbose_name="المستقبل")
    message = models.TextField(verbose_name="الرسالة")
    date = models.DateTimeField(auto_now_add=True, verbose_name="التاريخ")
    is_read = models.BooleanField(default=False, verbose_name="تم القراءة")

    def __str__(self) -> str:
        return str(self.sender)
    
    class Meta:
        verbose_name = "الإشعار"
        verbose_name_plural = "الإشعارات"