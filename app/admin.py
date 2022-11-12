from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class TasjilAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['name','Dname', 'Cname','study','year_grad','to','docType','note','img']
    list_display_links = ['name','Dname', 'Cname','study']
    list_filter = ['name','Dname', 'Cname','study','year_grad','to','docType']
    search_fields = ['name','Dname', 'Cname','study','year_grad','to','docType', 'note']
    list_per_page = 30


class NotificationsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['title', 'Dname', 'Cname', 'get_from', 'year', 'note']
    list_display_links = ['title']
    list_filter = ['title', 'Dname', 'Cname', 'get_from', 'year', 'note']
    search_fields = ['title', 'Dname', 'Cname', 'get_from', 'year', 'note']
    list_per_page = 25

# admin.site.register(Patient,AdminPatient)
class DocumentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=['user','name','Dname','Cname','study','graduate_year','to','Dnumber','Ddate','check_post']
    list_display_links=['user','name','Dname','Cname','graduate_year','to','Dnumber']
    list_filter=['user','name','Dname','Cname','study','graduate_year']
    search_fields = ['name','Dname','Cname','study','graduate_year','to','Dnumber','Ddate']
    list_per_page=25
        

class StateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['user', 'name', 'Dname', 'Cname', 'stage','state','year','note']
    list_display_links = ['user', 'name', 'Dname','Cname', 'stage', 'state', 'year', 'note']
    list_filter = ['user', 'name', 'Dname','Cname', 'stage', 'state', 'year', 'note']
    search_fields = ['user', 'name', 'Dname','Cname', 'stage', 'state', 'year', 'note']
    list_per_page = 25
    

class AllStudentsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['user', 'name', 'Dname','study', 'Cname', 'stage','state','date','year']
    list_display_links = ['name', 'Dname', 'Cname', 'stage','state']   
    list_filter = ['name', 'Dname', 'Cname','study', 'stage','state','date','year'] 
    search_fields = ['name', 'Dname', 'Cname', 'study','stage','date','year']
    list_per_page: 25
    
admin.site.register(StudentDocument,DocumentAdmin)
admin.site.register(StudentStatus,StateAdmin)
admin.site.register(Notifications,NotificationsAdmin)
admin.site.register(Department)
admin.site.register(City)
admin.site.register(UserProfile)
admin.site.register(TasjilDocuments,TasjilAdmin)
admin.site.register(AllStudents,AllStudentsAdmin)
