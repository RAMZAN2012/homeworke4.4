from django.shortcuts import render, redirect
from apps.main.models import Setting, Gallary, Form
from .service import get_text
# Create your views here.

def index(request):
    setting = Setting.objects.latest("id")
    gallary = Gallary.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        
        Form.objects.create(name=name, email=email, phone=phone, message=message)
        
        get_text(f""" 
Имя отправителя: {name}
email: {email}
Номер телефона: {phone}
Сообщение: {message}
""")        
        return redirect("index")
        
    return render(request, 'index.html', locals())

