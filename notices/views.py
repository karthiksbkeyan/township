from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Notice

def notice_list(request):
    notices = Notice.objects.order_by('-created_at')
    return render(request, 'notices/home.html', {'notices': notices})