from django import forms
from .models import Book 
from django.core.exceptions import ValidationError
class BookForm (forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__" 
        exclude=("isbn",)

    def clean(self):
        super(BookForm,self).clean()
        title=self.cleaned_data.get("title")   
        category=self.cleaned_data.get("categories") 

        

        if len(title) <10 :
          raise ValidationError("title must be grater than 10 ")
        elif len(title)>50:
          raise ValidationError("title must be less than 50")
        return self.cleaned_data  


class CategoryForm(forms.ModelForm):
    def clean(self):
        super(CategoryForm,self).clean()
        name=self.cleaned_data.get("name")
        if len(name) <2 :
          raise ValidationError("category name must be grater than 2 ")
        return self.cleaned_data  
