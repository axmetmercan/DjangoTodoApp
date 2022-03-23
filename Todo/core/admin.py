from django.contrib import admin
from .models import Todo
# Register your models here.


# admin.site.register(Todo)


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['todo','status', 'created_date', 'completed_date']
    list_filter = ['todo', 'created_date', 'completed_date']
    search_fields = ['todo', 'created_date', 'completed_date']
    list_display_links = ['todo']
    ordering = ['-created_date']
    list_max_show_all = 300
    list_per_page = 25
    class Meta:
        model = Todo


