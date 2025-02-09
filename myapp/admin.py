from django.contrib import admin
from .models import Post
from .models import Contact

admin.site.register(Contact)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'deadline')
    prepopulated_fields = {'slug': ('title',)}