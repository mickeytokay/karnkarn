from django.contrib import admin
from .models import General_Chairman, Co_Chair, Secretery_General, Financial_Secretery, Women_Chair, Youth_Chair
# Register your models here.
class General_ChairmanAdmin(admin.ModelAdmin):
    list_display = ('category', 'candidate', 'votes')

admin.site.register(General_Chairman, General_ChairmanAdmin)

class CochairAdmin(admin.ModelAdmin):
    list_display = ('category', 'candidate', 'votes')
admin.site.register(Co_Chair, CochairAdmin)

class SecreteryAdmin(admin.ModelAdmin):
    list_display = ('category', 'candidate', 'votes')
admin.site.register(Secretery_General, SecreteryAdmin)

class FinancialAdmin(admin.ModelAdmin):
    list_display = ('category', 'candidate', 'votes')
admin.site.register(Financial_Secretery, FinancialAdmin)

class WomenAdmin(admin.ModelAdmin):
    list_display = ('category', 'candidate', 'votes')
admin.site.register(Women_Chair, WomenAdmin)

class YouthAdmin(admin.ModelAdmin):
    list_display = ('category', 'candidate', 'votes')
admin.site.register(Youth_Chair, YouthAdmin)