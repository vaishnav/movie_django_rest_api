from django.db import models

# Create your models here.
class Genere(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    genere = models.ForeignKey(Genere, on_delete=models.SET_NULL, blank=True, null=True)
    director = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3,decimal_places=1)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(rating__gte=1.0) & models.Q(rating__lte=10.0),
                name="valid between 1 and 10",
            )
        ]