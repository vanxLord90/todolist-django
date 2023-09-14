from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title','description','due_date','priority','completed')

admin.site.register(Todo, TodoAdmin)
# Register your models here.
