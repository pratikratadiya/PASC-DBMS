from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm
from .models import user, Participant, Event, Registration, Slot_list

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = user

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('event',)}),
    )

    list_display = ['username','email','event']


admin.site.register(user, MyUserAdmin)
admin.site.register(Participant)
admin.site.register(Event)
admin.site.register(Registration)
admin.site.register(Slot_list)