from django.shortcuts import render
from django.http import HttpResponse
from .models import Service
from .forms import EnquiryForm

# ✅ Home Page – shows top 6 services
def home(request):
    services = Service.objects.all()[:6]
    return render(request, 'main/home.html', {'services': services})

# ✅ Services Page – shows all services
def services(request):
    services = Service.objects.all()
    return render(request, 'main/services.html', {'services': services})

# ✅ Contact Page with enquiry form and services for footer
def contact(request):
    services = Service.objects.all()[:4]  # Needed for footer
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/thanks.html', {'services': services})  # Include services for footer
    else:
        form = EnquiryForm()
    return render(request, 'main/contact.html', {'form': form, 'services': services})

# ✅ Optional Debug View – for console logging
def debug_services(request):
    services = Service.objects.all()
    for service in services:
        print(f"Display: {service.name} | Code: {service.code}")
    return HttpResponse("✅ Check your terminal for debug output.")
