from myconf.schedule.models import *
from django.contrib import admin

class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('day', 'begin_time', 'end_time', 'duration')

admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(Room)

def color(obj):
    return """
<div style=\"height:1em;background:%s;border:thin solid black;\"></div>
""" % obj.get_html_color()
color.short_description = 'Color'
color.allow_tags = True
color.admin_order_field = 'color'

class TrackAdmin(admin.ModelAdmin):
    list_display = (color, 'name')
    list_display_links = ('name',)

admin.site.register(Track, TrackAdmin)

#class ChoiceInline(admin.StackedInline):
#    model = Choice
#    extra = 3

class PresenterInline(admin.TabularInline):
    model = Presenter
    extra = 1

class SessionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
                'fields': ('title', 'description', 'intended_audience')
        }),
        ('Scheduling', {
                'classes':('collapse',),
                'fields': ('track', 'time_slot', 'room')
        }),
    )
    inlines = [
        PresenterInline,
    ]


admin.site.register(Session, SessionAdmin)
admin.site.register(Presenter)
