from django.contrib import admin

# Register your models here.
from timebound_v1.models import Thing

class ThingAdmin(admin.ModelAdmin):
	model = Thing
	list_display = ('name', 'description',)
	prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Thing, ThingAdmin) 
