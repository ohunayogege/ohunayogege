from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Blog, Portfolio, Comment, PaymentCode
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
            return JsonResponse(response) # return response as JSON
        else:
        	response = { 'error': 'Please check all fields' }
        	return JsonResponse(response)


def ajax_comment(request):
    if request.is_ajax():
        name = request.POST.get('name', None) # getting data from input name id
        email = request.POST.get('email', None)  # getting data from input email id
        content = request.POST.get('content', None)  # getting data from input content id
        blog = request.POST.get('blog', None)  # getting data from input blog id
        blog = Blog.objects.get(id=blog)
        if email and name and content: #cheking if first_name and last_name have value
            instance = Comment.objects.create(blog=blog, content=content, name=name, email=email)
            if instance:
                msg = 'Comment Posted Successfully.'
            else:
                msg = 'Error Publishing Comment. Try Again.'
            response = {
                         'msg': msg # response message
                        }
            return JsonResponse(response) # return response as JSON
        else:
            response = { 'error': 'Please check all fields' }
            return JsonResponse(response)

def payment(request):
    code = request.GET.get('code')
    payments = PaymentCode.objects.filter(code=code)
    paid = PaymentCode.objects.get(code=code)
    price = paid.price*100
    return render(request, 'payment.html', {'payments': payments, 'price': price})
