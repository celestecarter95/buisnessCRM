from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import FormView, ListView, DetailView, View
from django.views.generic.detail import SingleObjectMixin
from django.utils import timezone
from django.http import HttpResponseRedirect
import datetime

from viewsets import ModelViewSet
from .models import Stage, Company, Contact, Campaign, Opportunity, Reminder, Report, CallLog, OpportunityStage

class StageViewSet(ModelViewSet):
    model = Stage
    fields = ['name', 'order', 'descripton', 'value']
    success_url = reverse_lazy('crm:stage_list')

class Company(ListView):
    model = Company
    template_name = 'crm/company_list.html'
