from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.frontend , name='frontend'), # Home page
    path('login/',include('django.contrib.auth.urls')),
    path('backend/', views.backend,name='backend'),
    path('add_studentDoc/', views.add_studentDoc,name="add_studentDoc"),
    path('delete_studentDoc/<str:std_id>', views.delete_studentDoc,name="delete_studentDoc"),
    path('studentDoc/<str:std_id>', views.studentDoc,name="studentDoc"),
    path('edit_studentDoc/',views.edit_studentDoc,name='edit_studentDoc'),
    
    # urls for state 
    path('add_studentState/', views.add_studentState, name="add_studentState"),
    path('backendState/', views.backendState, name='backendState'),
    
    # edit_studentState 
    path('edit_studentState/', views.edit_studentState, name='edit_studentState'),
    path('studentState/<str:std_id>', views.studentState, name="studentState"),
    path('delete_studentState/<str:std_id>',views.delete_studentState, name="delete_studentState"),
    
    # notification
    path('notifications/', views.notification, name="notification"),
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


