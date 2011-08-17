from django.http import HttpResponse
from django.template import RequestContext, loader
from notifications.models import Notification
# Create your views here.


def index(request):
    notifs = Notification.objects.all().order_by("-date")
    t = loader.get_template('notifications.djhtml')
    c = RequestContext(request,{
        'notification_list': notifs,
    })
    return HttpResponse(t.render(c))
