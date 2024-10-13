from django.shortcuts import render, redirect
from .models import Flashcard
from .forms import FlashcardForm

def flashcard_list(request):
    flashcards = Flashcard.objects.all()
    return render(request, 'FlashApp/flashcard_list.html', {'flashcards': flashcards})
def create_flashcard(request):
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flashcard_list')
    else:
        form = FlashcardForm()
    return render(request, 'FlashApp/create_flashcard.html', {'form': form})
def delete_flashcard(request, flash_id):
    flashcards = Flashcard.objects.all()
    for x in flashcards:
        if x.id == flash_id:
            x.delete()
    return redirect('flashcard_list')
# Create your views here.
