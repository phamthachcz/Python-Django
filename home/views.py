from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Sport, Post
from home.models import Contact
from home.forms import ContactForm
# Create your views here.
def home_index(request):
	sports = Sport.objects.all()
	posts = Post.objects.all().order_by("-date")
	return render(request,'home.html', {'sports':sports, 'posts': posts})

def about_index(request):
	sports = Sport.objects.all()
	return render(request, 'about.html', {'sports': sports})

def addcontact(request):
	sports = Sport.objects.all()
	contact_form = ContactForm()
	if request.method == "POST":
		contact_form = ContactForm(request.POST)
		if contact_form.is_valid():
			contact_form.save()
			contact_form = ContactForm()
	else:
		contact_form = ContactForm()
	return render(request, 'contact.html', {'sports':sports, 'contact_form': contact_form})

