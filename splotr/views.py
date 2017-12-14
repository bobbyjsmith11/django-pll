from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import os
import matplotlib
matplotlib.use('agg')
import skrf

# from .forms import UploadFileForm

# Create your views here.


def index(request):
    context = {}
    if request.method == "POST" and request.FILES['ts_file']:
        myfile = request.FILES['ts_file']
        context['ts_data'] = myfile.read().decode("utf-8")
        request.session['ts_data'] = context['ts_data']
        request.session['filename'] = myfile.name
        ftemp = open(myfile.name, 'w')
        ftemp.write(context['ts_data'])
        ftemp.close()
        os.remove(myfile.name)
    return render(request, 'splotr/splotr.html', context)

def test_ajax(request):
    mydict = {'hello': 'world',
               'key2': 85,
               'data':request.session['ts_data']}
    return JsonResponse(mydict)
    # return HttpResponse('you successfully called test_ajax')

def get_logmag(request):
    # mydict = {'hello': 'world',
    #            'key2': 85,
    #            'data':request.session['ts_data'],
    #            'filename':request.session['filename']}
    fo = open(request.session['filename'],'w')
    fo.write(request.session['ts_data'])
    fo.close()
    try:
        n = skrf.Network( request.session['filename'])
    except Exception as e:
        print(e)
    os.remove(request.session['filename'])

    d = { 'f':                  n.f.tolist(),
          'number_of_ports':    int(n.number_of_ports)
          }
    for j in range(n.number_of_ports):      # j is second port
        for k in range(n.number_of_ports):  # k is first port
            tmp = []
            d["s"+str(j+1)+str(k+1)+"db"] = n.s_db[:,j,k].tolist()
    return JsonResponse(d)