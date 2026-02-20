from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):

    GENRE_CHOICES = [
    ("fiction", "Fiction"),
    ("nonfiction", "Non-Fiction"),
    ("scifi", "Science Fiction"),
    ("fantasy", "Fantasy"),
    ("mystery", "Mystery"),
    ("thriller", "Thriller"),
    ("romance", "Romance"),
    ("horror", "Horror"),
]

    title = models.CharField()
    author = models.CharField()
    description = models.TextField()
    genre = models.CharField(choices=GENRE_CHOICES, max_length=20)
    isbn = models.CharField(unique=True)
    publication_date = models.DateField()

    average_rating = models.DecimalField(
    max_digits=3,
    decimal_places=2,
    validators=[MinValueValidator(0), MaxValueValidator(5)],
    default=0
    )

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    


