from django.contrib import admin
from .models import course, about_us
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=('title',)
    list_filter=('created_at',)
    search_fields=('title',)

admin.site.register(course,PostAdmin)
admin.site.register(about_us)