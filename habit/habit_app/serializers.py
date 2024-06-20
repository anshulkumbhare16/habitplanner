from rest_framework import serializers
from .models import Topic, Task

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Topic
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Task
        fields = '__all__'