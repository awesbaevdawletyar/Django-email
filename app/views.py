from django.shortcuts import render
from django.core.mail import send_mail

from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def home(request):
    if request.method == 'POST':
        name=request.POST['name']
        mail = request.POST['email']
        subject = request.POST['subject']
        message='Informaciya jibergen paydalaniwshi: '+name+'\n'+'Informaciya: '+subject+'\n'+'Email addressi: '+mail
        send_mail(name,message,mail,['auesbaevdauletyar@gmail.com'],
                  fail_silently=False)
        luck='Informaciya jiberildi!!!'
        return render(request, 'index.html',{'luck':luck})
    return render(request, 'index.html')