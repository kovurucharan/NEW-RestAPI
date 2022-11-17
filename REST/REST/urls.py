"""REST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#from rest_framework.urlpatterns import format_suffix_patterns
from WebApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('js/',views.EmployeeList.as_view()),
    path('emp_list/',views.Emplist,name='emp_list'),
    path('emp_details/<int:id>/',views.Emp_details,name='emp_details'),
    path('emp_create/',views.Emp_create,name='emp_create'),
    path('emp_update/<int:id>/',views.Emp_update,name='emp_update'),
    path('emp_delete/<int:id>/',views.Emp_delete,name='emp_delete')
]
