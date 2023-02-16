from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from services.models import Services, ServiceProvider, ProviderMessage, AdminMessage
from services.forms import ProviderMessageForm, AdminMessageForm
from django.contrib import messages
# Create your views here.


def contactProvider(request):
    if request.method == 'POST':
        form = ProviderMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Success")
            form = ProviderMessageForm()
        else:
            messages.error(request, "Failed")
    else:
        form = ProviderMessageForm()
    return render(request, 'contactProvider.html', {'form': form})

def contactAdmin(request):
    if request.method == 'POST':
        form = AdminMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Success")
            form = AdminMessageForm()
        else:
            messages.error(request, "Failed")
    else:
        form = AdminMessageForm()
    return render(request, 'contactAdmin.html', {'form': form})

def services(request):
    popular_service_providers = ServiceProvider.objects.all().order_by('sp_star')[0:4]
    popular_service = Services.objects.filter(status=Services.ACTIVE).order_by('stars')[0:4]
    popular_services = Services.objects.all()
    return render(request, 'services.html', {
    'popular_service_providers': popular_service_providers,
    'popular_services': popular_services,
    })

def search_services(request):
    service_query = request.GET.get('service_query', '')
    services = None
    service_provider = None
    if service_query:
        services = Services.objects.filter(status=Services.ACTIVE).filter(Q(title__icontains=service_query) | Q(description__icontains=service_query))
        service_provider = ServiceProvider.objects.filter(Q(sp_name__icontains=service_query))

    return render(request, 'search_services.html', {
    'service_query': service_query,
    'services': services,
    'service_provider': service_provider,
    })   



def service_details(request):
    services = Services.objects.all()
    serpro = ServiceProvider.objects.all()
    return render(request, 'service_detail.html', {
    'services': services,
    'serpro': serpro,
    })

def view_services(request):
    services = Services.objects.all()
    serpro = ServiceProvider.objects.all()
    return render(request, 'view_services.html', {
    'services': services,
    'serpro': serpro,
    })

def view_service_category(request, slug):
    service = get_object_or_404(Services, slug=slug)
    return render(request, 'view_service_category.html', { 
    'service': service,
    })













