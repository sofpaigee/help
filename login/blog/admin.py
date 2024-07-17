from django.contrib import admin
from .models import Incident, Tag, IncidentFile

class IncidentFileInline(admin.TabularInline):
    model = IncidentFile

class TagInline(admin.TabularInline):
    model = Tag.incident_set.through

admin.site.register(Incident)  

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(IncidentFile)
class IncidentFileAdmin(admin.ModelAdmin):
    pass
