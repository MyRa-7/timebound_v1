from django.shortcuts import render

# Create your views here.
def index(request):
	number = 6
	# this is a new view
	thing = "Thing name"
	return render(request, 'index.html', {
			'number': number,
			'thing': thing,
		})