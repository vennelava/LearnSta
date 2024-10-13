from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Room, Message
from .forms import MessageForm


@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
                message = form.save(commit=False)
                message.user = request.user
                message.room = room
                message.save()
                return redirect('room', slug=room.slug)
    form = MessageForm()
    
    # return HttpResponse(str(messages.values()))
    return render(request, 'room/room.html', {'room': room, 'messages': messages, "form":form})

# Create your views here.
