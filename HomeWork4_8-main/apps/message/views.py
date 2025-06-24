from django.shortcuts import render, redirect, get_object_or_404
from apps.message.models import Message

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        text = request.POST['text']
        Message.objects.create(name=name, text=text)
        return redirect('/')
    message = Message.objects.all().order_by("-created_at")
    return render(request, 'index.html', {'message': message})


def like_message(request, message_id):
    if request.method == "POST":
        message = get_object_or_404(Message, id=message_id)
        message.likes += 1
        message.save()
        return redirect("/")
    



def delete_message(request, id):
    message = get_object_or_404(Message, id=id)
    message.delete()
    return redirect('/')

