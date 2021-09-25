from django.contrib import admin

from .models import Room, RoomImage


class RoomAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Room, RoomAdmin)
admin.site.register(RoomImage)
