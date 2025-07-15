from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                          # 🏠 Home page
    path('services/', views.services, name='services'),         # 🧾 Services list
    path('contact/', views.contact, name='contact'),            # 📞 Contact / Enquiry page
    path('debug-services/', views.debug_services, name='debug_services'),  # 🛠️ Debug (optional)
]
