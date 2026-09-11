from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def features(request):
    return render(request, 'core/features.html')

def services(request):
    return render(request, 'core/services.html')

def pricing(request):
    return render(request, 'core/pricing.html')

def contact(request):
    return render(request, 'core/contact.html')

def getstarted(request):
    return render(request, 'core/getstarted.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        full_message = f"""
        New Contact Form Message

        Name: {name}
        Email: {email}
        Phone: {phone}

        Message:
        {message}
        """

        send_mail(
            subject="New Contact Message",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        return redirect("home")

    return redirect("home")