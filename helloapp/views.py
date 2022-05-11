import json
import datetime
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def health(request):
    now = datetime.datetime.utcnow()
    html = f"Time is: {now}"

    data = request.body.decode('utf-8')

    if data:
        html = f"{html}\n\nPayload: {data}"

    print (html)

    return HttpResponse(html)
