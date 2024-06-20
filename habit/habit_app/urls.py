from django.urls import path, include
from habit_app import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'topic', views.TopicApiViewSet)
router.register(r'task', views.TaskApiViewSet)
router.register(r'userdefinedunits', views.UserDefinedUnitsAPIViewSet)

urlpatterns = [
    path('habitapp/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('createplan/', views.create_new_plan),
]
