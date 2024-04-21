from django.contrib import admin
from .models import Block
# Register your models here.
class BlockAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('block',)}
    list_display = ('block', 'slug')
admin.site.register(Block, BlockAdmin)