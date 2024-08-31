"""
URL configuration for Form_Automation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home),
    path("add_student", views.add_student),
    path("download_students_excel", views.download_students_excel, name='download_students_excel'),
    path("download_students_pdf", views.download_students_pdf, name='download_students_pdf'),
    path("download_students_form", views.download_students_form, name='download_students_form'),
    path("add_student_bulk", views.add_student_bulk, name='add_student_bulk'),
]
