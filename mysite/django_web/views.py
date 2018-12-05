from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request,'web/index.html', locals())