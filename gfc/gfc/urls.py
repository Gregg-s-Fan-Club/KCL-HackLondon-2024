"""gfc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, URLPattern
from django.conf import settings
from django.conf.urls.static import static
from greggor_productivity_companion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'log_in/',
        views.log_in_view,
        name='log_in'
    ),
    path('log_out/', views.log_out_view, name='log_out'),
    path('sign_up/', views.sign_up_view, name='sign_up'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('delete_profile/', views.delete_profile_view, name='delete_profile'),
    path('display_tasks/', views.display_tasks_view, name ='display_tasks'),
    path('edit_user_details/', views.edit_user_details_view, name="edit_user_details"),
    path('change_password/', views.change_password_view, name="change_password"),
    path('create_task/', views.create_tasks, name ='create_tasks'),
    path('summary/', views.summary_view, name ='summary'),
    path('edit_task/<int:pk>', views.edit_tasks, name ='edit_tasks'),
    path('delete_task/<int:pk>', views.delete_tasks, name ='delete_tasks'),
    path('display_tasks/<str:filter_type>', views.display_tasks_view, name ='display_tasks'),
    path('filter_task_request/', views.filter_task_request, name ='filter_task_request'),
     path('view_individual_task/<int:pk>', views.view_individual_task, name ='view_individual_task'),
    # path(
    #     'filter_task_request/<str:filter_type>',
    #     views.filter_task_request,
    #     name="filter_task_request"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)