from django.shortcuts import render_to_response
from ci.pv.models import PV

def this_year(request):
    last_pv = PV.objects.all().order_by('-date')[:0]
    if last_pv:
        current_year = last_pv[0].year
        latest_pv_list = PV.objects.all().order_by('-date').filter(year=current_year)
    else:
        latest_pv_list = []
    return render_to_response('pv/index.html', {
        'object_list': latest_pv_list, 'request': request})



