from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Blog, Portfolio, Comment
# Create your views here.

def index(request):
	blogs = Blog.objects.all()
	portfolios = Portfolio.objects.all()
	return render(request, 'index.html', {'blogs': blogs, 'portfolios': portfolios})

def blog(request):
	# blogs = get_object_or_404(Blog, slug=slug)
	blogs = Blog.objects.all()
	return render(request, 'blog.html', {'blogs': blogs})

def blogview(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = Comment.objects.filter(blog=blog)
    return render(request, 'single.html', {'blog': blog, 'comments': comments})

# ajax_posting function
def ajax_contact(request):
    if request.is_ajax():
        name = request.POST.get('name', None) # getting data from input first_name id
        email = request.POST.get('email', None)  # getting data from input last_name id
        message = request.POST.get('message', None)  # getting data from input last_name id
        if email and name and message: #cheking if first_name and last_name have value
            response = {
                         'msg':'Your form has been submitted successfully' # response message
            			}
            print(True)
            return JsonResponse(response) # return response as JSON
        else:
        	print(False)
        	response = { 'error': 'Please check all fields' }
        	return JsonResponse(response)
