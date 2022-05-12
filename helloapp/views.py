import logging
import json
import datetime
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger('django')

@csrf_exempt
def health(request):
    now = datetime.datetime.utcnow()
    html = f"Time is: {now}"

    data = request.body.decode('utf-8')

    if data:
        html = f"{html}\n\nPayload: {data}"

    logger.info(html)

    return HttpResponse(html)
