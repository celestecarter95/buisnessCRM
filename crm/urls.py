from django.contrib.auth.decorators import login_required
from decorator_include import decorator_include
from django.conf.urls import url, include
from viewsets import ModelViewSet
from . import views
from .views import StageViewSet
from .models import Stage, Company, Contact, Campaign, Opportunity, Reminder, Report, CallLog, OpportunityStage

urlpatterns = [
    #url(r'^company/$', login_required(views.Company.as_view()), name="company"),
    #url('', decorator_include(login_required, include(ModelViewSet(Stage).urls))),
    url('', include(StageViewSet(Stage).urls)),
    url('', decorator_include(login_required, include(ModelViewSet(Company).urls))),
]
