from django.contrib import admin
from .models import UserProfile, Topic, UserDefinedUnits, Task

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'created_at',
        'modified_at',
    ]

class TopicAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user_id',
        'topic_name',
        'start_date',
        'end_date',
        'duration_days',
        'created_at',
        'modified_at',
    ]
    list_per_page = 50

class UserDefinedUnitsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user_id',
        'unit',
    ]

class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'taskname',
        'topic_id',
        'user_id',
        'times',
        'system_defined_unit',
        'user_defined_unit',
        'completed_times',
        'created_at',
        'modified_at',
    ]
    list_per_page = 50


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(UserDefinedUnits, UserDefinedUnitsAdmin)
admin.site.register(Task, TaskAdmin)