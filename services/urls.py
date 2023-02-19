from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.services, name='services'), 
    path('search_services/', views.search_services, name='search_services'),
    path('services/<str:service_provider>/<str:service_name>/', views.view_service, name='view_service'),

    path('service_details/',views.service_details, name='service_details'),
    path('services/<slug:slug>/', views.view_service_category, name='view_service_category'),
    path('contact-admin/', views.contactAdmin, name='contactAdmin'),
    path('services/<str:service_provider>/<str:service_name>/contact-provider/', views.contactProvider, name='contactProvider'),
    # Create 2 url in for <str: sp_name>
    
]