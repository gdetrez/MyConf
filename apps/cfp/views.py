from .models import Submission
from django.forms import ModelForm
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.core.urlresolvers import reverse
from django.core.mail import send_mail

class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ('title', 'abstract', 'speakers',
                  'contact_name', 'contact_email',
                  'video', 'accessible')

def submit(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SubmissionForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            submission = form.save()
            c = RequestContext(request,{'submission':submission})

            mail = loader.get_template('cfp/submit_mail')
            send_mail('[FSCONS 2012] Thanks for your submission',
                      mail.render(c),
                      'programme@fscons.org',
                      [submission.contact_email],
                      fail_silently=True)
            t = loader.get_template('cfp/show.djhtml')       
            return HttpResponse(t.render(c))
    else:
        form = SubmissionForm() # An unbound form

    t = loader.get_template('cfp/form.djhtml')
    c = RequestContext(request,{
        'form': form,
    })
    return HttpResponse(t.render(c))


def edit(request):
    if request.method == 'POST': # If the form has been submitted...
        token = request.POST.get('token')
    else:
        token = request.GET.get('token')
    submission = get_object_or_404(Submission, edit_token=token)
    if not submission.can_edit():
        t = loader.get_template('cfp/noedit.djhtml')
        c = RequestContext(request)
        return HttpResponse(t.render(c))

    if request.method == 'POST': # If the form has been submitted...
        form = SubmissionForm(request.POST, instance=submission)
        if form.is_valid(): # All validation rules pass
            submission = form.save()
            t = loader.get_template('cfp/show.djhtml')
            c = RequestContext(request,{'submission':submission})
            return HttpResponse(t.render(c))
    else:
        form = SubmissionForm(instance = submission) # An unbound form

    t = loader.get_template('cfp/form.djhtml')
    c = RequestContext(request,{
        'form': form,
        'token': token,
        'action': reverse('cfp:edit'),
    })
    response = HttpResponse(t.render(c))
    response['Cache-Control'] = 'no-cache'
    return response
