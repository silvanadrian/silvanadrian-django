from django.shortcuts import render,render_to_response
from .models import Page
from django.conf import settings
from twython import Twython
twitter = Twython('hCkbdXZwdoFoIJsQqANRQ', 'mccOHaIdUEH8hsLoX0VtYe3sjlgfaX2RiChHT02rg','163400534-6PVteKAIQZVGmU2drQZJ0huwU2nBYS0UWbY7qAxW', 'pP7pa4UH0klP8JlOFmYBL5JhlJkLxmZ0qcreSohjulsig')
# Create your views here.

def about(request):
    aboutpage = Page.objects.filter(title='about')
    tweets = twitter.get_home_timeline()
    context = {'aboutpage': aboutpage}
    return render(request, 'pages/about.html',context)



from django.shortcuts import render
from .models import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = 'Name:' + '\n' + str(cd['name']).strip('[]') + '\n\n'
            description = 'Description:' + '\n' + str(cd['description']).strip('[]') + '\n\n'
            budget = 'Budget' + '\n' + str(cd['budget']).strip('[]') + '\n'
            startdatum = 'Startdatum' + '\n' + str(cd['startdatum']).strip('[]') + '\n\n'
            projecttype = 'Projekttyp:' + '\n' + str(cd['projecttype']).strip('[]') + '\n\n'
            sonstiges = 'Sonstiges:' + '\n' + str(cd['sonstiges']).strip('[]') + '\n\n'
            message = name + description + budget + startdatum + projecttype + sonstiges
            send_mail('Projektanfrage',message,cd.get('email', 'noreply@silvanadrian.ch'),['hallo@silvanadrian.ch'])
            return HttpResponseRedirect('/contact/danke/')
    else:
        form = ContactForm()
    return render(request, 'pages/kontakt.html', {'form': form})

def thankyou(request):
    return render_to_response('pages/danke.html')
