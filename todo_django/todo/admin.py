from django.contrib import admin
from .models import Profile, Task, Category


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  list_per_page = 20


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'description', 'expired_at', 'category_id', 'user_id')
  list_filter = ('category_id', 'user_id')
  search_fields = ('id', 'username', 'description', 'expired_at', 'user_id')
  list_per_page = 20

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_per_page = 20