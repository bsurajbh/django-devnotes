from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.views.decorators.http import require_http_methods
from . models import Devnote
from . forms import DevnoteForm


@csrf_exempt
@require_http_methods(["POST", ])
def add(request):
    """add new note"""
    data = {}
    form = DevnoteForm(request.POST)
    if form.is_valid():
        add_note = form.save(commit=False)
        add_note.save()
        data['status'] = 1
    else:
        data['status'] = 0
        data['error'] = form.errors.as_json(escape_html=True)
    return JsonResponse(data, safe=False)

def index(request):
    return render(request, 'devnotes/index.html', {})


@csrf_exempt
@require_http_methods(["POST", ])
def UpdateStatus(request):
    """update the status done/not done"""

    data = {'id': request.POST.get(
        'id', ''), 'status': request.POST.get('status', '')}
    try:
        note = Devnote.objects.get(pk=request.POST.get('id'))
    except Devnote.DoesNotExists:
        data['success'] = 0
        return JsonResponse(data, safe=False)
    note.status = not(bool(int((request.POST.get('status')))))
    note.save()
    data['success'] = 1
    return JsonResponse(data, safe=False)
