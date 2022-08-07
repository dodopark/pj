from django.contrib import admin
from app_main.models import Place, Register

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['username' ,'name', 'surname', 'email', 'address', 'password']
    search_fields = ['email']

class PlaceAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'p_address', 'p_province', 'p_district', 'p_subdistrict']
    search_fields = ['p_name']




admin.site.register(Place, PlaceAdmin)
admin.site.register(Register, RegisterAdmin)
