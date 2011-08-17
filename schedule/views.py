# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from myconf.schedule.models import *

def schedule(request):
    sessions = Session.objects.all().order_by("time_slot__begin")
    t = loader.get_template('schedule/schedule.djhtml')
    c = Context({
           'list_sessions': sessions,
    })
    return HttpResponse(t.render(c))

# def user(request, uname):
#     staff_member = User.objects.get(username=uname, groups=Group.objects.get(name="Staff"))
#     t = loader.get_template('people/staffmember.html')
#     c = Context({
#         'staff_member': staff_member,
#     })
#     return HttpResponse(t.render(c))
