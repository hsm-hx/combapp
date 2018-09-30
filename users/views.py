from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Member

def index(request):
    template = loader.get_template('users/index.html')

    member_list = Member.objects.all()
    context = {
        'member_list': member_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, member_id):
    return HttpResponse("You're looking at member %s" % member_id)

def results(request, member_id):
    response = "You're looking at the results of member %s"
    return HttpResponse(response % member_id)

def vote(request, member_id):
    return HttpResponse("You're voting on member %s" % member_id)

