from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from teambuilder.apps.contact.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from teambuilder.settings import ADMIN_MAIL as _email


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']

        recipients = [_email]
        if subject and message and sender:
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('thanks/')
        else:
            pass

    ctx = {'form':form}
    return render_to_response('contact/contact.html', ctx, context_instance=RequestContext(request))

def thanks(request):
    message = 'Thanks for submitting us a message. We sincerely appreciate your taking time to provide your comments and feedback.'
    ctx = {'message':message}
    return render_to_response('contact/thanks.html', ctx, context_instance=RequestContext(request))