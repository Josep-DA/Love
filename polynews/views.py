from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from .forms import LoveFrom


@csrf_exempt
def love_generator(request):
	context = {}
	if request.method == 'POST': 
		form = LoveFrom(request.POST) 
		if form.is_valid(): 
			to_name = form.cleaned_data['to_name']
			your_name = form.cleaned_data['your_name']
			your_email = form.cleaned_data['your_email']
			gender = form.cleaned_data['gender']
			
			love_url = f'http://127.0.0.1:8000/love/{to_name};{your_name};{gender};{your_email}'
			print(love_url)

			context['form'] = form
			context['love_url'] = love_url
			return render(request, 'polynews/lovegen.html', context)
	else:
		form = LoveFrom()
	
	context['form'] = form
	context['love_url'] = 'Fill in the form'
	return render(request, 'polynews/lovegen.html', context)

def love(request, dt):
	try:
		data = dt.split(';')
		to_name = data[0]
		from_name = data[1]
		gender = data[2]
		email = data[3]
	except:
		raise Http404("Page does not exist")
	
	return render(request, 'polynews/love.html', {
		'to_name':to_name.capitalize(), 
		'from_name':from_name.capitalize(),
		'gender':gender,
		'email': email
		})

def send_answer(request, dt):
	