from django.shortcuts import render,redirect
from .models import Skill,Project,ContactPage
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def skills(request):
    skill = Skill.objects.all()
    context = {
        'skills':skill
    }
    return render(request,'skills.html',context)

def projects(request):
    project = Project.objects.all()
    context = {
        'projects':project
    }
    return render(request,'projects.html',context)

from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render
from .models import ContactPage
from django.conf import settings
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        # Save to database
        ContactPage.objects.create(name=name, email=email, message=message)
        
        # Send email to yourself
        subject = f"New Contact Form Message from {name}"
        message_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        recipient_list = ['harshprasad2382006@gmail.com']  # Replace with your email
        
        send_mail(subject, message_body, email, recipient_list, fail_silently=False)

        send_mail(
                'Message sent successfully',
                f"""
                Dear {name},
                Thank you for reaching out to us. We have received your message and will be in touch with you shortly.""",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )
        
        messages.success(request, "Message sent successfully")
        return redirect('contact')
    
    return render(request, 'contact.html')


