from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.



class NotificationsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['title', 'Dname', 'Cname', 'get_from', 'year', 'note']
    list_display_links = ['title']
    list_filter = ['title', 'Dname', 'Cname', 'get_from', 'year', 'note']
    search_fields = ['title', 'Dname', 'Cname', 'get_from', 'year', 'note']
    list_per_page = 25

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
admin.site.register(Notifications,NotificationsAdmin)
admin.site.register(Department)
admin.site.register(City)
admin.site.register(UserProfile)
