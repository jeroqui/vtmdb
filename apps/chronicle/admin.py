from django.contrib import admin

from .models import *

# Register your models here.
class RelationshipsInline(admin.TabularInline):
    model = CharacterRelationship
    fk_name = "character1"


class VampireCCInline(admin.StackedInline):
    model = VampireCC
    fk_name = "character"

class HumanCCInline(admin.StackedInline):
    model = HumanCC

class CharacterAdmin(admin.ModelAdmin):
    list_display = ["name", "pc"]
    inlines = [RelationshipsInline, HumanCCInline, VampireCCInline]


admin.site.register(Chronicle)
admin.site.register(VampireClan)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Location)
