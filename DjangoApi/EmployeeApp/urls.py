from django.urls import path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('department/', views.departmentApi, name='department'),
    path('department/<int:id>', views.departmentApi), # to accepting ID as Inteager on app

    path('employee', views.employeeApi),
    path('employee/<int:id>', views.employeeApi),

    path('employee/savefile', views.SaveFile)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
