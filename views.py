from ci.fortunes.models import Fortune
from django.shortcuts import render_to_response

def error_404_random_fortune(request):
    fortune = Fortune.objects.all().order_by('?')[0]
    response = render_to_response('fortune_404.html', {'object': fortune})
    response.status_code = 404
    return response

