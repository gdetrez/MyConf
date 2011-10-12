from django.forms import ModelForm
from apps.signup.models import SessionSignup
from schedule.models import Session
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader, RequestContext

from django.forms.widgets import HiddenInput

# Create your views here.

class SignupForm(ModelForm):
    class Meta:
        model = SessionSignup
        widgets = {
            'session': HiddenInput()
            }

    class Media:
         css = {
             'all': ('style/forms.css',)
             }


def signup(request, session_pk):
    session = get_object_or_404(Session, pk=session_pk)
    if request.method == 'POST': # If the form has been submitted...
        form = SignupForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect(session.get_absolute_url() + "?signedup=ok") # Redirect after POST
    else:
        s = SessionSignup(session=session)
        form = SignupForm(instance = s) # An unbound form

    t = loader.get_template('schedule/session_signup.djhtml')
    c = RequestContext(request,{
            'form': form,
            'session': session
            })
    return HttpResponse(t.render(c))
