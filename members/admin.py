from django.contrib import admin
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('photo', 'full_name', 'block', 'nationality', 'phone')
    list_display_links = ('full_name',)

admin.site.register(Member, MemberAdmin)