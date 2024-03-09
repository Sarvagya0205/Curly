from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return HttpResponse("This is aboutpage")
def services(request):
    return HttpResponse("This is services page")
def contact(request):
    return(HttpResponse("this is contact page"))
def my_text_file_view(request):
    with open('path/to/your/text/file.txt', 'r') as file:
        text_content = file.read()
    
    return HttpResponse(text_content, content_type='text/plain')