"""
URL configuration for core project.

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
from authenticate.views import login_user, home, create_user, view_task, add_task, delete_task,modify_task

urlpatterns = [
    path('', home, name='home'),
    path('view-task/', view_task, name='view_task'),  # View tasks
    path('view-task/add-task/', add_task, name='add_task'),  # Add task
    path('view-task/modify-task/<int:id>/', modify_task, name='modify_task'),
    path('view-task/delete-task/<int:id>/', delete_task, name='delete_task'),  # Delete task with task ID
    path('create-user/', create_user, name='create_user'),
    path('login/', login_user, name='login_user'),
    path('admin/', admin.site.urls),
]

