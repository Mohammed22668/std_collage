from django.contrib import admin
from .models import Patient , Department , City , StudentDocument , UserProfile ,StudentStatus
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# class AdminPatient(admin.ModelAdmin):
#     list_display=['name','phone','email','age','gender','created_at']
#     search_fields=['name','phone','email','age','gender']
#     list_per_page=8


# admin.site.register(Patient,AdminPatient)
class DocumentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=['user','name','Dname','Cname','graduate_year','to','Dnumber','Ddate','check_post']
    list_display_links=['user','name','Dname','Cname','graduate_year','to','Dnumber']
    list_filter=['user','name','Dname','Cname','graduate_year']
    search_fields = ['name','Dname','Cname','graduate_year','to','Dnumber','Ddate']
    list_per_page=25
        

class StateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['user', 'name', 'Dname', 'Cname', 'stage','state','year','note']
    list_display_links = ['user', 'name', 'Dname','Cname', 'stage', 'state', 'year', 'note']
    list_filter = ['user', 'name', 'Dname','Cname', 'stage', 'state', 'year', 'note']
    search_fields = ['user', 'name', 'Dname','Cname', 'stage', 'state', 'year', 'note']
    list_per_page = 25
    
admin.site.register(StudentDocument,DocumentAdmin)
admin.site.register(StudentStatus,StateAdmin)
admin.site.register(Department)
admin.site.register(City)
admin.site.register(UserProfile)
