from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from datetime import datetime
from deal.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse



def index(request):
    context ={}
    return render_to_response('index.html', context, context_instance = RequestContext(request))
