from django.contrib import admin
from lmApp.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','publish','created','updated','status']
    list_filter = ('status','created','publish','author')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    ordering = ('status','publish')

admin.site.register(Post,PostAdmin)

#username:-shankar
#password:-shankar123
#email:-shankar@gmail.com


