from django.shortcuts import render
from . models import ContactUs
# Create your views here.
def Home(request):
    return render(request, 'Pages/Home.html')

def About(request):
    return render(request, 'Pages/About.html')

def Contact(request):
    if request.method == 'POST':
        FristName = request.POST.get('Fname')
        LastName = request.POST.get('Lname')
        Email = request.POST.get('email')
        Subject = request.POST.get('subject')
        Massage = request.POST.get('message')
        SendDatatoDB = ContactUs(FristName=FristName,LastName=LastName,Email=Email,Subject=Subject,Massage=Massage)
        SendDatatoDB.save()
        return render(request, 'Pages/Contact.html')

    else:
       return render(request, 'Pages/Contact.html')