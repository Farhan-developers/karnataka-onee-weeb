from django.db import models

# 📞 Contact Us Submission
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name

# 🛎️ Online Services Offered
class Service(models.Model):
    name = models.CharField(max_length=100)  # Full service name (e.g., 'Aadhaar Services')
    code = models.CharField(max_length=20, unique=True)  # Unique short code for service (e.g., 'aadhaar')
    icon = models.ImageField(upload_to='service_icons/', blank=True)  # Optional image icon
    description = models.TextField(blank=True)  # Optional description

    def __str__(self):
        return self.name

# 📬 General Enquiries
class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    def __str__(self):
        return f"{self.name} ({self.contact})"
