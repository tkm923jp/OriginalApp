from django.contrib import admin
from .models import User,Schedule,Category,Schedulename,Timehour,Timeminutes

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group', 'category')
    search_fields = ('name',)
    list_filter = ('category',)

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('idnumber', 'calendar_day')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class SchedulenameAdmin(admin.ModelAdmin):
    list_display = ('schedule_name',)

class TimehourAdmin(admin.ModelAdmin):
    list_display = ('time_hour',)

class TimeminutesAdmin(admin.ModelAdmin):
    list_display = ('time_minutes',)

admin.site.register(User,UserAdmin)
admin.site.register(Schedule,ScheduleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Schedulename, SchedulenameAdmin)
admin.site.register(Timehour, TimehourAdmin)
admin.site.register(Timeminutes, TimeminutesAdmin)