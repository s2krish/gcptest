import datetime
from django.http import HttpResponse
# Create your views here.

def health(request):
    now = datetime.datetime.utcnow()
    html = f"Time is: {now}"
    return HttpResponse(html)
