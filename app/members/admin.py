from django.contrib import admin
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("id", "firstname", "lastname", "email", "birth_date", "joined_date",)
  
admin.site.register(Member, MemberAdmin)