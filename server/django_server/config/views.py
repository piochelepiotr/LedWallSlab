from django.shortcuts import render, get_object_or_404
from datetime import datetime
from config.models import Configuration
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging

call_function = None


def set_call_function(function):
    global call_function
    call_function = function


def list_config(request):
    date = datetime.now()
    configs = Configuration.objects.all()
    return render(request, 'config/list-config.html', locals())


def edit_config(request, id):
    get_object_or_404(Configuration, id=id)
    return render(request, 'config/edit-config.html', locals())


def home(request):
    return render(request, 'config/home.html')


def get_config(request, id):
    if request.is_ajax():
        config_to_send = get_object_or_404(Configuration, id=id).config
        return HttpResponse(json.dumps(config_to_send), content_type="json")

@csrf_exempt
def save_config(request, id, apply=None):
    global call_function
    if request.is_ajax():
        if request.method == 'POST':
            received_json_data = json.loads(request.body.decode('utf-8'))
            saved_config = get_object_or_404(Configuration, id=id)
            try:
                saved_config.name = received_json_data['name']
                saved_config.description = received_json_data['description']
                saved_config.config = json.dumps(received_json_data)
                saved_config.save()
            except:
                print("Wrong JSON format !")
            if apply is not None:
                if call_function is not None:
                    call_function(received_json_data)
        return HttpResponse(json.dumps(received_json_data), content_type="json")