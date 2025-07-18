from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Category(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name
  
class Ad(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  created_at = models.DateTimeField(auto_now_add=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ads')
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')

  def __str__(self):
    return self.title
  
class AdImage(models.Model):
  ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='images')
  image = models.ImageField(upload_to='ad_images/')

  def __str__(self):
    return f"Image for {self.ad.title}"