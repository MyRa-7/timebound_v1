from django.forms import ModelForm

from timebound_v1.models import Thing

class ThingForm(ModelForm):
	class Meta:
		model = Thing
		fields = ('name', 'description',)
