from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import event_list

urlpatterns = [
    path('', views.index, name='index'),
    path('calendar/', views.calendar_list, name='calendar_list'),
    path('calendar/add/', views.add_calendar, name='add_calendar'),
    path('calendar/<int:calendar_id>/', event_list, name='event_list'),
    path('create_event/', views.create_event, name='create_event'),
    path('event/update/<int:event_id>/', views.update_event, name='update_event'),
    path('event/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('calendar/<int:calendar_id>/export/', views.export_calendar, name='export_calendar'),
    path('calendar/<int:calendar_id>/export/vcs/', views.export_vcs_calendar, name='export_vcs_calendar'),
    path('calendar/<int:calendar_id>/delete/', views.delete_calendar, name='delete_calendar'),


]
