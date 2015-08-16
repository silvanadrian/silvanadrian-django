from django.db import models
from django.utils.timezone import now
from markdown import markdown
from django import forms
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError

# Create your models here.


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    budget = forms.ChoiceField(choices=(('<1000','<1000'), ('1000-2000','1000-2000'), ('>2000','>2000')))
    projecttype = forms.MultipleChoiceField(choices=(('Statische Website','Statische Webseite'), ('Dynamische Webseite','Dynamische Webseite'), ('Web Applikation','Web Applikation'),('Template/Theme','Template/Theme'), ('Logo/CI Design','Logo/CI Design'), ('Anderes','Anderes')),widget=forms.CheckboxSelectMultiple,required=True)
    startdatum = forms.ChoiceField(choices=(('ASAP','ASAP'), ('in 2 - 3 Monaten','in 2-3 Monaten'), ('in 4 - 6 Monaten','in 4-6 Monaten')))
    description = forms.CharField(widget=Textarea())
    sonstiges = forms.CharField(widget=Textarea(),required=False)



class Page(models.Model):
    title = models.CharField(u'title', max_length=255)
    text = models.TextField(u'text',blank=True)
    date_created = models.DateTimeField(u'date created')
    date_updated = models.DateTimeField(u'date updated')
    text_html = models.TextField(editable=False, blank=True,null=True)

    class Meta:
        verbose_name = u'page'
        verbose_name_plural = u'pages'

    def __unicode_(self):
        return u'%s (%s)' % (self.title,self.text)


    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        self.text_html = markdown(self.text, ['codehilite'])
        super(Page, self).save(*args, **kwargs)