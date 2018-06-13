from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from blogs.models import Blog

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class BlogInline(admin.StackedInline):
    model = Blog
    can_delete = False
    verbose_name_plural = 'Blog'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (BlogInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)