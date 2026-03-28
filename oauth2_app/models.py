from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Room(models.Model):
    ROOM_CHOICES = (('Single', 'Single'), ('Double', 'Double'), ('Suite', 'Suite'))
    room_number = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(50)]
    )
    room_choice = models.CharField(choices=ROOM_CHOICES)
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.room_number} - {self.room_choice}"
