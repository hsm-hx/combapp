from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from slacker import Slacker

import datetime

from .models import *
from . import forms, secret

CHANNEL_ID = 'G8XP0KUNQ'

class Slack(object):
  __slacker = None

  def __init__(self, token):
    self.__slacker = Slacker(token)

  def post_to_channel(self, channel, message):
    channel_name = "#" + channel
    self.__slacker.chat.post_message(CHANNEL_ID, message)

slack = Slack(secret.slack_token)

def index(request):
  equipment_list = Equipment.objects.all()
  context = {
    'equipment_list': equipment_list,
  }
  return render(request, 'equipments/index.html', context)

def detail(request, equipment_id):
  equipment = get_object_or_404(Equipment, pk=equipment_id)
  form = forms.BorrowForm()

  context = {
    'equipment': equipment,
    'form': form,
  }
  return render(request, 'equipments/detail.html', context)

def borrowing(request, equipment_id):
  equipment = get_object_or_404(Equipment, pk=equipment_id)

  context = {
    'equipment': equipment,
  }
  return render(request, 'equipments/borrow.html', context)

def returning(request, equipment_id):
  equipment = get_object_or_404(Equipment, pk=equipment_id)

  context = {
    'equipment': equipment,
  }
  return render(request, 'equipments/return.html', context)

def extension(request, equipment_id):
  equipment = get_object_or_404(Equipment, pk=equipment_id)

  context = {
    'equipment': equipment,
  }
  return render(request, 'equipments/extend.html', context)

def borrow_act(request, equipment_id):
  equipment = get_object_or_404(Equipment, pk=equipment_id)
  temp = Equipment.objects.get(pk=equipment_id)

  if temp.state == 0:
    dueday = datetime.date.today() + datetime.timedelta(days=13)

    temp.borrower = request.POST['name']
    temp.state = 1
    temp.due = dueday
    temp.save()

    slack.post_to_channel('bot_test', 'A equipment is borrowed!')

  return HttpResponseRedirect(reverse('equipments:index'))

def return_act(request, equipment_id):
  equipment = get_object_or_404(Equipment, pk=equipment_id)

  temp = Equipment.objects.get(pk=equipment_id)

  if temp.borrower == request.POST['name']:
    temp.borrower = ""
    temp.state = 0
    temp.save()

  return HttpResponseRedirect(reverse('equipments:index'))

def extend_act(request, equipment_id):
  equipment = get_object_or_404(Equipment, pk=equipment_id)

  temp = Equipment.objects.get(pk=equipment_id)

  if temp.borrower == request.POST['name']:
    if temp.due < datetime.date.today():
      dueday = datetime.date.today() + datetime.timedelta(days=7)
    else:
      dueday = temp.due + datetime.timedelta(days=7)
    temp.due = dueday
    temp.save()
    return HttpResponseRedirect(reverse('equipments:index'))
