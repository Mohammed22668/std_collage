from django.contrib import admin
from .models import *
# Register your models here.
from import_export.admin import ImportExportModelAdmin


class DepartmentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display= ["name"]



class CourseAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display= ["name" , "description" , "credit_hours" , "department" ] 
    list_display = ["name"]
    list_filter = ["credit_hours" , "department"]
    
    
    
    
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ["user", "department"]
    list_filter = ["department"]
    search_fields = ["user__username", "user__first_name", "user__last_name"]

class StudentAdmin(admin.ModelAdmin):
    list_display = ["user", "year_of_admission", "section"]
    list_filter = ["year_of_admission", "section"]
    search_fields = ["user__username", "user__first_name", "user__last_name"]

class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ["course", "professor", "day_of_week", "time_start", "time_end", "room_number"]
    list_filter = ["course", "professor", "day_of_week"]
    search_fields = ["course__name", "professor__user__first_name", "professor__user__last_name"]

class ExamAdmin(admin.ModelAdmin):
    list_display = ["course", "professor", "exam_date", "exam_time", "room_number"]
    list_filter = ["course", "professor", "exam_date"]
    search_fields = ["course__name", "professor__user__first_name", "professor__user__last_name"]

class GradeAdmin(admin.ModelAdmin):
    list_display = ["student", "course", "professor", "grade"]
    list_filter = ["course", "professor"]
    search_fields = ["student__user__username", "student__user__first_name", "student__user__last_name"]

class NotificationAdmin(admin.ModelAdmin):
    list_display = ["sender", "receiver", "date", "is_read"]
    list_filter = ["sender", "receiver", "date", "is_read"]
    search_fields = ["sender__username", "receiver__username"]
    
    
    

admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(ClassSchedule, ClassScheduleAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Notification, NotificationAdmin)
    
    
    