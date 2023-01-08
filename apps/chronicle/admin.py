from django.contrib import admin

from .models import *

# Register your models here.
class RelationshipsInline(admin.TabularInline):
    model = CharacterRelationship
    fk_name = "character1"


class VampireCCInline(admin.TabularInline):
    model = VampireCC
    fk_name = "character"

class HumanCCInline(admin.TabularInline):
    model = HumanCC


class VampireClanAdmin(admin.ModelAdmin):
    exclude = ()

class CharacterAdmin(admin.ModelAdmin):
    inlines = [RelationshipsInline, HumanCCInline, VampireCCInline]


admin.site.register(Chronicle)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Location)
