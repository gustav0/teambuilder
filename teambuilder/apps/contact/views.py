from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from teambuilder.apps.contact.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

f = ContactForm() #AUN NO ESTA FUNCIONANDO

data = {'subject': 'hello',
        'message': 'Hi there',
        'sender': 'foo@example.com',
        'cc_myself': True}
f = ContactForm(data)

def contact(request):
    title = 'TeamBuilder - Contact Us'
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['ingferrermiguel@gmail.com']
            if cc_myself:
                recipients.append(sender)

            if subject and message and sender:
                try:
                    send_mail(subject, message, sender, recipients)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return HttpResponseRedirect('thanks/')
            else:
                return HttpResponse('Make sure all fields are entered and valid.')
    else:
        form = ContactForm() # An unbound form

    ctx = {'title':title, 'form':form}
    return render_to_response('contact/contact.html', ctx, context_instance=RequestContext(request))

def thanks(request):
    title = 'TeamBuilder - Thanks'
    message = 'Thanks for submitting us a message. We sincerely appreciate your taking time to provide your comments and feedback.'
    ctx = {'title':title, 'message':message}
    return render_to_response('contact/thanks.html', ctx, context_instance=RequestContext(request))