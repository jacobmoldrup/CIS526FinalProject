from django.shortcuts import render

# Create your views here.
def post_main_page(request):
    return render(request, 'Layout/index.html', {})
