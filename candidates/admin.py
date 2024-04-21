from django.contrib import admin
from .models import Candidate
# Register your models here.
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('photo','candidate', 'positions', 'block', 'nationality')
    list_display_links = ('candidate',)


admin.site.register(Candidate, CandidateAdmin)