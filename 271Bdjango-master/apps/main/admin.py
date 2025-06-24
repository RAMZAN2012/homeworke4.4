from django.contrib import admin
from apps.main.models import Setting, Gallary, Form
# Register your models here.

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'logo',)
    list_editable = ("logo",)
    list_filter = ("title", "description")
    search_fields = ("title",)

@admin.register(Gallary)
class GalaryAdmin(admin.ModelAdmin):
    list_display = ('image',)
    
@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ('name', 'message')