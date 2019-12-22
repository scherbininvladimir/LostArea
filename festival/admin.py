from django.contrib import admin

from festival.models import Scene, Request, Voice, TimeSlot, SceneSlot

@admin.register(Scene)  
class SceneAdmin(admin.ModelAdmin):  
    pass


@admin.register(Request)  
class RequestAdmin(admin.ModelAdmin):  
    pass


@admin.register(Voice)  
class VoiceAdmin(admin.ModelAdmin):  
    pass


@admin.register(TimeSlot)  
class TimeSlotAdmin(admin.ModelAdmin):  
    pass


@admin.register(SceneSlot)  
class SceneSlotAdmin(admin.ModelAdmin):  
    pass

