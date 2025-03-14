"""
URL configuration for ToDo project.

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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.Registration_view.as_view(),name='register'),
    path('login/',views.Login.as_view(),name="login"),
    path('task/',views.TaskAdd.as_view(),name="create"),
    path('taskview/',views.TaskAll.as_view(),name='viewall'),
    path('taskdele/<int:pk>',views.TaskDelete.as_view(),name='delete'),
    path('taskup/<int:pk>',views.TaskUpdate.as_view(),name='update'),
    path('detail/<int:pk>',views.TaskDetail.as_view(),name='detail'),
    path('status/<int:pk>',views.Task_Status.as_view(),name='status'),
    path('logout/',views.Signout.as_view(),name="logout"),
    path('completed/',views.Completed_view.as_view(),name='complete'),
    path('home/',views.Taskhome.as_view(),name='home'),
    path('userdetails/',views.Userdetailview.as_view(),name='userdetails')
   
]
