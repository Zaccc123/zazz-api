from django.contrib import admin
from zazzapp.models import Shout


class ShoutAdmin(admin.ModelAdmin):
    list_display = ('message', 'created_by', 'created_at')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()


admin.site.register(Shout, ShoutAdmin)
