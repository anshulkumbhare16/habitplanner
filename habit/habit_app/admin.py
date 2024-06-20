from django.contrib import admin
from .models import Topic, UserDefinedUnits, Task, User

# Register your models here.



class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'name',
        'first_name',
        'last_name',
        'date_of_birth',
        'city',
        'zip_code',
        'mobile_number',
        'is_active',
        'is_staff',
        'created_at',
        'updated_at'
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
    list_filter =[
        'user_id',
        'start_date',
    ]
    list_per_page = 50



class UserDefinedUnitsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user_id',
        'unit',
    ]
    list_filter = [
        'user_id'
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
    list_filter = [
        'taskname',
        'topic_id',
        'user_id',
    ]
    list_per_page = 50




admin.site.register(User, UserAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(UserDefinedUnits, UserDefinedUnitsAdmin)
admin.site.register(Task, TaskAdmin)