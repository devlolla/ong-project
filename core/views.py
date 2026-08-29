from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

@login_required
def home(request):
    return render(request, "core/home.html")

def health_check(request):
    return HttpResponse("ok", content_type="text/plain")
