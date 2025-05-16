from django.contrib import admin
from .models import Skill,Project,ContactPage

# Register your models here.
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = [i.name for i in Skill._meta.fields]
    search_fields = ('name', 'level')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [i.name for i in Project._meta.fields]


@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = [i.name for i in ContactPage._meta.fields]
