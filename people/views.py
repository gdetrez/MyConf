from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.models import User,Group
from myconf.people.models import Profile

def staff(request):
    staff = User.objects.filter(groups=Group.objects.get(name="Staff")).order_by("first_name")
    t = loader.get_template('people/staff.djhtml')
    c = Context({
        'staff_list': staff,
    })
    return HttpResponse(t.render(c))

def user(request, uname):
    staff_member = User.objects.get(username=uname, groups=Group.objects.get(name="Staff"))
    t = loader.get_template('people/staffmember.djhtml')
    c = Context({
        'staff_member': staff_member,
    })
    return HttpResponse(t.render(c))

