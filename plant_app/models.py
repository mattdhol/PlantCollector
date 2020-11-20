from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=50)

    low = 'Low'
    medium = 'Medium'
    high = 'High'
    very_high = 'Very High'

    amount_of_light = [
        (low, 'Low'),
        (medium, 'Medium'),
        (high, 'High'),
        (very_high, 'Very High'),
    ]
    amount_of_light = models.CharField(
        max_length=10,
        choices=amount_of_light,
        default='low',
    )
    amount_of_water = [
        (low, 'Low'),
        (medium, 'Medium'),
        (high, 'High'),
        (very_high, 'Very High'),
    ]
    amount_of_water = models.CharField(
        max_length=10,
        choices=amount_of_water,
        default=low,
    )
    description = models.TextField()
    worth_buying = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return "/plants/"
        
    def __str__(self):
        return self.name

DRINK = (
    ('L', 'Light'),
    ('M', 'Medium'),
    ('H', 'Heavy'),
)

class Water(models.Model):
    date = models.DateField()
    drink = models.CharField(
        max_length=1,
        choices=DRINK,
        default=DRINK[0][0]
    )
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_drink_display()} on {self.date}"
