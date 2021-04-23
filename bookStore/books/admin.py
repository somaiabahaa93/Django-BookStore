from django.contrib import admin
from .models import Book ,Category, Isbn, Tag
from .forms import BookForm,CategoryForm

# Register your models here.
# admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    form=BookForm
    list_display=("title","content","auther","tag")
    list_filter=("categories",)

   

class BookInline(admin.StackedInline):
    model=Book
    max_num=3
    extra=1



class TagAdmin(admin.ModelAdmin):
     inlines=[BookInline] 



class CategryAdmin(admin.ModelAdmin):
    form=CategoryForm
    


admin.site.register(Book, BookAdmin)
admin.site.register(Category,CategryAdmin)
admin.site.register(Isbn)
admin.site.register(Tag,TagAdmin)




