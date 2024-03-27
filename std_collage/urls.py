from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import re_path
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from app import views
from django.views.static import serve

urlpatterns = [
    path('userAdminpnl/', admin.site.urls),
    path('', views.frontend , name='frontend'), # Home page
    path('',include('django.contrib.auth.urls')),
    path('backend/', views.backend,name='backend'),
    path('add_studentDoc/', views.add_studentDoc,name="add_studentDoc"),
    path('delete_studentDoc/<str:std_id>', views.delete_studentDoc,name="delete_studentDoc"),
    path('studentDoc/<str:std_id>', views.studentDoc,name="studentDoc"),
    path('edit_studentDoc/',views.edit_studentDoc,name='edit_studentDoc'),
    
    
    #
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    #
    # urls for state 
    path('add_studentState/', views.add_studentState, name="add_studentState"),
    path('backendState/', views.backendState, name='backendState'),
    
    # edit_studentState 
    path('edit_studentState/', views.edit_studentState, name='edit_studentState'),
    path('studentState/<str:std_id>', views.studentState, name="studentState"),
    path('delete_studentState/<str:std_id>',views.delete_studentState, name="delete_studentState"),
    
    # notification
    path('notifications/', views.notification, name="notification"),
    
    ######################### All student ##########################
    path('add_allstudent/',views.add_allstudent,name="add_allstudent"),
    path('backend-allstudents/',views.backend_all_student,name="backend_all_student"),
    path('edit_allstudent/',views.edit_allstudent,name="edit_allstudent"),
    path('all_student/<str:std_id>', views.all_student, name="allstudent"),
    path('delete_allstudent/<str:std_id>',views.delete_allstudent,name="delete_allstudent"),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


