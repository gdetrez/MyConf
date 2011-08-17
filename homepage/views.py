from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.models import User,Group

def index(request):
    #staff = User.objects.filter(groups=Group.objects.get(name="Staff")).order_by("first_name")
    t = loader.get_template('home.djhtml')
    c = Context({
    #    'staff_list': staff,
    })
    return HttpResponse(t.render(c))

