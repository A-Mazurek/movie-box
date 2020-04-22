from django.contrib import admin
from movies_info.models import Movie
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)


admin.site.register(Movie, MovieAdmin)
