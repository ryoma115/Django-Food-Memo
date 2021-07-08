from django.db import models

class Post(models.Model):
  # user = models.ForeignKey(User, on_delete=models.CASCADE)
  where = models.CharField(max_length=100)
  store_name = models.CharField(max_length=100)
  food_category = models.CharField(max_length=200)
  photo1 = models.ImageField(upload_to='documents/')
  photo2 = models.ImageField(upload_to='documents/', blank=True, null=True)
  photo3 = models.ImageField(upload_to='documents/', blank=True, null=True)
  photo4 = models.ImageField(upload_to='documents/', blank=True, null=True)
  photo5 = models.ImageField(upload_to='documents/', blank=True, null=True)
  description = models.TextField()
  posted_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.where

      