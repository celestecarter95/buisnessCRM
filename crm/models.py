from django.db import models
from django.contrib.auth.models import User
import datetime

class Stage(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField(help_text = 'The order this is displayed on the screne')
    description = models.TextField(blank=True, null=True)
    value = models.IntegerField(help_text = 'On a scale of 0 to 100 of the stage of the pipeline')

    def __unicode__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(max_length=200, blank=True, null=True)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    zipcode = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "companies"

class Contact(models.Model):
    company = models.ForeignKey(Company, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    zipcode = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def __unicode__(self):
        return self.get_full_name()

class Campaign(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

class Opportunity(models.Model):
    stage = models.ForeignKey(Stage)
    company = models.ForeignKey(Company, blank=True, null=True)
    contact = models.ForeignKey(Contact)
    value = models.FloatField(help_text="How much this opportunity is worth to the organization")
    sourse = models.ForeignKey(Campaign, help_text="How did this contact find out about this?")
    user = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        if self.company:
            return self.company
        else:
            return self.contact

    class Meta:
        verbose_name_plural = "opportunities"

class Reminder(models.Model):
    opportunity = models.ForeignKey(Opportunity)
    date = models.DateField()
    note = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.opportunity + ": " + self.note

class Report(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField()

    def __unicode__(self):
        return self.name

class CallLog(models.Model):
    opportunity = models.ForeignKey(Opportunity)
    date = models.DateTimeField(auto_now_add=True)
    note = models.TextField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.opportunity + " on " + self.date.strftime("%Y-%m-%d") + " by " + self.user.get_full_name()

class OpportunityStage(models.Model):
    opportunity = models.ForeignKey(Opportunity)
    stage = models.ForeignKey(Stage)
    time_stamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.opportunity + " moved to " + self.stage
