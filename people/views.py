# Copyright (C) 2011 Grégoire Détrez
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

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

