from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.services, name='services'), 
    path('view_services/',views.view_services, name='view_services'),
    path('service_details/',views.service_details, name='service_details'),
    path('search_services/', views.search_services, name='search_services'),
    path('services/<slug:slug>/', views.view_service_category, name='view_service_category'),
    path('contact-admin/', views.contactAdmin, name='contactAdmin'),
    path('contact-provider/', views.contactProvider, name='contactProvider'),
    # Create 2 url in for <str: sp_name>
    
]