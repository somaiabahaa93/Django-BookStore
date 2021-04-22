from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural="categories"

    name = models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.name
    
class Isbn(models.Model):

    autherTitle=models.CharField(max_length=256)
    bookTitle=models.CharField(max_length=256)
    isbnNumber= models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    # other fields

    def __str__(self):
         return str(self.isbnNumber)



class Tag(models.Model):
    name=models.CharField( max_length=25)   
    def __str__(self):
         return str(self.name)     

    
class Book(models.Model):
    title=models.CharField(max_length=256)
    content=models.TextField(max_length=2048)
    auther= models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,related_name="books")
    categories=models.ManyToManyField(Category)
    isbn=models.OneToOneField(Isbn, on_delete=models.CASCADE,null=True,blank=True)
    tag=models.ForeignKey(Tag,null=True,blank=True,on_delete=models.CASCADE)


    def __str__(self):
       return self.title
