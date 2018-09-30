from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Member

def index(request):
    template = loader.get_template('users/index.html')

    member_list = Member.objects.all()
    context = {
        'member_list': member_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render(request, 'users/detail.html', {'member': member})

def results(request, member_id):
    response = "You're looking at the results of member %s"
    return HttpResponse(response % member_id)

def vote(request, member_id):
    return HttpResponse("You're voting on member %s" % member_id)

