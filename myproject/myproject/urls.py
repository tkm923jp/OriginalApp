"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TopView.as_view(), name="top"),
    path('crud/users/', views.UserListView.as_view(), name="users"),
    path('crud/new_user/', views.UserCreateView.as_view(), name="new_user"),
    path('crud/edit/<int:pk>', views.UserUpdateView.as_view(), name="edit"),
    path('crud/delete/<int:pk>', views.UserDeleteView.as_view(), name="delete"),
    path('crud/schedules/', views.ScheduleListView.as_view(), name="schedules"),
    path('crud/new_schedule/', views.ScheduleCreateView.as_view(), name="new_schedule"),
    path('crud/edit_schedule/<int:pk>', views.ScheduleUpdateView.as_view(), name="edit_schedule"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
]
