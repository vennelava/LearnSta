from django.db import models

# Create your models here.
class Flashcard(models.Model):
    title = models.CharField(max_length=200)
    front_side = models.TextField()
    back_side = models.TextField()

    def __str__(self):
        return self.title
