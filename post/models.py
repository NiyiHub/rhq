from django.db import models
from django.utils.timezone import now

class Post(models.Model):

    class Category(models.TextChoices):
        RESTURANT = 'Resturant'
        SHOPPING = 'Shopping'
        HOTELS_AND_TRAVELS = 'Hotel and Travel'
        ENTERTAINMENT = 'Entertainment'
        HEALTH_AND_MEDICAL = 'Health and Medical'
        BEAUTY_AND_SPAS = 'Beauty and Spas'
        AUTOMOTIVE = 'Automotive'
        HOME_AND_GARDEN = 'Home and Garden'
        PETS = 'Pets'
        PROFESSIONALS = 'Professionals'
        EDUCATION = 'Education'
        SPORTS_AND_FITNESS = 'Sport and Fitness'
        OTHERS = 'Others'

    title = models.CharField(max_length=60)
    category = models.CharField(max_length=30, choices=Category.choices, default=Category.RESTURANT)
    address = models.CharField(max_length=255)
    review_text = models.TextField(max_length=1000)
    date_of_vist = models.DateTimeField(auto_now_add=True)
    main_photo = models.ImageField(upload_to='posts/', blank=True)
    photo_1 = models.ImageField(upload_to='posts/', blank=True)
    photo_2 = models.ImageField(upload_to='posts/', blank=True)
    photo_3 = models.ImageField(upload_to='posts/', blank=True)


    def __str__(self):
        return self.title

